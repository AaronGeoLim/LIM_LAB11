words = []
for i in range(10):
    word = input(f"Kindly enter 10 words {i+1}: ")
    words.append(word)
    
num_letters = int(input("Enter the number of letters that you want: "))

matching_words = []
for word in words:
    if len(word) == num_letters:
        matching_words.append(word)
        
if matching_words:
    print("These are the words with", num_letters, "letters:",",".join(matching_words))
else:
    print("There are no words with", num_letters, "letters.")
    