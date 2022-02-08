#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/1/27
# project = leetcode2047
class Solution:
    def countValidWords(self, sentence: str) -> int:
        Punctuation = ['!', '.', ',']
        hyphen = '-'
        number = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']
        def check(token):
            if token.find('-') != token.rfind('-'):
                return False
            for i in Punctuation:
                if token.find(i)!= token.rfind(i):
                    return False

            for index,i in enumerate(token):
                if i not in number and i != hyphen and i not in Punctuation:
                    return False
                if i=='-':
                    if index <1 or index >=len(token)-1:
                        return False
                    if token[index-1] not in number or token[index+1] not in number:
                        return False
                if i in Punctuation:
                    if index != len(token)-1:
                        return False

            return True

        tokens = sentence.split()
        ret = 0
        for token in tokens:
            if check(token):
                ret += 1

        return ret

solution=Solution()
print(solution.countValidWords("a-b-c"))