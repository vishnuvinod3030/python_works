



f_news=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\fileoperation\\latestnews.txt")
f_stop=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\fileoperation\\stopwords.txt")
f_write=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\fileoperation\\stwords.txt","w")

news_words=set()

stop_words={line.rstrip("\n") for line in f_stop}


for line in f_news:
    words=line.split()
    for w in words:
        news_words.add(w)

diff=news_words.difference(stop_words)
# print(diff)
for i in diff:
    f_write.write(i+"\n")

