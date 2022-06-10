import connections
import table


class User:
    Session = connections.get_session()
    session = Session()
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
        # nickname = str(input("INPUT YOUR NICKNAME: ").upper())
        # password = str(input("INPUT YOUR PASSWORD: "))

        # user = self.session.query(User).filter_by(nickname, password).all()
        # if user:
        #     menu.Menu().secondary_menu()
        #     self.end = False
        # else:
        #     print('\nINVALID NICKNAME OR PASSWORD\n')
        # if not self.end:
        #     print("\nSIGN UP FIRSTLY\n")

        for u in self.session.query(User).order_by(table.User.ID)[:3]:
            print(u)

    def sign_up(self):
        fullname = str(input("INPUT YOUR FULLNAME: ").upper())
        nickname = str(input("INPUT YOUR NICKNAME: ").upper())
        password = str(input("INPUT YOUR PASSWORD: "))
        occupation = str(input("INPUT YOUR OCCUPATION: ").upper())
        point = 0

        # self.session.add(table.User(f'{fullname}, {nickname}, {password}, {occupation}'))
        self.session.add(table.User(fullname, nickname, password, occupation, point))

        self.session.commit()

        print("\nNOW YOU CAN SIGN IN\n")
