text="ABCDABB"

wc={}
for ch  in text:
    if ch not in wc:
        wc[ch]=1
    else:
        print(ch,"is first recursivecharacter")
        break
    
