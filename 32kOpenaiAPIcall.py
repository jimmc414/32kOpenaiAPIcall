# Import the OpenAI library
import openai

# Load the API key from the environment
openai.api_key = os.environ["OPENAI_API_KEY"]

# Read the text input from input.txt
with open("input.txt", "r") as f:
    text = f.read()

# Create a chatgpt engine with GPT-4 and 32,000 tokens
engine = openai.Engine("chatgpt-gpt4-32k")

# Make an API call to generate a response
response = openai.Completion.create(
    engine=engine,
    prompt=text,
    max_tokens=32000,
    temperature=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.6,
)

# Write the response to output.txt
with open("output.txt", "w") as f:
    f.write(response["choices"][0]["text"])