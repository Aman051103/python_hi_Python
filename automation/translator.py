from googletrans import Translator
translator = Translator()

out = translator.translate("क्या हाल है", dest='en')
print(out)

mystory = '''well, the world that wew live in today.
is fucked up.
'''
out = translator.translate(mystory, dest='hi')
print(out.text)
