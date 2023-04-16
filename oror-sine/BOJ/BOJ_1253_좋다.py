import sys
N = int(sys.stdin.readline())
seq = sorted([int(i) for i in sys.stdin.readline().split()])  # 오름차순 수열
idxs = {}  # 평가대상  # {숫자값: idx_list}
for idx, num in enumerate(seq):
    if num in idxs:
        idxs[num].append(idx)
        continue
    idxs[num] = [idx]

ans = 0
for i in range(N):
    for j in range(0, i):
        _sum = seq[i]+seq[j]
        if _sum > seq[-1]:  # seq is asc, therefore 이후의 j는 의미 없음 
            break
        if _sum not in idxs: # 
            continue
        # 어떤 두 수의 합과 같은 평가대상이 존재
        # 각 평가대상이 어떤 두 수와 다른 값인지 확인
        k = 0
        while k < len(idxs[_sum]):
            # 평가 대상 in 어떤 두 수, 다음 대상으로
            if idxs[_sum][k] in (i, j): 
                k += 1
                continue

            # 좋은 수로 평가됨
            ans += 1
            # 평가가 끝났으므로, 대상에서 제외
            idxs[_sum][k], idxs[_sum][-1] = idxs[_sum][-1], idxs[_sum][k]
            idxs[_sum].pop()
        
        # 어떤 값을 지니는 평가 대상이 없으면 해당 key를 삭제
        if not idxs[_sum]:
            del idxs[_sum]
    
    # 더이상 평가할 대상이 없으면 종료
    if not idxs:
        break
    
print(ans)
