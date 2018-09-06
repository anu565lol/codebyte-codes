def LetterChanges(stri): 
    new = ""
    vl = ["a","e","i","o","u"]
    for w in stri:
        if w == " ":
            new = new
        if w.isalpha():
            if chr(ord(w)+1) in vl:
                w = chr(ord(w)+1).upper()
            else:
                w = chr(ord(w)+1)
            new = new+w
        else:
            new = new+w
    return new
print LetterChanges(raw_input())
