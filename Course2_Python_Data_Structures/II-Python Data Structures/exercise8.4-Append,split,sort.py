#splitting words
abc=input("Enter file name:")
fhand=open(abc)
st=list()
for line in fhand:
    words=line.split()
    for wrd in words :
        if wrd not in st :
            st.append(wrd)
st.sort()
print(st)

