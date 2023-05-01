N,K = map(int,input().split())
# 맨 처음에 원에 앉아있는 사람들
arr = [i for i in range(1,N+1)]    

# 배열에서 제거된 사람들을 저장할 새로운 배열
result = []   
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1
    # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
    if num >= len(arr):   
        num = num%len(arr)
 
    result.append(str(arr.pop(num)))
print("<",", ".join(result)[:],">", sep='')