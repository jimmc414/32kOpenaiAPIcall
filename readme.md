This is a basic call to OpenAI's new GPT432k API endpoint that allows 32,000 tokens. Calls can cost a max of $2 each per 3/18/23 pricing, so be careful.  Pulls API key from env.  input.txt and output.txt for I/O

need to have your openai API in your env with (windows) 
```
setx OPENAI_API_KEY "yourkeyhere"
```
added tiktoken token counter

import tiktoken openai
