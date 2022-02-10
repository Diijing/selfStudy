# 91번

# a, b, c = map(int, input().split())
# d = 1
# while d%a!=0 or d%b!=0 or d%c!=0 :
#   d += 1
# print(d)
# 특이하기도 하고 신기하기도 하다. 최소공배수를 구하는 방식보다 빠르다.

# 92번

# n = int(input())
# a = input().split()
# attend = [0] * 23
# for i in a:
#     b = int(i)
#     attend[b-1] += 1
# for j in attend:
#     print(j, end=' ')

# 93번

# n = int(input())
# a = input().split()
# a.reverse()
# for i in a:
#     print(i, end=' ')

# 94번

# n = int(input())
# a = list(map(int, input().split()))
# minIndex = 0
# for i in range(len(a)):
#     if a[minIndex] > a[i]:
#         minIndex = i
# print(a[minIndex])
# 최소값 코드인데 선택정렬이랑 헷갈렸음

# 95번

# n = int(input())
# graph = [[0] * 19 for i in range(19)]
# for i in range(n):
#     a, b = map(int, input().split())
#     graph[a-1][b-1] = 1
# for num1 in graph:
#     for num2 in num1:
#         print(num2, end=' ')
#     print()
# 문제에서는 리스트 내 아이템에 더하는 것이 아닌 입력을 원했다

# 96번

# baduk = [[] for _ in range(19)]
# for i in range(19):
#     graph = list(map(int, input().split()))
#     baduk[i] = graph
#     # 그래프는 19개
# n = int(input())
# spot = [[] for _ in range(n)]
# for j in range(n):
#     a, b = map(int, input().split())
#     spot[j] = (a-1, b-1)
# for k in spot:
#     for idx, number in enumerate(baduk[k[0]]):
#         if number == 1:
#             baduk[k[0]][idx] = 0
#         elif number == 0:
#             baduk[k[0]][idx] = 1
#     # 가로 바꾸기
#     for r in range(19):
#         if baduk[r][k[1]] == 0:
#             baduk[r][k[1]] = 1
#         elif baduk[r][k[1]] == 1:
#             baduk[r][k[1]] = 0
#         # 세로 바꾸기
# for num1 in baduk:
#     for num2 in num1:
#         print(num2, end=' ')
#     print()
#     # 뽑아주기

# 97번

# h, w = map(int, input().split())
# floor = [[0 for _ in range(w)] for _ in range(h)]
# n = int(input())
# for i in range(n):
#     l, d, x, y = map(int, input().split())
#     if d == 0:
#         for i in range(l):
#             floor[x - 1][y - 1 + i] = 1
#     elif d == 1:
#         for j in range(l):
#             floor[x - 1 + j][y - 1] = 1
# for num1 in floor:
#     for num2 in num1:
#         print(num2, end=' ')
#     print()
# 이거 할 때 생각보다 느낌이 너무 좋았다. 완전히 머릿속에서 구상할 수 있게 됨

# 98번

# maze = [[] for _ in range(10)]
# for i in range(10):
#     graph = list(map(int, input().split()))
#     maze[i] = graph
# antx = 1
# anty = 1
# maze[antx][anty] = 9
# while True:
#     if maze[antx][anty + 1] == 0:
#         anty += 1
#         maze[antx][anty] = 9
#     elif maze[antx + 1][anty] == 0:
#         antx += 1
#         maze[antx][anty] = 9
#     elif maze[antx][anty + 1] == 2 or maze[antx+1][anty] == 2:
#         if maze[antx][anty + 1] == 2:
#             maze[antx][anty + 1] = 9
#         else:
#             maze[antx + 1][anty] = 9
#         break
#     if maze[antx + 1][anty] == 1 and maze[antx][anty + 1] == 1:
#         break
# for num1 in maze:
#     for num2 in num1:
#         print(num2, end=' ')
#     print()
# if와 elif의 관계, 종료 시점과 등호 설정 등 여러 가지를 배울 수 있었던 문제였다.