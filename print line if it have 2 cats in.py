# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
#
# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так
#
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     # process line


# catcat
# cat and cat
# catac
# cat
# ccaatt

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall("cat", line)) >= 2:
        print(line)

# import sys
# import re
#
# pattern = r'(cat.*){2,}'
# lst = []
# for line in sys.stdin:
# 	line = line.rstrip()
# 	if re.findall(pattern, line):
# 		print(line)
