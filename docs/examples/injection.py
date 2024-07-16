# Unsicheres Beispiel
# Umwandlung eines Strings in Quellcode
eval(user_input)

# SQL-Injection
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
cursor.execute(query)


# Besser: Verwendung von Prepared Statements
# Umwandlung eines Strings in Quellcode
result = ast.literal_eval(user_input)

# SQL-Injection
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (user_input,))