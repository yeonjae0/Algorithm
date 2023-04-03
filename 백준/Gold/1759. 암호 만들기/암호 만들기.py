# 1759 백준 암호만들기

def combi(n, r):  # n개에서 r개를 고르는 조합
    if r == 0:
        # comb_lst.append(comb[:])  # !! comb_lst.append(comb) 그냥 이렇게만 쓸 경우 마지막 주소값만 복사됨. !!
        check(comb[:])
    elif n < r:
        return
    else:
        comb[r-1] = alpha[n-1]
        combi(n-1, r-1)
        combi(n-1, r)


def check(lst):
    cnt = 0
    for j in lst:
        if j in vowel:
            cnt += 1
    if 1 <= cnt < L-1:
        # 여기를 lstt = sorted(lst)로 바꿀 경우 위 함수에서 comb[:] 슬라이싱 필요없음
        lst.sort()
        tmp = ''.join(lst)
        ans.append(tmp)


L, C = map(int, input().split())
alpha = list(map(str, input().split()))
vowel = ['a', 'e', 'i', 'o', 'u']
comb = [0] * L
ans = []
combi(len(alpha), L)
ans.sort()
for i in ans:
    print(i)

'''
.sort() -> 리스트의 주소를 직접 참조해서 그 주소에 있는 요소를 정렬
sorted() -> 괄호 안에 있는 인자를 정렬해서 새로운 객체를 반환
.sort()는 리스트만 되는데 sorted는 다른것도 됨
'''

