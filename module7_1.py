word = '<Spaghetti>'
cleaned_word = word.strip()
print(cleaned_word)


modified_string = cleaned_word.replace('<', '').replace('>', '')
print(modified_string)