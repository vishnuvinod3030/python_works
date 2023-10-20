text=("Your meeting has been launched Don’t see your Zoom meeting?")

words=text.casefold().split(" ")

wc={}

for w in words:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)
stop_words={"has","see","for","to"}