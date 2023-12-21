# this is done using dictionaries
message = input">"
words = message.split('')
emojis = {
":)": "#emojihere"
  
}
output=""
for words in words:
output +=  emojis.get(words ,word) + ""
  
