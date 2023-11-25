def f(sentence):
    new_sentence=''.join(sentence.split())
    return new_sentence

sentence='Jak sie masz?'
result=f(sentence)

print(result)
