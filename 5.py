#Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). 
#That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") 
#should return the string "tothohisos isos fofunon"

def translate(s):
    r = ""
    for c in s:
        r += c
        if c in "bcdfghjklmnpqrstvwxz":
            r += 'o' + c
    return r

print(translate("this is fun"))
