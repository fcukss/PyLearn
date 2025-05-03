import emoji

def get_emoji():
    emo = input("Input: ")
    print(f"Output: {emoji.emojize(emo, language='alias')}")
