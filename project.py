# "Database code" for the DB Forum.
import time
import psycopg2
DBNAME = 'news'


def answer_one():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    """top 3 articles"""
    c.execute("""select articles.title,count(path) from articles join log
                  on articles.slug = (replace(path,'/article/',''))
                  where status = '200 OK' and path != '/'
                  group by articles.title
                  order by count desc limit 3;
                  """)
    return c.fetchall()
    db.close()

x = 1
print('Top 3 most viewed Articles!')
for i in answer_one():
    print(str(x) + ': Article: ' + i[0] + '. Views: ' + str(i[1]))
    x += 1


def answer_two():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    """top authors"""
    c.execute("""select authors.name,count(log.path)
               from authors,articles,log where authors.id = articles.author
               and articles.slug = (replace(log.path,'/article/',''))
               group by authors.name order by count(log.path) desc limit 4;
                """)
    return c.fetchall()
    db.close()

y = 1

print('\n \nMost popular Authors!')
for i in answer_two():
    print(str(y) + ': Author: ' + i[0] + '. Views: ' + str(i[1]))
    y += 1


def answer_three():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    """next question"""
    try:
        c.execute("""create view vwHitByDate as select
                     (to_char(time, 'YYYY-MM-DD')),count(status)
                     from log group by to_char;""")
        c.execute("""select vwHitByDate.to_char,vwHitByDate.count,
                     count(log.status) as errors from log join vwHitByDate on
                     (to_char(log.time, 'YYYY-MM-DD')) = to_char
                     where log.status != '200 OK' group by to_char,count
                        order by errors desc limit 1;""")
    except:
        db.rollback()
        c.execute("""select vwHitByDate.to_char,vwHitByDate.count,
                     count(log.status) as errors from log join vwHitByDate on
                     (to_char(log.time, 'YYYY-MM-DD')) = to_char
                     where log.status != '200 OK' group by to_char,count
                        order by errors desc limit 1;""")
    return c.fetchall()
    db.close()


print('\n \nDate with the failure rate!\n')
for i in answer_three():
    print ('On the date ' + i[0] +
           ' the rate of requests leading to failure was ' +
           str((i[2]/i[1])*100)[:4] + '%')
