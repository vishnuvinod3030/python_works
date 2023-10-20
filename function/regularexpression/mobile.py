#rule for validating mobile number
from re import *
mob=input("enter mobile number")
# pattern="(91)?[0-9]{10}"#mobile number
# pattern="\d{3}[-]?\d{3}[-]?\d{4}" #212-212-2323
pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}\d{4}[A-Z]{1}"

matcher=fullmatch(pattern,mob)
print("invalid" if matcher == None else "valid")
