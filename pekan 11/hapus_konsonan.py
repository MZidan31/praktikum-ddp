consonant = ("a","i","u","e","o")

def hapusVokal(text):
    for i in consonant:
        text = text.replace(i,"")
    print(text)

hapusVokal("Nurul Fikri")