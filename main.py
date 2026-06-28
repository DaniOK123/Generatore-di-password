import random

password = ********

def menu():
    print("Benvenuti al generatore di password!!!")


def main():

    while True:
        
        try:
            scelta = int(input("Vuoi creare una nuova password?\n Yes => 1\n No => 2"))

        except ValueError:
            print("Devi scegliere un numero tra 1 e 2!")



def cambio():
    pass




def run():
    menu()
    main()


if __name__ == '__main__':
    run()
