import pandas as pd
#TODO 1. Create a dictionary in this format:

alphabets =  pd.read_csv("C:/Users/ASUS/Desktop/NATO-alphabet-start/nato_phonetic_alphabet.csv") 
print(alphabets)



new = {row.letter:row.code  for (i, row ) in alphabets.iterrows()}
# print(new)


n = ("YASH")
# l = [new[letter] for letter in n]
# print(l)

rowing = []
for letter in n:
    p = (new[letter])
    r= (str(p))
    
    rowing.append(r)

print (rowing)





# new_dict = {row.letter:row.code for (i,row) in alphabets.iterrows()}
# print(new_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# var = input().upper()

# l = [new_dict[letter] for letter in var]
# print(l)