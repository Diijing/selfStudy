# 81번

# a = input()
# b = int('0x'+a, 16)
# c = int('0xF', 16)
# for i in range(1, c+1):
#     print('%s*%X=%X' % (a, i, b*i))
# 아스키 코드에 대한 이해도 및 16진수의 포매팅에 대한 이해가 부족하면 풀기 힘들듯
# 풀 때도 좀 까다로웠다

# 82번

# a = int(input())
# for i in range(1, a+1):
#     b = str(i)
#     if '3' in b:
#         print('X', end=' ')
#     elif '6' in b:
#         print('X', end=' ')
#     elif '9' in b:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')
# 마지막에 공백 있어서 틀릴 수도 있겠다 생각함
# 10으로 나눠줘도 된다니

# 83번

# r, g, b = map(int, input().split())
# cCount = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             cCount += 1
#             print(i, j, k)
# print(cCount)

# 84번

# h, b, c, s = map(int, input().split())
# mega = (h * b * c * s)/(8 * 1024 * 1024)
# print('%.1f MB' % mega)
# 문제는 길지만 어렵지 않음

# 85번

# w, h, b = map(int, input().split())
# pixel = (h * w * b)/(8 * 1024 * 1024)
# print('%.2f MB' % pixel)
# 위와 같다

# 86번

# a = int(input())
# sumC = 0
# n = 1
# while sumC < a:
#     sumC += n
#     n += 1
# print(sumC)
# 이러한 문제는 항상 범위를 지정해 주는 것에서 약간 틀린다. 주의하자

# 87번

# a = int(input())
# for i in range(1, a+1):
#     if i % 3 == 0:
#         continue
#     print(i, end=' ')

# 88번

# a, d, n = map(int, input().split())
# result = a + (n-1) * d
# print(result)

# 89번

# a, r, n = map(int, input().split())
# result = a * r ** (n-1)
# print(result)

# 90번

# a, m, d, n = map(int, input().split())
# for i in range(1, n+1):
#     if i == 1:
#         result = a
#     else:
#         result *= m
#         result += d
# print(result)
# 초항을 너무 안일하게 설정해버렸다. 1로 고쳐주니 바로 ok