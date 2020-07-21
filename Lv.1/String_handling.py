def solution(s):
    cnt=0
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            cnt+=1
    if len(s)==4:
        if cnt==4:
            return True
        else:
            return False
    else:
        if cnt==6:
            return True
        else:
            return False

a="a234"
print(solution(a))