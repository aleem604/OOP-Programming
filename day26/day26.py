import pandas as p


data = p.read_csv('nato_phonetic_alphabet.csv')

new_dic = {row.letter:row.code for (index, row) in data.iterrows()}

print(new_dic)