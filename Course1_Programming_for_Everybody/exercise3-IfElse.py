print("compute pay-if")
hrs = input("Enter hours:")
rate = input("Enter rate per hour:")
h = float(hrs)
r = float(rate)
if h>40 :
    pay=40*r
    epay=(h-40)*r*1.5
    Total=pay+epay
    print("Pay :",Total)
else :
    pay=h*r
    print("Pay:",pay)
print("All Done")