# 51번
# 두 정수(a, b)를 입력받아
# a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.
# 입력 예시
# 0 1
#
# 출력 예시
# True

# a, b = map(int, input().split())
# print(a != b)

# 52번
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
# 입력 예시
# 0
#
# 출력 예시
# False

# a = int(input())
# print(bool(a))

# 53번
# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.
# 입력 예시
# 1
#
# 출력 예시
# False

# a = int(input())
# print(not a)

# 54번
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# 입력 예시
# 1 1
#
# 출력 예시
# True
# a, b = map(int, input().split())
# print(bool(a and b))

# 55번
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# 입력 예시
# 1 1
#
# 출력 예시
# True
# a, b = map(int, input().split())
# print(bool(a or b))

# 56번
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
# 입력 예시
# 1 1
#
# 출력 예시
# False
# a, b = map(int, input().split())
# print(bool(a) != bool(b))

# 57번
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
# 입력 예시
# 0 0
#
# 출력 예시
# True
# a, b = map(int, input().split())
# print(bool(a) == bool(b))

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
# 이거는 좀 헷갈렸다.

# 59번
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)
# 입력 예시
# 2
#
# 출력 예시
# -3

# a = int(input())
# b = ~a
# print(b)

# 60번
# 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)
# 입력 예시
# 3 5
#
# 출력 예시
# 1
a, b = map(int, input().split())
print(a & b)