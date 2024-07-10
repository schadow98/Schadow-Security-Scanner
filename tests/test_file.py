
import ast
import os

class inClass:
    def __init__(self):
        eval("1+1")

def inFunction():
    eval("1+1")



eval("1+1")
ast.literal_eval("1+1")
username  = "Malte"
password  = "TEST"
cmd = "SELECT * FROM Users WHERE Username = '" + username + "' AND Password = '"+ password + "'"

secret = os.getenv("secret")
secret = "MySecret"
my_secret = "MySecret"
private_key = "-----BEGIN RSA PRIVATE KEY----- GAHSDUZASGDIUZGASIUTDGAIUSZGDIUZSGADIUZGASIUDZGASIUZGDIUZGSDIUZGSIUAZGSDIUZG -----END RSA PRIVATE KEY-----"
api_key = "1234567890abcdef1234567890abcdef"


app = object()

@app.route('/')
def index(request):
    name = request.args.get('name', '')
    # Unsichere Einbettung der Benutzereingabe in die HTML-Ausgabe
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)