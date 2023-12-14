def f(first_letter,last_letter):
    with open('data.txt','r', encoding='UTF-8') as file:
        data=file.read().split()
        counter=0
        for word in data:
            if word.startswith(first_letter) and word.endswith(last_letter):
                counter+=1
    return counter

print(f("w","d"))           


