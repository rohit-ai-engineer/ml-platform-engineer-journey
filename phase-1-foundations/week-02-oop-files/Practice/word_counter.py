word_count = {}

user_input = input("Enter you sentence: ")
word_spilt = user_input.split()

for word in word_spilt:
    if word in word_count:
        word_count [word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print (f"{word}: {count}") 


