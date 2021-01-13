# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
#
# Примечание:
# Обратите внимание на параметр count у функции sub.
# Sample Input:
#
# There’ll be no more "Aaaaaaaaaaaaaaa"
# AaAaAaA AaAaAaA
# Sample Output:
#
# There’ll be no more "argh"
# argh AaAaAaA
import sys
import re

pattern = r"\ba+\b"
replacement_for_sub = "argh"
for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(pattern, replacement_for_sub, line, count=1, flags=re.IGNORECASE)
    print(new_line)