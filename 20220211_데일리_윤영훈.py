# 1. 모험가 길드
# n = 모험가의 수
# 둘째 줄: 각 모험가의 공포도의 값이 N 이하의 자연수로 주어지며, 각 자연수는 공백 구분
#
# 그리디 알고리즘 : 큰 친구부터 짝을 지어주면 좋겠다(큰 사람끼리)
# 어차피 공포도가 낮은 사람은 혼자서도 충분하니 큰 수끼리 묶어주면 될듯

# n = int(input())
# # 어떻게 n번의 입력을 받을 수 있을까(공백을 통해서)
# a = input().split()
# for idx, i in enumerate(a):
#     a[idx] = int(i)
# # 먼저 정렬한 이후에 뒤에서부터 묶어주면 되지 않을까?
# a.sort()
# count = 0
# print(a)
# while a:
#     del a[-1:(-a[-1]-1):-1]
#     # 여기가 정렬 후에 뒤에서부터 그 수만큼 잡아먹는 구조
#     count += 1
# print(count)

# 2. 곱하기 혹은 더하기
# 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 s 받는다.
# s = 문자열(숫자로 바꿀 수 있는)
# 이 문제는 0일 때만 제외하고는 무조건 곱셈을 해주는 것이 유리하다는
# 사실을 쉽게 확인할 수 있다.

# s = input()
# nums = []
# result = 0
# # s를 각자 한자리의 자연수로 분리해야 하기 때문에 리스트 만들어주기
# for num in s:
#     nums.append(int(num))
# # 순서대로 넣기
# for i in range(len(nums)):
#     if i == 0:
#         if nums[i] <= 1 or nums[i+1] <=1 :
#             result = nums[i] + nums[i+1]
#         else:
#             result = nums[i] * nums[i+1]
#     elif i == 1:
#         continue
#     # 여기 부분에서 시간 진짜 오래걸림. 쓸데없이 많은 시간을 i = 0, 1 설정하는데 써버렸음
#     else:
#         if nums[i] == 0:
#             result += nums[i]
#         else:
#             result *= nums[i]
# print(result)

# 1번 문제는 얼추 들어맞았지만, 2번 문제는 완전히 틀렸다고 볼 수 있습니다.
# 일단 문자열도 iterable하기 때문에 굳이 리스트를 만들어 줄 필요도 없었고,
# result와 잘 분리해내기 위해서 0번과 1번을 굳이 어렵게 분류할 필요도 없었습니다.
# 그리고 결정적으로 0은 고려했으나 1의 경우 그대로 곱하는 과정을 거쳐서
# 답이 더 적게 나올 수 밖에 없었습니다. 1의 경우에도 그대로 더해주는 과정을 거쳐야
# 값이 극대화됩니다.

# s = input()
# result = int(s[0])
# # 첫번째 문자를 숫자로 바꿔서 인풋. 어차피 목적은 최대화
# for i in range(1, len(s)):
#     # 어차피 0은 이미 result 자리에 들어가 있다
#     num = int(s[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)

