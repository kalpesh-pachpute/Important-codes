def is_anagram(s1,s2):
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().rplace(" ","")
    return sorted(s1) == sorted(s2)
