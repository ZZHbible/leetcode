#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/12/3
# project = transformer_demo
import math

import torch
import torch.nn as nn

# 设置PyTorch随机种子
from torch import optim

torch.manual_seed(42)


class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, heads, dropout=0.1):
        super(MultiHeadAttention, self).__init__()
        self.embed_size = embed_size
        self.h = heads
        self.h_dim = embed_size // heads

        assert (
                self.h_dim * self.h == self.embed_size
        ), "embedding size need to be divisible by heads"

        self.q = nn.Linear(self.embed_size, self.embed_size)
        self.k = nn.Linear(self.embed_size, self.embed_size)
        self.v = nn.Linear(self.embed_size, self.embed_size)
        self.dropout = nn.Dropout(dropout)
        self.fc_out = nn.Linear(self.embed_size, self.embed_size)
        self.atten = None  # attention 张量, 后续可以可视化

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, mask=None):
        N, L = q.size(0), q.size(1)
        q, k, v = self.q(q), self.k(k), self.v(v)
        q = q.reshape(N, L, self.h, self.h_dim)
        k = k.reshape(N, L, self.h, self.h_dim)
        v = v.reshape(N, L, self.h, self.h_dim)
        energy = torch.einsum("nqhd,nkhd->nhqk", q, k)
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))
        self.attention = torch.nn.functional.softmax(energy / math.sqrt(self.h_dim), dim=-1)
        if self.dropout:
            self.attention = self.dropout(self.attention)
        out = torch.einsum("nhql,nlhd->nhqd", self.attention, v).transpose(1, 2).reshape(N, L, -1)
        out = self.fc_out(out)
        return out


class FFN(nn.Module):
    def __init__(self, d_model, hidden, dropout=0.1):
        super(FFN, self).__init__()
        self.d_model = d_model
        self.hidden = hidden
        self.f1 = nn.Linear(d_model, hidden)
        self.relu = nn.ReLU()
        self.f2 = nn.Linear(hidden, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        return self.f2(self.dropout(self.relu(self.f1(x))))


class EncoderLayer(nn.Module):
    def __init__(self, embed_size, heads, forward_expansion, dropout=0.1):
        super(EncoderLayer, self).__init__()
        self.attention_layer = MultiHeadAttention(embed_size=embed_size, heads=heads, dropout=dropout)
        self.layer_norm1 = nn.LayerNorm(normalized_shape=embed_size)
        self.ffn = FFN(d_model=embed_size, hidden=embed_size * forward_expansion, dropout=dropout)
        self.layer_norm2 = nn.LayerNorm(normalized_shape=embed_size)

    def forward(self, x: torch.Tensor, src_mask):
        out = self.attention_layer(x, x, x, src_mask)
        layer_norm1 = self.layer_norm1(x + out)
        ffn_out = self.ffn(layer_norm1)
        out = self.layer_norm2(layer_norm1 + ffn_out)
        return out


class PositionalEncoding(nn.Module):
    def __init__(self, embed_size, max_len):
        super(PositionalEncoding, self).__init__()
        self.encoding = torch.zeros(max_len, embed_size)
        self.encoding.requires_grad = False  # we don't need to compute gradient
        pos = torch.arange(0, max_len)
        pos = pos.float().unsqueeze(dim=1)
        _2i = torch.arange(0, embed_size, step=2).float()
        self.encoding[:, 0::2] = torch.sin(pos / (10000 ** (_2i / embed_size)))
        self.encoding[:, 1::2] = torch.cos(pos / (10000 ** (_2i / embed_size)))

    def forward(self, x):
        # self.encoding
        # [max_len = 512, d_model = 512]

        batch_size, seq_len = x.size()
        # [batch_size = 128, seq_len = 30]

        return self.encoding[:seq_len, :]


class TransformerEmbedding(nn.Module):
    def __init__(self, vocab_size, embed_size, max_len=256, drop_prob=0.1):
        super(TransformerEmbedding, self).__init__()
        self.tok_emb = nn.Embedding(vocab_size, embedding_dim=embed_size)
        self.pos_emb = PositionalEncoding(embed_size, max_len)
        self.drop_out = nn.Dropout(drop_prob)

    def forward(self, x):
        tok_emb = self.tok_emb(x)
        pos_emb = self.pos_emb(x)
        return self.drop_out(tok_emb + pos_emb)


class Encoder(nn.Module):
    def __init__(self, embed_size, heads, vocab_size, forward_expansion=2, n_layers=6, dropout=0.1):
        super(Encoder, self).__init__()
        self.emb = TransformerEmbedding(vocab_size, embed_size)
        self.layers = nn.ModuleList([
            EncoderLayer(embed_size=embed_size, heads=heads, forward_expansion=forward_expansion, dropout=dropout)
            for _ in range(n_layers)
        ])

    def forward(self, x, src_mask):
        x = self.emb(x)
        for layer in self.layers:
            x = layer(x, src_mask)
        return x


class DecoderLayer(nn.Module):
    def __init__(self, embed_size, heads, forward_expansion=2, dropout=0.1):
        super(DecoderLayer, self).__init__()
        self.attention = MultiHeadAttention(embed_size=embed_size, heads=heads, dropout=dropout)
        self.layernorm1 = nn.LayerNorm(embed_size)
        self.enc_dec_attention = MultiHeadAttention(embed_size=embed_size, heads=heads, dropout=dropout)
        self.layernorm2 = nn.LayerNorm(embed_size)
        self.ffn = FFN(d_model=embed_size, hidden=embed_size * forward_expansion, dropout=dropout)
        self.layernorm3 = nn.LayerNorm(embed_size)

    def forward(self, dec, enc, trg_mask, src_mask):
        x = self.attention(dec, dec, dec, trg_mask)
        x = self.layernorm1(dec + x)
        x = self.layernorm2(x + self.enc_dec_attention(x, enc, enc, src_mask))
        x = self.layernorm3(x + self.ffn(x))
        return x


class Decoder(nn.Module):
    def __init__(self, embed_size, heads, n_layers=6, forward_expansion=2, vocab_size=3124, max_len=256, dropout=0.1):
        super(Decoder, self).__init__()
        self.emb = TransformerEmbedding(vocab_size=vocab_size, embed_size=embed_size, max_len=max_len)
        self.layers = nn.ModuleList([
            DecoderLayer(embed_size=embed_size, heads=heads, forward_expansion=forward_expansion, dropout=dropout)
            for _ in range(n_layers)
        ])
        self.linear = nn.Linear(embed_size, vocab_size)

    def forward(self, x, enc, trg_mask, src_mask):
        x = self.emb(x)
        for layer in self.layers:
            x = layer(x, enc, trg_mask, src_mask)
        output = self.linear(x)
        return output


class Transformer(nn.Module):
    def __init__(self, src_pad_idx, trg_pad_idx, trg_sos_idx, voc_size, embed_size, n_head, max_len,
                 forward_expansion, n_layers, drop_prob, device):
        super(Transformer, self).__init__()
        self.src_pad_idx = src_pad_idx
        self.trg_pad_idx = trg_pad_idx
        self.trg_sos_idx = trg_sos_idx

        self.encoder = Encoder(embed_size=embed_size, heads=n_head, vocab_size=voc_size,
                               forward_expansion=forward_expansion, n_layers=n_layers, dropout=drop_prob)
        self.decoder = Decoder(embed_size=embed_size, heads=n_head, n_layers=n_layers,
                               forward_expansion=forward_expansion, vocab_size=voc_size, max_len=max_len,
                               dropout=drop_prob)

    def forward(self, src, trg):
        src_mask = self.make_src_mask(src)
        trg_mask = self.make_trg_mask(trg)
        enc_src = self.encoder(src, src_mask)
        output = self.decoder(trg, enc_src, trg_mask, src_mask)
        return output

    def make_src_mask(self, src):
        src_mask = (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)
        return src_mask

    def make_trg_mask(self, trg):
        trg_pad_mask = (trg != self.trg_pad_idx).unsqueeze(1).unsqueeze(3)
        trg_len = trg.shape[1]
        trg_sub_mask = torch.tril(torch.ones(trg_len, trg_len)).type(torch.ByteTensor)
        trg_mask = trg_pad_mask & trg_sub_mask
        return trg_mask

# model = MultiHeadAttention(768,8)
# q= torch.tensor([[[i for i in range(16)]*(768//16),[2]*768],[[10]*768,[20]*768]],dtype=torch.float32)
# k= torch.tensor([[[i for i in range(16)]*(768//16),[2]*768],[[10]*768,[20]*768]],dtype=torch.float32)
# v= torch.tensor([[[i for i in range(16)]*(768//16),[2]*768],[[10]*768,[20]*768]],dtype=torch.float32)
# model(q,k,v)
