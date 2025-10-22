#compute pay using function
def computepay (h,r) :
    if h > 40 :
        reg = h*r
        otp = (h-40.0)*(r*0.5)
        p = reg+otp    
    else:
        p = h*r
    return p

hrs=input("Enter hours:")  
ra=input("Enter rate:")
h=float(hrs)
r=float(ra)
Pay=computepay(h,r)
print("Pay",Pay)
