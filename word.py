"""
统计文章 出现频率最高的前 10 个「二元词组」，并输出它们的频率。
"""

import operator

with open("happiness_seg.txt", encoding='utf-8') as f:
    text = f.read()

words = text.split()
num_of_words = len(words)
words2 = [(words[i], words[i+1]) for i in range(num_of_words-1)]

# 移除标点符号
punctuation = """，。,.？?―“”‘’"""

words2_clean = []

for words in words2:
    if (words[0] not in punctuation) and (words[1] not in punctuation):
        words2_clean.append(words)

# 统计二元词组频率
words2_freq = {}

for words in words2_clean:
    if words not in words2_freq:
        words2_freq[words] = 1
    else:
        words2_freq[words] += 1

words2_freq_sorted_reverse = sorted(
            words2_freq.items(), key=operator.itemgetter(1),reverse=True)

print("出现频率最高的前 10 个「二元词组」是")
for i in range(10):
    print(words2_freq_sorted_reverse[i])
