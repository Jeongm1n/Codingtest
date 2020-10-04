def solution(new_id):
    str = new_id.lower()
    str = list(str)
    string = []
    for i in range(len(str)):
        if (str[i]>='a' and str[i]<='z') or (str[i]>='0' and str[i]<='9') or str[i]=='-' or str[i]=='_' or str[i]=='.':
            string.append(str[i])
    i=0
    while i<len(string)-1:
        if string[i]=='.' and string[i+1]=='.':
            del string[i]
            i=0
            continue
        i+=1

    if len(string)!=1:        
        if string[0]=='.':
            del string[0]
        length = len(string)-1
        if string[length]=='.':
            del string[length]
    elif len(string)==1 and string[0]=='.':
        del string[0]
    
    if len(string)==0:
        string.append('a')
    
        
    if len(string)<=15:
        if len(string)<=2:
            while len(string)<=2:
                string.append(string[len(string)-1])
            return "".join(string)
            
        else:
            return "".join(string)
    
    new_string = []
    if len(string)>=16:
        if len(string)>=16:
            for i in range(15):
                new_string.append(string[i])
    
        length = len(new_string)-1
        if new_string[length]=='.':
            del new_string[length]
        
    return "".join(new_string)

new_id = "..."
print(solution(new_id))
