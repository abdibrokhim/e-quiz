import requests
from bs4 import BeautifulSoup
import pandas as pd

queries_list = []
answers_list = []


def get_url_page():
    url_page = "https://www.cosmopolitan.com/uk/worklife/a32388181/best-general-knowledge-quiz-questions/"
    return url_page


def get_queries(soup):
    queries = soup.find('div', class_='article-body-content standard-body-content').find_all('li')
    j = 0
    for i in queries:
        query = i.text
        if j < 85:
            queries_list.append(query)
        else:
            answers_list.append(query)
        j += 1


def write_to_csv():
    data = {'QUERY': queries_list,
            'ANSWER': answers_list}
    df = pd.DataFrame(data)
    df.to_csv('quiz.csv', index=False)


def print_info():
    for i in zip(queries_list, answers_list):
        print("{:120s} {:50s}".format(i[0], i[1]))


def print_queries():
    for i in queries_list:
        print(i)


def print_answers():
    for i in answers_list:
        print(i)


def update_quiz_data():
    page = requests.get(get_url_page())
    soup = BeautifulSoup(page.content, 'html.parser')
    get_queries(soup)

    print_info()
    write_to_csv()
