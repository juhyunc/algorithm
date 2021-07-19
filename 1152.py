# https://www.acmicpc.net/problem/1152

text = input()
if text == "":
    print(0)
elif text[0]==" " and text[-1]==" ": # 앞뒤 모두 공백이 있다
    n = text.count(" ")-1
    print(n)
elif text[-1]==" ": # 뒤에만 공백이 있다
    m = text.count(" ")
    print(m)
elif text[0]==" ": # 앞에만 공백이 있다
    k= text.count(" ")
    print(k)
elif text.count(" ")==0: # 단어가 한 개인 경우
    o = 1
    print(o)
else:
    p = text.count(" ") + 1
    print(p)

"""
<다른 풀이 참고>
input().split(" ") 이라는 코드를 사용한 경우가 있다.
이 경우 공백을 사이에 두고 두 개의 입력을 받았다면 말 그대로 두 개가 떨어져서 입력이 된다.

<오답이었을 때 다시 생각해보기>
1) 아무 것도 입력하지 않은 경우를 고려하지 않았다.
2) 입력한 단어가 한 개인 경우도 고려하지 않았었다.
"""




