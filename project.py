#!/usr/bin/python

import psycopg2
import sys
DBNAME = 'news'


def connect_to_db(database_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print("Unable to connect to database")
        # THEN perhaps exit the program
        sys.exit(1)  # The easier method
        # OR perhaps throw an error


def get_query_results(db, c, query):
    c.execute(query)
    results = c.fetchall()
    return results


def answer_one(db, c):
    query_str = """select articles.title,count(path) from articles join log
                   on articles.slug = (replace(path,'/article/',''))
                   where status = '200 OK' and path != '/'
                   group by articles.title
                   order by count desc limit 3;
                   """

    return get_query_results(db, c, query_str)


def answer_two(db, c):

    query_str = """select authors.name,count(log.path)
               from authors,articles,log where authors.id = articles.author
               and articles.slug = (replace(log.path,'/article/',''))
               group by authors.name order by count(log.path) desc limit 4;
                """

    return get_query_results(db, c, query_str)


def answer_three(db, c):
    query_str = """select vwHitByDate.to_char,vwHitByDate.count,
                 count(log.status) as errors from log join vwHitByDate on
                 (to_char(log.time, 'YYYY-MM-DD')) = to_char
                 where log.status != '200 OK' group by to_char,count
                 order by errors desc limit 1;"""

    return get_query_results(db, c, query_str)


def create_view(db, c):
    try:
        c.execute("""create view vwHitByDate as select
                     (to_char(time, 'YYYY-MM-DD')),count(status)
                     from log group by to_char;""")
    except Exception as e:
        print("except!")
        db.rollback()



if __name__ == '__main__':

    db, c = connect_to_db(DBNAME)
    create_view(db, c)
    # answer one
    x = 1
    print('Top 3 most viewed Articles!')
    for i in answer_one(db, c):
        print("{}: Article: {}. Views: {}".format(x, i[0], i[1]))
        # print(str(x) + ': Article: ' + i[0] + '. Views: ' + str(i[1]))
        x += 1
    # answer_two
    y = 1
    print('\n \nMost popular Authors!')
    for i in answer_two(db, c):
        print(str(y) + ': Author: ' + i[0] + '. Views: ' + str(i[1]))
        y += 1
    # answer_three
    print('\n \nDate with the failure rate!\n')
    for i in answer_three(db, c):
        print('On the date ' + i[0] +
              ' the rate of requests leading to failure was ' +
              str((i[2]/i[1])*100)[:4] + '%')
