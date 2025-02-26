"""
Write a function that takes an array
of words and smashes them together
into a sentence and returns the sentence.
 You can ignore any need to sanitize words
 or add punctuation, but you should add spaces
 between each word.
 Be careful, there shouldn't be a space
 at the beginning or the end of the sentence!
"""
def smash(words):
  return ' '.join(words)




words = ['hello', 'world', 'this', 'is', 'great']
print(smash(words)) # returns "hello world this is great"