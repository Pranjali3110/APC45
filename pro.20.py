# Q20. Write a program to count how many times a specific word appears in a sentence.

s = input("Enter a sentence: ")
word = input("Enter word: ")

words = s.split()
count = words.count(word)

print("Word occurs", count, "times")