largest=None
smallest=None
while True :
    num = input("Enter a number")
    if num == 'done' :
        break
    else :
        try :
            fnum=int(num)
        except:
            print('Invalid input')
            continue
    if largest is None :
        largest=fnum
    elif largest<fnum :
        largest=fnum
        
    elif smallest is None :
        smallest = fnum
    elif fnum < smallest :
        smallest=fnum
    elif fnum > smallest :
        continue
         
print('Maximum is',largest)
print("Minimum is", smallest)
