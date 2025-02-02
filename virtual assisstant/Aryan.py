from instruction import *

def main():
    while True:
        if wake_word():
            talk("I'm listening.")
            exit_program = play_Aryan()
            if exit_program:
                break

if __name__ == '__main__':
    main()
