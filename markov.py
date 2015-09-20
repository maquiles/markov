import random

with open('less_rubbish.txt') as f: #provide text file to parse
    text = f.read()

text = [i.lower() for i in text.split(' ') if i != ""] #create list of all words

markov = {i:[] for i in text} #create dictionary with words as keys and empty lists as values

for before, after in zip(text, text[1:]):
    markov[before].append(after)

new = markov.keys() #new dict for seed to march up with

length_sentence = random.randrange(500) #create a random length for a sentence
seed = random.randrange(len(new)) #randomly pick a starting point
sentence_data = [new[seed]] #use as first word and starting point
current_word = random.choice(markov.keys())

for i in range(0, length_sentence):
    next_index = random.randint(0, len(markov[current_word])-1) #randomly pick word from last words list
    next_word = random.choice(markov[current_word])
    sentence_data.append(next_word)
    current_word = next_word

write_markov = "markov_para.txt"
min = open("markov_para.txt", "w")
min.write(' '.join(sentence_data))
min.close()