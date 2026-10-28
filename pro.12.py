# Q12. Write a program to find the longest word in a given sentence.

s = input("Enter a sentence: ")

words = s.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)