def vowels_count(sentence):

    count= 0
    vowels= ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']

    for character in sentence:
    
        if character in vowels:
            count= count+1

    return count

print (vowels_count(input(str('write your sentence:'))))
    

