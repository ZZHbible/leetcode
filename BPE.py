import re
from collections import defaultdict

def get_stats(vocab):
    """
    统计词汇表中每对相邻字符的频率
    """
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, vocab):
    """
    合并词汇表中出现次数最多的一对相邻字符
    """
    new_vocab = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in vocab:
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab

# 示例输入
corpus = ["low", "lower", "newest", "widest"]

# 初始化词汇表
vocab = defaultdict(int)
for word in corpus:
    vocab[' '.join(list(word)) + ' </w>'] += 1  # 在每个单词的末尾添加 </w> 表示单词结束

# BPE 迭代
num_merges = 10
for i in range(num_merges):
    pairs = get_stats(vocab)
    best_pair = max(pairs, key=pairs.get)
    vocab = merge_vocab(best_pair, vocab)

# 打印最终词汇表
print("Final Vocabulary:")
print(vocab)
