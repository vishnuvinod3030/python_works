from re import *

text="abaabcaabaaaa"
#     0123456789

# pattern="a+"  # + atleast one a
# pattern="a*" # matches for any number of a
# pattern="a?" #optional
# pattern="a{2}" #2 aa 6 aa 9 aa 11 aa
pattern="a{2,3}"  #minimum 2 maximum 3
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

#+ altleast
#* any num (count edukum)
#? optional
# {1,2}lower limit,upper limi
