def f(first_letter,last_letter):
    with open('data.txt','r', encoding='utf-8') as file:
        data=file.read().split()
        num_of_words=0
        for word in data:
            if word.startswith(first_letter)and word.endswith(last_letter):
                num_of_words+=1
    return num_of_words   


print(f("w","d"))
