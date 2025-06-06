#姓名：王薪洋，学号：24210227016，日期，25.6.6
from collections import Counter
import re

text = """
Climate change is one of the most significant challenges facing humanity today.
Rising global temperatures, melting polar ice caps, and increasing sea levels are clear indicators of a warming planet.
Scientists have warned that if greenhouse gas emissions continue to rise, the consequences could be catastrophic.
Extreme weather events, such as hurricanes, droughts, and wildfires, are becoming more frequent and intense.
These changes threaten ecosystems, agriculture, and human health.
To combat climate change, governments and individuals must work together to reduce carbon footprints,
invest in renewable energy, and promote sustainable practices.
Every small action, from recycling to using public transportation, can make a difference.
The time to act is now; the future of our planet depends on it.
"""

words = re.findall(r'\b\w+\b', text.lower())

word_counts = Counter(words)

top_five_words = word_counts.most_common(5)

print("单词出现次数统计：")
for word, count in word_counts.items():
    print(f"{word}: {count}")

print("\n出现频率最高的前 5 个单词：")
for word, count in top_five_words:
    print(f"{word}: {count}")