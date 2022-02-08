# 61번

# a, b = map(int, input().split())
# print(a | b)

# 62번

# a, b = map(int, input().split())
# print(a ^ b)

# 63번

# a, b = map(int, input().split())
# print(a if a > b else b)

# 64번

# a, b, c = map(int, input().split())
# d = a if a < b else b
# e = b if b < c else c
# print(d if (d < e) else e)
# 이렇게 풀기는 풀었지만 계산식 안의 계산식으로 삼항연산자를 구성할 수 있다.

# 65번

# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)

# 66번

# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print('even')
# else:
#     print('odd')
# if b % 2 == 0:
#     print('even')
# else:
#     print('odd')
# if c % 2 == 0:
#     print('even')
# else:
#     print('odd')

# 67번

# a = int(input())
# if a < 0:
#     if a % 2 == 0:
#         print('A')
#     else:
#         print('B')
# elif a > 0:
#     if a % 2 == 0:
#         print('C')
#     else:
#         print('D')
# 인풋을 빼먹고 복사를 하지 않아서 첫 시도는 틀림

# 68번

# a = int(input())
# if a <= 39:
#     print('D')
# elif a <= 69:
#     print('C')
# elif a <= 89:
#     print('B')
# elif a <= 100:
#     print('A')

# 69번

# a = input()
# if a == 'A':
#     print('best!!!')
# elif a == 'B':
#     print('good!!')
# elif a == 'C':
#     print('run!')
# elif a == 'D':
#     print('slowly~')
# else:
#     print('what?')

# 70번

# a = int(input())
# win = [12, 1, 2]
# spr = [3, 4, 5]
# summ = [6, 7, 8]
# fal = [9, 10, 11]
# if a in win:
#     print('winter')
# if a in spr:
#     print('spring')
# if a in summ:
#     print('summer')
# if a in fal:
#     print('fall')
# 리스트화 하지 않아도 몫을 구하는 방식을 통해 풀 수 있다.
