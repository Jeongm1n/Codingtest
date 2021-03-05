n, m = map(int, input().split())
people_list = list(map(int, input().split()))
people = n * m
for i in range(len(people_list)):
        print(people_list[i]-people, end = ' ')
