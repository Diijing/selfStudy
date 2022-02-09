# 58번
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# 입력 예시
# 0 0
#
# 출력 예시
# True
# a, b = map(int, input().split())
# print(bool(not a) and bool(not b))

# 78번
# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
# 입력 예시
# x
# b
# k
# d
# l
# q
# g
# a
# c
#
# 출력 예시
# x
# b
# k
# d
# l
# q
# a = 0
# while True:
#     a = input()
#     print(a)
#     if a == 'q':
#         break
# 문제 좀 이상하게 제시한듯

# 윈도우
# 운영체제의
# 파일
# 경로를
# 출력하는
# 연습을
# 해보자.
#
# 파일
# 경로에는
# 특수문자들이
# 포함된다.
#
# 다음
# 경로를
# 출력하시오.
#
# "C:\Download\'hello'.py"
# (단, 따옴표도 함께 출력한다.)

# print('"C:\Download\\\'hello\'.py"')
# 역슬래시 처리가 조금 어려웠음

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

