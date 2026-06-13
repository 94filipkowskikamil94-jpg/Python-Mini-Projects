import random
from english_words import get_english_words_set

# === 1. PRZYGOTOWANIE BAZY DANYCH ===
# Pobieramy zestaw angielskich słów i zamieniamy go w listę, z której będziemy losować
word_database = list(get_english_words_set(['web2'], lower=True))

gussed_letter = []

print("Welcome to the game !")
print("How do you want level")

# === 2. MENU WYBORU POZIOMU I LOSOWANIA HASŁA ===
while True:
    choice_level = input("Easy, Medium, Hard: ")

    if choice_level == "Easy" or choice_level == "1":
        print("okey, you have 5 lives")
        life = 5
        
        # Pętla losująca słowo o długości 3 liter
        while True:
            wylosowane = random.choice(word_database)
            if len(wylosowane) == 3:
                password = wylosowane
                break # Kończy losowanie słowa
        break # Kończy działanie menu i przechodzi do gry

    elif choice_level == "Medium" or choice_level == "2":
        print("okey, you have 4 lives")
        life = 4
        
        # Pętla losująca słowo o długości 4 liter
        while True:
            wylosowane = random.choice(word_database)
            if len(wylosowane) == 4:
                password = wylosowane
                break
        break

    elif choice_level == "Hard" or choice_level == "3":
        print("okey, you have 3 lives")
        life = 3
        
        # Pętla losująca słowo o długości 5 liter
        while True:
            wylosowane = random.choice(word_database)
            if len(wylosowane) == 5:
                password = wylosowane
                break
        break

    else:
        print("Can you choice once again ?")


# === 3. GŁÓWNA PĘTLA GRY (WISIELEC) ===
while True:
    user_won = True 
    letter = input("Guess a letter: ")
    gussed_letter.append(letter)
    
    for char in password:
        if char in gussed_letter:
            print(char)
        else:
            user_won = False
            print("_")
            
    if user_won == True:
        print("Congratulations ! You won the game !")
        break    
        
    if letter in password:
        print("Bravo! Good job")
    else:
        print("Unfortunately, it didn't work out")
        life = (life - 1)
        print(f"You have {life} lives left")
        
    if life == 0:
        print("Game over")
        print(f"The password was: {password}") # Dodatek, żebyś wiedział co przegrałeś!
        break