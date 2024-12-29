import random
print('end svar')
print('1=a')
print('2=aa')
print('3=i')
print('4=ee')
print('5=u')
print('6=ri')
end_svar=int(input('Ant svar:'))
print('1=pooling')
print('2=strilinga')
print('3=napunsak linga')
linga=int(input('Linga:'))
if end_svar==1 and linga==1:
    list_a = ['rama', 'deva', 'soma', 'purusha', 'varna', 'hasta', 'krishna', 'kar', 'shabd', 'manushya', 'pad',
              'danta', 'karna', 'jana']
    list_a1 = ['h:11', 'm:21', 'en:31', 'ay:41', 'at:51', 'sya:61', 'e:71']
    visheshan = ['sveta', 'peeta', 'subhra', 'vachal', 'valishth', 'vishal', 'naveen', 'vigya', 'krishna', 'harit',
                 'andh', 'dheer', 'shobhan', 'kripan', 'hasva', 'rakta', 'neel', 'purana', 'komal', 'vadhir', 'deergh',
                 'udar', 'dhnadhya', 'moodh', 'udar']
    # Add more kriya lists if needed

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
        word_b = random.choice(visheshan)
        new_word2 = word_b + word_a1
        print("New word:", new_word)
        print('new visheshan vishesya:',new_word2,new_word)
elif end_svar==1 and linga==3:
    list_a = ['pustaka','nayana','netra','udara','nakha','lalata','vastra','bhooshan','nagara','patra','vana','patra','jal','salil','ambara','kamal','pushpa','phala','pustaka','dvara','griha']
    list_a1 = ['m:11', 'm:21', 'en:31', 'ay:41', 'at:51', 'sya:61', 'e:71']
    visheshan = ['sveta', 'peeta', 'subhra', 'vachal', 'valishth', 'vishal', 'naveen', 'vigya', 'krishna', 'harit',
                 'andh', 'dheer', 'shobhan', 'kripan', 'hasva', 'rakta', 'neel', 'purana', 'komal', 'vadhir', 'deergh',
                 'udar', 'dhnadhya', 'moodh', 'udar']

    # Select random items from the lists
    # word_a = random.choice(list_a)
    # word_a1 = random.choice(list_a1)

    # Concatenate the words
    # new_word = word_a + word_a1

    # print("New word:", new_word)
    num_words = 15  # Number of new words to create

    for _ in range(num_words):
        word_a = random.choice(list_a)
        word_a1 = random.choice(list_a1)
        new_word = word_a + word_a1

        print("New word:", new_word)
        word_b = random.choice(visheshan)
        new_word2 = word_b + word_a1
        print("New word:", new_word)
        print('new visheshan vishesya:', new_word2, new_word)






