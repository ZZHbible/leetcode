#!/usr/bin/env python
# author = 'ZZH'
# time = 2024/10/11
# project = vit_train

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
from transformers import  ViTImageProcessor, ViTModel

image_processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")


# CIFAR-10 数据集的自定义数据预处理
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, image_processor):
        self.dataset = dataset
        self.image_processor = image_processor

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        image, label = self.dataset[idx]
        # 使用 ViTImageProcessor 进行图像预处理
        inputs = self.image_processor(images=image, return_tensors="pt")
        inputs = {
            key: value.squeeze(0) for key, value in inputs.items()
        }  # 去除 batch 维度
        return inputs["pixel_values"], label  # 返回原始图像用于可视化


# 加载 CIFAR-10 数据集（不需要 transforms）
train_dataset = datasets.CIFAR10(root="./data", train=True, download=True)
test_dataset = datasets.CIFAR10(root="./data", train=False, download=True)

# 使用自定义的数据集类进行预处理
train_dataset = CustomDataset(train_dataset, image_processor)
test_dataset = CustomDataset(test_dataset, image_processor)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 加载预训练的 ViT 基础模型
vit_model = ViTModel.from_pretrained("google/vit-base-patch16-224")


class CustomViTForImageClassification(nn.Module):
    def __init__(self, num_labels):
        super(CustomViTForImageClassification, self).__init__()
        self.vit = ViTModel.from_pretrained("google/vit-base-patch16-224")
        self.classifier = nn.Linear(self.vit.config.hidden_size, num_labels)

    def forward(self, pixel_values):
        outputs = self.vit(pixel_values=pixel_values)
        # 提取 [CLS] token 的输出
        cls_output = outputs.last_hidden_state[
                     :, 0, :
                     ]  # shape: [batch_size, hidden_size]
        logits = self.classifier(cls_output)  # shape: [batch_size, num_labels]
        return logits


# 指定类别数量，例如 CIFAR-10 有 10 个类别
num_labels = 10

# 初始化自定义模型
model = CustomViTForImageClassification(num_labels=num_labels)

# 将模型移动到 GPU 上（如果可用）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# 训练模型的函数
def train_model(model, train_loader, criterion, optimizer, num_epochs=5):
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            inputs, labels = inputs.to(device), labels.to(device)

            # 前向传播
            logits = model(inputs)
            loss = criterion(logits, labels)

            # 反向传播与优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            if i % 100 == 99:  # 每 100 个小批次输出一次损失
                print(
                    f"Epoch [{epoch + 1}/{num_epochs}], Step [{i + 1}], Loss: {running_loss / 100:.4f}"
                )
                running_loss = 0.0


# 测试模型的函数
def test_model(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs).logits
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(
        f"Test Accuracy of the model on the test images: {100 * correct / total:.2f}%"
    )


# 开始训练模型
train_model(model, train_loader, criterion, optimizer, num_epochs=5)
# 测试模型的准确率
test_model(model, test_loader)

# 保存模型
torch.save(model.state_dict(), "vit_cifar10_transformers.pth")

# 加载模型
model.load_state_dict(torch.load("vit_cifar10_transformers.pth"))
model.eval()  # 切换到评估模式
