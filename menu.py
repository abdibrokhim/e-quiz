import quiz
import user


class Menu:
    def main_menu(self):
        while True:
            print('\nCHOOSE AN OPTION\n')
            print('[1] -> CONTINUE')
            print('[0] -> EXIT')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                user.User().main_menu()
            elif choice == 0:
                exit()
            else:
                print("\nINVALID")

    def secondary_menu(self):
        while True:
            print('\nCHOOSE AN OPTION\n')
            print('[1] -> TAKE A QUIZ')
            print('[2] -> GET RESULTS')
            print('[0] -> BACK')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                quiz.Quiz().take_quiz()
            if choice == 2:
                quiz.Quiz().get_result()
            elif choice == 0:
                return False
            else:
                print("\nINVALID")