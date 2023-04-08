# 16 digit credit card number validation
num = ["1","2","3","4","5","6","7","8","9","0","-"]
reps = ["1111","2222","3333","4444","5555","6666","7777","8888","9999","0000"]
arr = []

def valid(word):
    cozy = True
    mozy = True
    if word[0] == "4" or word[0]=="5" or word[0]=="6":
        xx = word.split("-")
        melun = True
        for j in xx:
            if len(j) == 4 or len(j)==16:
                melun = True
            else:
                melun = False
                break
        if melun:
            word = word.replace("-","")
            if len(word) == 16:
                    for x in reps:
                        if x not in word:
                            continue
                        else:
                            cozy = False
                            break
                    for i in word:
                        if i in num:
                            continue
                        else:
                            mozy = False
                            break
                    if cozy and mozy:
                        return True
                    else:
                        return False
                    
            else:
                return False
        else:
            return False
    else:
        return False

        
a = int(input())
        
for i in range(a):
    b = input()
    arr.append(b)
    
for i in range(a):
    if valid(arr[i]):
        print("Valid")
    else:
        print("Invalid")


# valid(arr[0])
    
    
    
    
    
    
    
    
    
