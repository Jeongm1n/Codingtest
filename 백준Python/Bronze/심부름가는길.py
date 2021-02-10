a = int(input())
b = int(input())
c = int(input())
d = int(input())
minutes = (a+b+c+d)//60
seconds = (a+b+c+d)%60
print(str(minutes) + '\n' + str(seconds))