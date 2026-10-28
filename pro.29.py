# Q29. Sentence Reversal
# Reverse the order of words in a sentence without changing the words themselves.
# Example:
# Input: Python is easy
# Output: easy is Python

sentence = input("Enter a sentence: ")

words = sentence.split()
words.reverse()

print("Output:", " ".join(words))