#file name readn print itin upper case
fname=input("enter a file name:")
fh=open(fname)
for lx in fh :
    ly=lx.rstrip()
    print(ly.upper())
    