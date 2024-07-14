import re

# Unsicherer Code als String
code = '''
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_input = request.args.get('input')
    html_content = f'<div>{user_input}</div>'
    return html_content

if __name__ == '__main__':
    app.run()
'''

# Der Regex zur Erkennung von XSS-Schwachstellen
pattern = r'<.*?{.*?request\.args\.get\([\'\"].*?[\'\"]\).*?}?.*?>'

# Suche nach Matches
matches = re.findall(pattern, code, re.DOTALL)

# Ausgabe der Matches
print("Gefundene Matches:", matches)
