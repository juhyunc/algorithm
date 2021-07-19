# https://www.acmicpc.net/problem/2475
# 검증수
text = input().split(" ")
a = 0
for t in text:
    var_t = int(t)
    a += var_t * var_t
print(a % 10)





