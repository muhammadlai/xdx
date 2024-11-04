from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error_message = None

    if request.method == 'POST':
        access_tokens = request.form['access_tokens']
        token_list = [token.strip() for token in access_tokens.split(',')]
        
        # Check each token
        for token in token_list:
            profile_name, error = check_token(token)
            if error:
                results.append(f"Token: {token} - Error: {error}")
            else:
                results.append(f"Token: {token} - Profile Name: {profile_name}")

    return render_template('index.html', results=results, error_message=error_message)


def check_token(token):
    # Placeholder: yahan aapko actual validation logic insert karna hoga
    # Example logic; Replace this with actual API call or validation
    if token == "valid_token":  # Replace this with actual validation logic
        return "Your Profile Name", None
    else:
        return None, "Invalid or expired token"


if __name__ == "__main__":
    app.run(debug=True)
