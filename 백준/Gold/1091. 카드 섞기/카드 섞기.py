
N = int(input())  # 카드 개수: 수열의 길이 (S, P  길이 동일)
P = list(map(int, input().split()))  # 각 카드가 어느 플레이어에게 가야하는지
S = list(map(int, input().split()))  # 카드 한 번 섞으면 i번째 카드-> S[i] 이동

order = [0, 1, 2] * (N//3)  # 원래 순서
card = [0] * N  # 섞인 카드
pre_card = P[:]
ans = 0  
# P의 숫자를 012로 만들기

while P != order:  # 일단 012012 이런순서면 바로 답

    # 카드 섞기
    for i in range(N):
        card[S[i]] = pre_card[i]
    ans += 1

    if card == P or card == pre_card:
        ans = -1
        break

    if card == order:  # 만약 card와 order 같아지면 바로 break
        break

    #  초기화 작업
    pre_card = card[:]
    card = [0] * N

print(ans)