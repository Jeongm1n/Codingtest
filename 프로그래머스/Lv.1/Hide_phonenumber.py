def solution(phone_number):    
    return '*'*(len(phone_number)-4)+phone_number[-4:]

phonenumber="01084067716"
print(solution(phonenumber))