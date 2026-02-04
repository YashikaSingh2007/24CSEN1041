text1= input("Enter first text: ").lower()
text2= input("Enter second text: ").lower()
words1= text1.split()
words2= text2.split()
common=0
for word in words1:
    if word in words2:
        common+=1
similarity= (common/len(words1))*100
print("similarity percentage:", round(similarity,2),"%")

if similarity>70:
    print("High plagiarism detected")
elif similarity> 40:
    print("Moderate plagiarism")
else:
    print("Low plagiarism")
