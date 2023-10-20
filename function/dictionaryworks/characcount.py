text="ABBCAABBDEF"

WC={}

for ch in text:
    if ch not in WC:
        WC[ch]=1
    else:
        WC[ch]+=1
print(WC)


#non repeating characters


for k,v in WC.items():
    if v==1:
        print(k)
        