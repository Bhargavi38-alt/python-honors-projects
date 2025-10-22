#Dictionaries,counting max number of email sender
fname=input("Enter file:")
fh=open(fname)
counts=dict()
for line in fh :
    if line.startswith("From "):
        line=line.rstrip()
        words=line.split()
        email=words[1]
        counts[email]=counts.get(email,0)+1
       
largest=None
hsent=None
for email, freq in counts.items() :
    if largest is None or freq >largest :
        largest=freq
        hsent=email
print(hsent,largest)