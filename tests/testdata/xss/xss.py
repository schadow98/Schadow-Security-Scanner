from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  user_input = request.args.get('input')
  # Unsanitized user input used in HTML
  html_content = f"<div>" + user_input + "</div>"
  return html_content

if __name__ == '__main__':
  app.run(debug=True)
