from  re import *
#               101112
text="abcabABC K@&9eys"
#     0123456789
# pattern="[a-d]"
# pattern="[A-Z]"
# pattern="[0-9]"
# pattern="[a-zA-Z0-9]"#MATCH ALL ALPHANUMERIC CHARACTERS
# pattern="[^a-z]"#exclude all lower case alpha
# pattern="[^a-zA-Z]"# exclude all alphabets
# pattern="[^a-zA-Z0-9]" # matches for special characters
#predefined characters
# pattern="\d" #[0-9]
# pattern="\D" #[^0-9]
# pattern="\w" #[a-zA-Z0-9]alphanumeric characters 
pattern="\W" #[^a-zA-Z0-9]
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())