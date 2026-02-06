# method 1
def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]


# method 2
def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == "".join(reversed(s))


# method 3
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ","")
    reversed_s = "".join(reversed(s))
    if s == reversed_s:
        return True
    else:
        return False
