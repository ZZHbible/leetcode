#!/usr/bin/env python
# author = 'ZZH'
# time = 2024/10/23
# project = patch embedding
import torch.nn as nn
import torch

class PatchEmbedding(nn.Module):
    def __init__(self, patch_size, in_chans, embed_dim):
        super(PatchEmbedding, self).__init__()
        self.patch_size = patch_size
        self.in_chans = in_chans
        self.embed_dim = embed_dim

        # 使用卷积层将图像分成 patch，并进行通道数的映射
        self.proj = nn.Conv2d(
            in_chans, embed_dim,
            kernel_size=patch_size,
            stride=patch_size
        )

    def forward(self, x):
        B, C, H, W = x.size()

        # 检查图像尺寸是否可以被 patch_size 整除
        assert H % self.patch_size == 0 and W % self.patch_size == 0, \
            "输入图像的高度和宽度必须是 patch 大小的整数倍"

        # 通过卷积直接进行 patch embedding
        x = self.proj(x)  # (B, embed_dim, H/patch_size, W/patch_size)

        # 调整形状为 (B, num_patches, embed_dim)
        x = x.flatten(2)  # (B, embed_dim, num_patches)
        x = x.transpose(1, 2)  # (B, num_patches, embed_dim)

        return x

# 测试代码
img = torch.randn(1, 3, 224, 224)  # 模拟输入图像
patch_embedding = PatchEmbedding(patch_size=16, in_chans=3, embed_dim=768)  # 初始化模块
output = patch_embedding(img)  # 前向传播

print(output.size())  # 输出形状

