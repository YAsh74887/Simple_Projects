to_be_replaced = "[name]"

with open("C:/Users/ASUS/Desktop/Mail Merge Project Start/Input/Names/invited_names.txt","r") as names_files:
    names = names_files.readlines()

        
with open("C:/Users/ASUS/Desktop/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r+") as letter_file:
    letter_format = letter_file.read() 
print(letter_format)

for name in names:
    stripped = name.strip()
    new = letter_format.replace(to_be_replaced, stripped)
    print (new)
    with open("C:/Users/ASUS/Desktop/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped}.txt", "w") as output:
        output.write(new)
        
        
    

      
   
        