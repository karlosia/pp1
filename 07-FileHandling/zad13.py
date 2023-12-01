movie_titles=['The Hunger Games','Harry Potter','Frozen','The Notebook','The Last Song']

file=open('movies.txt','w')

for i in movie_titles:
    file.write(i+'\n')

file.close()    