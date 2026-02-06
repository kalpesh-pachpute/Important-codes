text = input("Enter the text: ")
def count_character(text):
    text=text.lower()
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    for ch in text:
        if ch in 'aeiou':
            vowels += 1
        elif ch.isalpha():
            consonants += 1 
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
    return vowels, consonants, digits, spaces
v, c, d, s = count_character(text)
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", s)
