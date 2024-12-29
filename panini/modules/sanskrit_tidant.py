import random

print('lakaar')
print('1=lat')

lakar=int(input('lakar(1 to 11):'))

pad=int(input('1=parasmaipad,2=atmanaipad:'))
if lakar==1 and pad==1:
    list_a = ['path', 'as', 'aagachchh', 'bhav', 'pata']
    list_a1 = ['ti:11', 'si:21', 'ami:31']

    # Select random items from the lists
    #word_a = random.choice(list_a)
    #word_a1 = random.choice(list_a1)

    # Concatenate the words
    #new_word = word_a + word_a1

    #print("New word:", new_word)
    num_words = 15  # Number of new words to create

    for _ in range(num_words):
        word_a = random.choice(list_a)
        word_a1 = random.choice(list_a1)
        new_word = word_a + word_a1
        print("New word:", new_word)






