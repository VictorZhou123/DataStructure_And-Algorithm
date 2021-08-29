s = "anagram", t = "nagaram"
a = list(s)
b = list(t)
if a.sort() == b.sort():
    print(True)
else:
    print(False)
