sentence = input("Enter a sentence: ")

words = sentence.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency:")

for word, count in word_count.items():
    print(word, ":", count)

OUTPUT:
Enter a sentence: I don't know who i am

Word Frequency:
i : 2
don't : 1
know : 1
who : 1
am : 1


Enter a sentence: Every single day the weather is so hot and humid but today's weather is absolutely perfect !

Word Frequency:
every : 1
single : 1
day : 1
the : 1
weather : 2
is : 2
so : 1
hot : 1
and : 1
humid : 1
but : 1
today's : 1
absolutely : 1
perfect : 1
! : 1
