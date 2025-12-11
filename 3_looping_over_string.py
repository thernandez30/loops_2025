# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.

word = input("Pick a word. ")
print("Your word is", word)

for x in (word):
    print(x)

# Challenge:
# Count how many vowels are in the word.
count = 0
for vowel in word.lower():
    if vowel in "aeiou":
        count += 1
print(f"There are {count} vowels in your word.")