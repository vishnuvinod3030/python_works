source_word="chicken"

target_word="hen"
is_kangaroo_word=True
source_word_list=[]

for ch in source_word:
    source_word_list.append(ch)

for ch in target_word:
    char_count=source_word_list.count(ch)

    if char_count>0:
        source_word_list.remove(ch)

    else:
        is_kangaroo_word=False
    break
print(is_kangaroo_word)

