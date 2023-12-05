# #!/usr/bin/env python
# # author = 'ZZH'
# # time = 2023/12/4
# # project = bleu_demo
from collections import Counter

from nltk import ngrams
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import math
from collections import defaultdict

# 参考翻译
reference = ["The cat is sitting on the mat".split(), "The cat is lying on the mat".split()]

# 机器翻译结果
candidate = "The cat is on the mat".split()

# 计算BLEU分数
bleu_score = sentence_bleu(reference, candidate,weights=[0.3,0.3,0.4])

print(f"BLEU Score: {bleu_score}")

weight = [0.3,0.3,0.4]
ans= 0
epsilon = 1e-12
for n in range(len(weight)):
    c = Counter(ngrams(candidate,n+1))
    count_dic =defaultdict(int)
    for ref in reference:
        for key,val in Counter(ngrams(ref,n+1)).items():
            if key in c:
                count_dic[key]=max(count_dic[key],val)
    Count = sum(c.values())
    num = 0
    for key in count_dic:
        num += min(c[key],count_dic[key])
    ans += weight[n] * math.log((num+epsilon) / (Count+epsilon),math.e)
    print(ans)
temp  = min(reference,key=lambda x:len(x)-len(candidate))
if len(candidate) > len(temp):
    BP=1
else:
    BP=pow(math.e,1-len(temp)/len(candidate))
bleu_score = BP* pow(math.e,ans)
print(f"BLEU Score: {bleu_score}")

print(list(ngrams(candidate,1)))
