import openai

# link secret to .env file
def complete(note_text):
    openai.api_key = ""
    response = openai.Completion.create(model="text-davinci-003", temperature=0.1, max_tokens=128,
                                        prompt="Correct grammar & punctuation, summarize, and extract subject, location, & time (if possible). Then, write a two word summary (subheading)"
                                               f"derived from this statement: {note_text}")
    return response['choices'][0]['text']

print(complete("yoga class downtown next tuesday"))