import random
import string 


def menu():
    print("Benvenuti al generatore di password!!!")


def main():

    while True:
        
        try:
            scelta = int(input("Vuoi creare una nuova password?\n Yes => 1\n No => 2\n Scegli => "))
            print("----------------")

        except ValueError:
            print("Devi scegliere un numero tra 1 e 2!")
            continue


        if scelta == 1:
            password = stringa_random()
            print(f"La tua nuova password è: {password}")
            break 
            
        elif scelta == 2:
            print("Grazie per averci scelto!")
            break



def stringa_random(lunghezza=10):

    caratteri = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))




def run():
    menu()
    main()


if __name__ == '__main__':
    run()
