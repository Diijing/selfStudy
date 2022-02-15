# 5번 볼링공 고르기
# 볼링공의 개수는 n, 볼링공의 무게 종류의 수는 m으로 구분
# 1부터 m까지의 자연수 형태로 존재한다
# 서로 무게가 다른 볼링공을 골라야 한다
# 무게가 같아도 인덱스가 다르면 서로 다른 볼링공으로 간주

# 인덱스와 무게를 같이 활용해야 하기 때문에 enumerate함수를 쓰면
# 간단하다고 생각이 들어 바로 시도해봄
# 문제에서 아주 힌트까지 줘서 튜플 형태로 또 다른 리스트를 만들기로 함

# 근데 막상 코드를 써 보니까 차라리 len 함수를 통해서 직접 리스트 접근하는
# 방식이 나을 듯하여 바로 선회(9분)

# n, m = map(int, input().split())
# k = list(map(int, input().split()))
# count = 0
#
# for i in range(len(k)):
#     for j in range(len(k)):
#         a = k[i]
#         if a != k[j]:
#             b = k[j]
#             count += 1
# print(int(count/2))

# 위 코드는 중복 조합의 문제를 해결하기 위한 해법
# 솔직히 이 코드에서 2로 나누기만 해 준다면 중복 조합의 문제는 해결되지만,
# 문제가 요구하는 바는 그것보다 더 근본적인 거라고 생각했음 그래서 다시
# 도전(21분)


# n, m = map(int, input().split())
# k = list(map(int, input().split()))
# pairs = []
#
# for i in range(len(k)):
#     for j in range(len(k)):
#         a = k[i]
#         if a != k[j]:
#             b = k[j]
#             pairs.append([a, b])
# for k in pairs:
#     k.sort()
# pairs = set(pairs)
# print(len(pairs))
# 시간 얼마 안남아서 그냥 2 나누기로 품(28분)

# 6번 무지의 먹방 라이브
# n개의 음식, 번호 부착, 1번부터 음식 먹기
# 마지막 음식 섭취 후 다시 1번부터 앞으로 옴
# 1초 동안 음식을 섭취 후 남은 음식을 넘기고 다음으로 섭취할 음식을 먹음
# 걸리는 시간 x
# 쉽게 말해서 k초 후에 멈추면 다시 먹어야 할 음식의 번호를 고르면 된다.
# k번 먹는다고 생각하면 간단할 듯

def solution(food_times, k):
    second = 0
    flag = True
    while flag:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            else:
                food_times[i] -= 1
                second += 1
                if second == k:
                    answer = i + 1
                    if answer == len(food_times):
                        answer = 1
                    else:
                        answer += 1
                    flag = False
                    break
    return answer


ans = solution([1, 1, 1, 1, 1, 1], 5)
print(ans)
# 시간 딱 맞춰서 풀었는데 디버깅 활용. 디버깅이 문제가 아니라
# 와일문 루프 빠져나가게 하는 데 있어서 능숙하지 못했다.
# 아직 완전하지 않고 좀 더 부족한 건
# 엄밀하게 생각하는 것. 치밀함이 부족하다.
# 루프문을 쓴다면 어디에서 종료를 할 것인지에 대해서 확실히 생각해 놓아야 한다.