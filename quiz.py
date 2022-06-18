import pandas as pd

import user


class Quiz:
    user_guess = ""
    min_query = 5
    max_query = 0

    def read_quiz_data(self):
        df = pd.read_csv('quiz.csv')
        return df

    def get_queries_amount(self):
        # while True:
        print('\nCHOOSE AN OPTION\n')
        print('[1] -> 5 QUERIES')
        print('[2] -> 10 QUERIES')
        print('[3] -> 15 QUERIES')
        print('[4] -> 20 QUERIES')
        print('\n[0] -> BACK')

        choice = input("[?] -> ")
        try:
            choice = int(choice)
        except ValueError:
            print("\nINVALID")
            # continue

        if choice == 1:
            # return min_que
            self.max_query = self.min_query
        elif choice == 2:
            # return min_que * 2
            self.max_query = self.min_query * 2
        elif choice == 3:
            # return min_que * 3
            self.max_query = self.min_query * 3
        elif choice == 4:
            # return min_que * 4
            self.max_query = self.min_query * 4
        elif choice == 0:
            return False
        else:
            print("\nINVALID")

    def take_quiz(self):
        self.get_queries_amount()
        for i in range(0, self.max_query):
            print(self.read_quiz_data().QUERY[i])
            answer = self.read_quiz_data().ANSWER[i].upper()
            self.user_guess = str(input("INPUT YOUR GUESS: ")).upper()
            if self.user_guess == answer:
                print("\nPERFECT!\n")
                user.User().update_point()
                self.get_result()
            else:
                print("\nWRONG!\n")
                self.get_result()
        self.get_result()

    def check_answer(self, i):
        # for i in range(0, self.max_query):
        answer = self.read_quiz_data().ANSWER[i]
        if answer == self.user_guess:
            return True
        else:
            return False

    def get_result(self):
        print("\nYOUR SCORE IS: {}\n".format(user.User().get_point()))
