# 61번
# 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
#
# 입력 예시
# 3 5
#
# 출력 예시
# 7
# a, b = map(int, input().split())
# print(a | b)

# 62번
# 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise) 연산자 ^(xor, circumflex/caret, 서컴플렉스/카릿)를 사용하면 된다.
# 입력 예시
# 3 5
#
# 출력 예시
# 6

# a, b = map(int, input().split())
# print(a ^ b)

# 63번
# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.
# 입력 예시
# 123 456
#
# 출력 예시
# 456
# a, b = map(int, input().split())
# print(a if a > b else b)

# 64번
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.
# 입력 예시
# 3 -1 5
#
# 출력 예시
# -1

# a, b, c = map(int, input().split())
# d = a if a < b else b
# e = b if b < c else c
# print(d if (d < e) else e)
# 이렇게 풀기는 풀었지만 계산식 안의 계산식으로 삼항연산자를 구성할 수 있다.

# 65번
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
# 입력 예시
# 1 2 4
#
# 출력 예시
# 2
# 4

# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)

# 66번
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
# 입력 예시
# 1 2 8
#
# 출력 예시
# odd
# even
# even
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
# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.
# 입력 예시
# -2147483648
#
# 출력 예시
# A
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
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
#
# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.
# 입력 예시
# 73
#
# 출력 예시
# B

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
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
#
# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?
# 입력 예시
# A
#
# 출력 예시
# best!!!

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
# 월이 입력될 때 계절 이름이 출력되도록 해보자.
#
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall
# 입력 예시
# 12
#
# 출력 예시
# winter
a = int(input())
win = [12, 1, 2]
spr = [3, 4, 5]
summ = [6, 7, 8]
fal = [9, 10, 11]
if a in win:
    print('winter')
if a in spr:
    print('spring')
if a in summ:
    print('summer')
if a in fal:
    print('fall')
# 리스트화 하지 않아도 몫을 구하는 방식을 통해 풀 수 있다.
