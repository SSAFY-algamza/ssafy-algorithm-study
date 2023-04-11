def solution(s):
    answer = 1

    for i in range(1,len(s)-1):
        j = 0
        while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
            j += 1
        answer = max(answer, (j-1)*2+1)
        if s[i] == s[i+1]:
            j = 0
            while i-j >= 0 and i+1+j < len(s) and s[i-j] == s[i+j+1]:
                j += 1
            answer = max(answer, (j-1)*2+2)
    return answer