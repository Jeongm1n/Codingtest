def pseudo(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def palindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            res1 = pseudo(s, left + 1, right)
            res2 = pseudo(s, left, right - 1)
            if res1 == True or res2 == True:
                return 1
            else:
                return 2
    return 0


for _ in range(int(input())):
    s = input()
    answer = palindrome(s, 0, len(s) - 1)
    print(answer)
