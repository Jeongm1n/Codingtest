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
<<<<<<< HEAD:Lv.1/Reverse_number.py
    return answer
=======
    return answer
>>>>>>> 9b0a2205ad43717b743996fa1197acc172f8e902:Lv.1/Problem.1.py
