# https://www.acmicpc.net/problem/1008
# A/B 구하기

number = input()
a= int(number[0])
b= int(number[-1])
c = a/b
print(c)

"""
<문제번호 1000에서 오답이었을 때 다시 생각해보기>
(0 < A, B < 10)라는 조건이 A는 0보다 크고, B는 10보다 작다고 생각했다.
문제에서 원하는 조건은 A와 B가 0과 10 사이라는 뜻이었다.

1000번: 7번째 줄을 c = a+b 로 바꾸면 됨.
1001번: 7번째 줄을 c = a-b 로 바꾸면 됨.
"""