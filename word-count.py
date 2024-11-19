sentence= input("write and check how many words:")
sentence= str(sentence)
word_count= 0

for character in sentence :
    if character ==' ':
        word_count= word_count+1

word_count= word_count+1

print(word_count)