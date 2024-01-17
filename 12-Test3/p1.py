def f(word):
    wave=[]
    i=0
    for i in range(0,len(word)):
        wave_word=word[:i].lower() +word[i].capitalize()+word[i+1:].lower()
        wave.append(wave_word)
        i+=1
    return '-'.join(wave)

print(f("book"))

