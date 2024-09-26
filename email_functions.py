from openai import OpenAI
client = OpenAI(api_key='')

def generate_email(prompt, body):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages = [
            {"role":"user","content":f"You are an email specialist. A person wants a perfect email and this is what they want: {prompt} Maximum number of lines is 10."}
        ]
    )
    email = response.choices[0].message.content
    if len(prompt)>0:
        if len(body.get("0.0", "end")) > 0:
            body.delete("0.0", "end")
        body.insert("0.0",str(email))

def change_tone(tone,body):
    email_content = body.get("0.0","end")
    response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages = [
        {"role":"user","content":f"You are an email specialist. Make this email sound more {tone}: /n {email_content}"}
    ]
)
    new_email = response.choices[0].message.content
    if len(email_content) < 0:
        raise Exception("No body to edit")
    else:
        body.delete("0.0","end")
        body.insert("0.0",str(new_email))
