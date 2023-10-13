message = input("> ")

words = message.split(" ")
emojis = {
    ":)": "😄",
    ":(": "😞"
}
output = ""
# for word in words:
#     if word == ":)":
#         output += emojis.get(word) + " "
#     elif word == ":(":
#         output += emojis.get(word) + " "
#     else:
#         output += word + " "

for word in words:
    output += emojis.get(word, word) + " "
print(output)