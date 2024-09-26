from flask import Flask, render_template, request, jsonify
from email_functions import generate_email, change_tone  # Import your email functions

app = Flask(__name__)

@app.route('/')
def index():
    # This renders the HTML file for the UI
    return render_template('index.html')

@app.route('/generate_email', methods=['POST'])
def generate_email_route():
    prompt = request.form['prompt']  # Get email prompt from the form
    email = generate_email(prompt)   # Call your logic function
    return jsonify({'email': email}) # Return the generated email as JSON

@app.route('/change_tone', methods=['POST'])
def change_tone_route():
    email_body = request.form['email_body']
    print(email_body)
    tone = request.form['tone']
    new_email = change_tone(tone, email_body)  # Call your logic function
    return jsonify({'new_email': new_email})   # Return the updated email as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
