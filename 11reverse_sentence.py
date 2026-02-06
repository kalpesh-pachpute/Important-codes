sentence = input("Enter sentence you want to reverse ")

def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)
print(reverse_sentence(sentence))