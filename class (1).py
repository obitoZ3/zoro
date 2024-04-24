actualpassword = 4567
for i in range(3):
    currentpassword=int(input())
    if currentpassword==actualpassword:
        print("sucessfully logged in")
        break
    else:
        if attemptscount==1:
            print("your account blocked,try after 24 hours ")
        else:
            print("incorrect password,your left with",attemptscount-1,"attempts")
      attemptscount-=1
