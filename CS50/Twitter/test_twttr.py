from twttr import shorten

def test_res():
    assert shorten("Twitter") =="Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert  shorten("CS50") =="CS50"


