
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
public_key = "-----BEGIN (EC|RSA|DSA|PGP|OPENSSH) PRIVATE KEY----- GAHSDUZASGDIUZGASIUTDGAIUSZGDIUZSGADIUZGASIUDZGASIUZGDIUZGSDIUZGSIUAZGSDIUZG -----END (EC|RSA|DSA|PGP|OPENSSH) PRIVATE KEY-----"
api_key = "1234567890abcdef1234567890abcdef"