# Import tiktoken module
import tiktoken

# Prompt the user for the path and file name of the input text file
path = input("Enter the path and file name of the input text file: ")

# Open the text file and read its contents
with open(path, "r") as f:
    text = f.read()

# Get the encoding object for cl100k_base
enc = tiktoken.get_encoding("cl100k_base")

# Encode the text using tiktoken and get the number of tokens
tokens = enc.encode(text)
count = len(tokens)

# Display the token count to the user
print(f"The input text file has {count} tokens.")