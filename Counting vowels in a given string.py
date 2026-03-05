VOWELS = "aeiouAEIOU"

def count_vowels(input_string):
    count = 0
    for char in input_string:
        if char in VOWELS:
            count+=1
    return count
input_string= input("Enter the string:")

result= count_vowels(input_string)

print("Number of vowels in the string:", result)


OUTPUT:
Enter the string:Hello, World!
Number of vowels in the string: 3

Enter the string:Python is a great programming language
Number of vowels in the string: 12

Enter the string:APPle
Number of vowels in the string: 2

