# this is done using dictionaries
message = input">"
words = message.split('')
emojis = {
":)": "😊"
}
output=""
for words in words:
output +=  emojis.get(words ,word) + ""
  print(output)
