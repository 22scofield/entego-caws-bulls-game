import random

#Hlavní funkce, která řídí běh hry
def main():
    start_game()
    gen_secret_num()
    #Počet pokusů uživatele
    max_user_attempts = 10
    play_game(sec_num, max_user_attempts)

#Dialog s uživatelem o tom, zda chce začít hru, nebo ne
def start_game():
    while True:
        user_start = input("You wanna start the game? Press 'y' for start, or 'q' to end the program: ").lower()
        if user_start == "y":
            print('I am thinking of a number. What number is it?')
            break
        elif user_start == "q":
            print("You don't want play games anymore :(. If you change your mind, run program again.")
            exit()
            break
        else:
            continue

#Vygenerování a uchování tajného čísla
def gen_secret_num():
    global sec_num
    sec_num = []
    for num in range(4):
        n = random.randrange(0,9)
        sec_num.append(n)
    if len(sec_num) > len(set(sec_num)):
        sec_num.clear()
        gen_secret_num()
    return sec_num

#Funkce, která přijme vstup uživatele a validnost daného vstupu
def user_guess_val():
    global user_input
    user_input = input("Please guess your number: ")
    #Ochrana proti nesvéprávným jedincům :)
    spam_protection = 0
    while user_input.isdigit() == False or len(user_input) != 4:
        user_input = input("Input must be a number between 1000-9999. Please try again: ")
        spam_protection += 1
        if spam_protection == 5:
            print("Security warning: Program was stopped, please try it again.")
            exit()
            break
        return user_input

#Funkce, která řídí průběh hry
def play_game(sec_num, max_user_attempts):
    while max_user_attempts > 0:
        user_guess_val()
        cow = 0
        bull = 0
        user_num_list = []
        #Vytvoření listu čísel ze vstupu uživatele
        for user_num in user_input:
            user_num_list.append(int(user_num))
        print(f'Your input is: {user_num_list}.')
        #Počítání úspěšnosti vstupu uživatele - validnost čísla
        for x in range(4):
            for y in range(4):
                if user_num_list[x] == sec_num[y]:
                    cow += 1
        # Počítání úspěšnosti vstupu uživatele - validnost čísla a pozice
        for z in range(4):
            if user_num_list[z] == sec_num[z]:
                    bull += 1
        #Určení výhry a ukončení smyčky
        if bull > 3 and max_user_attempts > 0:
            print(f'You win the game. The secret number was: {sec_num}. Remaining attempts: {max_user_attempts}.')
            max_user_attempts = 0
        else:
            print(f'Cows: {cow}.')
            print(f'Bulls: {bull}.')
            max_user_attempts -= 1
            print(f'Remaining attempts: {max_user_attempts}.')
            #Ukončení programu po vyčeprání všech pokusů.
            if max_user_attempts == 0:
                print(f'You lose. You have no remaining attempts. The secret number was: {sec_num}.')

main()