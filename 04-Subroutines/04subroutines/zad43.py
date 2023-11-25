def f(text):
    words=text.split()
    acronym=''.join(word[0].upper() for word in words)
    return acronym
text='Mam juz dosc'
print(f(text))