def emoji_coverter(message):
    words = message.split(' ')
    emojis = {
    ":)": "😊",
    ":": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
return  output


message = input(">" )
emoli_converer(message)
print(output)
     