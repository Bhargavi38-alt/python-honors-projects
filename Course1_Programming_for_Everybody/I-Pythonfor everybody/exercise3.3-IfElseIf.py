#print grades using score
score=input ("Enter your score:")
sc=float(score)
if sc<=0.6 :
    print("score grade=F")
elif sc<=0.7:
    print("score grade:D")
elif sc<=0.8:
    print("score grade:C")
elif sc<=0.9: 
    print("Score grade:B")
elif sc>=0.9:
    print("score garde:A")
else:
    print("enter valid score from 0.0 to 1.0 :")