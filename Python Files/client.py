from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)