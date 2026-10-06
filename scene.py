import secrets

bruh = secrets.token_hex(10000)

print(bruh)
# u forgot the 1000s of errors that will occur when you run this code. Generating a token of 100 million bytes will likely cause memory issues and is not practical.