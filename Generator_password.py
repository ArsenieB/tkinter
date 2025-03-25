import string
import random

def generate_password(length=12):
    # Defirire caractere posibile
    characters = string.ascii_letters + string.digits + string.punctuation 
    # Generajea parola
    password =''.join(random.choice(characters) for _ in range(length))
    return password
#Exemplu de utilizare  
print(generate_password())
 



 


