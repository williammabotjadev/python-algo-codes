input_val = "fr"

def greeting(lang):
    if lang == "en":
        return "Hello, World!"
    elif lang == "fr":
        return "Bonjour le Monde!"
    else:
        return "Language Not Supported"

res = greeting(input_val)

print(res)