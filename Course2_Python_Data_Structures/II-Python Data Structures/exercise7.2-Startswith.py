# Use the file name mbox-short.txt as the file name
fname=input("enter a file name:")
fhand=open(fname,"r")
count=0
total=0
for line in fhand :
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    val=float(line[20:])
    total=val+total
    count=count+1
    
avg= total/count
print("Average spam confidence:",avg)
        
       
        
 