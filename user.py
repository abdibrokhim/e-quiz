import menu
import table


class User:
    session = table.Session()
    end = False

    def main_menu(self):
        while True:
            print('\nCONTINUE ...\n')
            print('[1] -> SIGN IN')
            print('[2] -> SIGN UP')
            print('\n[0] -> BACK\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                self.sign_in()
            elif choice == 2:
                self.sign_up()
            elif choice == 0:
                return False
            else:
                print("\nINVALID")

    def sign_in(self):
        user_nickname = str(input("INPUT YOUR NICKNAME: ").upper())
        user_password = str(input("INPUT YOUR PASSWORD: "))

        user = self.session.query(table.User).filter_by(NICKNAME=user_nickname,
                                                        PASSWORD=user_password).all()
        if user:
            menu.Menu().secondary_menu()
            self.end = True
        else:
            print('\nINVALID NICKNAME OR PASSWORD\n')
            self.end = True
        if not self.end:
            print("\nSIGN UP FIRSTLY\n")

    def sign_up(self):
        user_fullname = str(input("INPUT YOUR FULLNAME: ").upper())
        user_nickname = str(input("INPUT YOUR NICKNAME: ").upper())
        user_password = str(input("INPUT YOUR PASSWORD: "))
        user_occupation = str(input("INPUT YOUR OCCUPATION: ").upper())
        user_point = 0

        new_user = table.User(FULLNAME=user_fullname, NICKNAME=user_nickname, PASSWORD=user_password,
                              OCCUPATION=user_occupation, POINT=user_point)
        self.session.add(new_user)

        self.session.commit()

        print("\nNOW YOU CAN SIGN IN\n")
