string = input()
count = 1
for i in range(len(string)):
    if string[i] == ' ':
        count += 1

if string[0] == ' ':
    count -= 1
if string[len(string)-1] == ' ':
    count -= 1
print(count)