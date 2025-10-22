#Find function in string
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find("0")
fpos=float(text[23 : 29])
print(fpos)