# 21번

# a = input()
# for i in range(len(a)):
#     print(a[i])
# 문제 이해를 제대로 하지 못해서 1차 시도는 틀림.

# 22번

# a = input()
# for i in range(3):
#     j = 2 * i
#     print(a[j:j+2],end=' ')
# 이런 방식으로 풀어도 되고 인덱싱을 따로 해줘도 됨

# 23번

# a, b, c = input().split(':')
# print(b)

# 24번

# a, b = input().split()
# print(a + b)

# 25번

# a, b = map(int, input().split())
# print(a+b)
# 문제에서는 따로따로 정수화했지만 map을 쓰면 편하게 정수화 가능

# 26번

# a = float(input())
# b = float(input())
# print(a + b)

# 27번

# a = hex(int(input()))
# print(a[2:])
# 처음에는 헷갈렸는데 그냥 16진수 뽑아주고 인덱싱 쓰면 편하다는 것을 알게됨

# 28번

# a = int(input())
# print('%X' % a)
# X자를 크게 입력하면 대문자로 나온다는 것을 처음 알았음

# 29번
#
# a = int(input(), 16)
# b = oct(a)
# print(b[2:])
# 처음에 :의 방향을 잘못 설정해서 틀림. 그리고 %o로 뽑아줘도 됨

# 30번

# a = ord(input())
# print(a)