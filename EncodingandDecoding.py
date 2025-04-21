import random
import string

# Function to generate 3 random letters
def random_letters():
    return ''.join(random.choices(string.ascii_lowercase, k=3))

# Encoding function
def encode(word):
    if len(word) >= 3:
        word = word[1:] + word[0]  # move first letter to the end
        word = random_letters() + word + random_letters()
    else:
        word = word[::-1]  # reverse the word
    return word

# Decoding function
def decode(word):
    if len(word) < 3:
        word = word[::-1]
    else:
        word = word[3:-3]  # remove 3 letters from start and end
        word = word[-1] + word[:-1]  # move last letter to the start
    return word

#program
choice = input("Do you want to encode or decode? (e/d): ")

message = input("Enter your message: ")
words = message.split()
l= []

for word in words:
    if choice == 'e':
        l.append(encode(word))
    elif choice == 'd':
        l.append(decode(word))
    else:
        print("Invalid choice")
        break

# Print the result
print("Result:", ' '.join(l))