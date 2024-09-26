from openai import OpenAI
client = OpenAI(api_key='')


def generate_email(prompt):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": f"You are an email specialist. Create a perfect email based on: {prompt}"}]
    )
    email = response.choices[0].message.content
    return email

def change_tone(tone, email_body):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": f"Make this email more {tone}: {email_body}"}]
    )
    new_email = response.choices[0].message.content
    return new_email
