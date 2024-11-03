test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Here is the test dictionary:")
print(test_dict)

word = input("Enter the word you want to check the frequency of: ")
frequency = test_dict.get(word, 0)

print("The frequency of", word, "is:", frequency)
