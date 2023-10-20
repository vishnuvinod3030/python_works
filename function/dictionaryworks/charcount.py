words=["hello","hai","hello","hai","hai"]

wc={}#{"hello":2 ,"Hai":1}
for w in words:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)