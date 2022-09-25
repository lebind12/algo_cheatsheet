import sys


# 1차원 리스트에서 연속되는 값 중 최대 값을 출력.
list = list(map(int, sys.stdin.readline().rstrip().split(",")))
max_count = 0
count = 1
max_element = list[0]
for i in range(1, len(list)):
    if list[i] == list[i - 1]:
        count += 1
    else:
        if max_count < count:
            max_count = count
            max_element = list[i-1]
        count = 1
print("MAX ELEMENT IS " + str(max_element))
print("MAX COUNT IS " + str(max_count))
