# text="ABACDC"
# #Print first recursive character
# lst=[] 

# for ch in text:
#     #ch=A
#     char_count=lst.count(ch)

#     if char_count==0:
#         lst.append(ch)
#     else:
#         print(f"first recursive character is {ch}")
#         break
         
    
        #  print(f" is {ch}")



text="ABACDC"
#Print scnd recursive character
lst=[] 
duplicate_lst=[]

for ch in text:
    #ch=A
    char_count=lst.count(ch)

    if char_count==0:
        lst.append(ch)
    else:
        duplicate_lst.append(ch)
        
print(f"secnd recursive character={duplicate_lst[1]}")