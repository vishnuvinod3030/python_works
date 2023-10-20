def capitalize (fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper

@capitalize
def morng_greetings():
    return "good morning"
# ++++++
@capitalize
def afternoon_greeting():
    return "good afternoon"

print(morng_greetings())
print(afternoon_greeting())


from datetime import datetime

current_time=datetime.now()
current_hour=current_time.hour

print(current_hour)
@capitalize
def greeting_bytime():
    current_time=datetime.now()
    current_hour=current_time.hour
    if (5<=current_hour<12):
        return"good morning"
    elif (12<=current_hour<18):
        return"good afternoon"
    else:
        return"good evening"

print(greeting_bytime())
