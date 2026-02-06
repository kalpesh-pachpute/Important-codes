def first_non_repeating(s):
    s = s.lower()
    character = {}
    for ch in s:
        if ch in character:
            character[ch] = character[ch]+1
        else:
            character[ch] = 1

    for ch in s:
        if character[ch] == 1:
            return ch
    return -1 