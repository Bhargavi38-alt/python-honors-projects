#counting hours and finding max
fname=input("Enter file:")
fh=open(fname)
counts=dict()
for line in fh :
    if line.startswith("From "):
        line=line.rstrip()
        words=line.split()
        time=words[5]
        hour=time.split(':')[0]
        counts[hour]=counts.get(hour,0)+1
for hour, freq in sorted(counts.items()) :
        print(hour,freq)