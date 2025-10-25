from groq import Groq

# Create the client instance with your free Groq API key
client = Groq(
    api_key="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"
)

# Send a chat completion request
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # free model
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is python?"}
    ]
)

# Print the assistant's response
print(completion.choices[0].message.content)

