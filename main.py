from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    profile_name = None
    error_message = None

    if request.method == 'POST':
        access_token = request.form['access_token']
        profile_name, error_message = check_token(access_token)

    return render_template('index.html', profile_name=profile_name, error_message=error_message)


def check_token(token):
    # Placeholder: yaahan aapko API endpoint use karne hain
    # Is example mein hum log yeh maan rahe hain ki agar token 'valid' hai toh
    if token == "valid_token":  # Replace this with actual validation logic
        return "Your Profile Name", None
    else:
        return None, "Invalid or expired token"


if __name__ == "__main__":
    app.run(debug=True)
