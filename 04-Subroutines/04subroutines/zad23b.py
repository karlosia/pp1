from zad23 import count_letter_occurences

text="You never get a second chance to make a first impression"
letter_to_count="e"

occurrences=count_letter_occurences(text, letter_to_count)
print(text)
print(f"The number of letter '{letter_to_count}': {occurrences}")