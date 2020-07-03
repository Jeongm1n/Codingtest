import math
def solution(n):
    answer = 0
    length = str(n)
    arr = []
    size_ = len(length)-1
    for i in range(len(length)):
        size=math.pow(10,size_)
        arr.append(int(n/size))
        n=n-(arr[i]*size)
        size_ -= 1
    arr.sort(reverse=True)
    size_ = len(length)-1
    for i in range(len(length)):
        size=math.pow(10,size_)
        answer+=arr[i]*size
        size_-=1
    return answer

