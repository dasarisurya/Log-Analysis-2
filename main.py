#!/usr/bin/env python2

# importing the time library
import time

# importing Postgresql library
import psycopg2


class Suzuki:
    '''
    class Suzuki executes the below queries by defining functions
    '''

    def __init__(monami):

        # connecting to the database
        try:
            monami.database = psycopg2.connect('dbname=news')
            monami.cursor = monami.database.cursor()
        except psycopg2.DatabaseError as e:
            print e

    def report_query(monami, query):

        monami.cursor.execute(query)
        return monami.cursor.fetchall()

    def report(monami, pro, query, data='views'):

        query = query.replace('\n', ' ')
        routcome = monami.report_query(query)
        print pro
        for w in range(len(routcome)):
            print '\n', '\t', '->', routcome[w][0], '--', routcome[w][1], data
        print '\n'

    def exit(monami):

        # Database connection is closed
        monami.database.close()


# PSQL Query to display the top three articles

capeta_1 = '    ** Most popular top 3 articles of all time ** '
minamoto_articles = (
    "SELECT articles.title, count(*) as popular "
    "FROM articles inner join log on log.path "
    "LIKE CONCAT('%', articles.slug, '%') "
    "WHERE log.status like '%200%' group by "
    "articles.title, log.path ORDER BY popular DESC LIMIT 3")

# PSQL Query to display the top authors

capeta_2 = '   ** Most popular authors of all time ** '
minamoto_authors = """
SELECT authors.name, count(*) AS views
            FROM articles, authors, log
            WHERE log.status='200 OK'
            AND authors.id = articles.author
            AND articles.slug = substring(log.path, 10)
            GROUP BY authors.name
            ORDER BY views DESC;

"""

# Query to display the day Variable1s which lead to errors more than 1%

capeta_3 = '    ** Days which lead to errors more than 1% ** '
minamoto_errors = """
SELECT * FROM(
    SELECT a.e1,
    round(cast((100*c.errors) as numeric) / cast(a.errors as numeric), 2)
    AS errp FROM
        (SELECT date(time) AS e1, count(*) AS errors FROM log GROUP BY e1) AS a
        INNER JOIN
        (select date(time) as e1, count(*) as errors FROM log WHERE STATUS
        NOT LIKE '200 OK' group by e1) AS c
    ON a.e1 = c.e1)
AS t WHERE errp > 1.0;
"""

if __name__ == '__main__':
    Variable1 = Suzuki()
    Variable1.report(capeta_1, minamoto_articles)
    Variable1.report(capeta_2, minamoto_authors)
    Variable1.report(capeta_3, minamoto_errors, '% error')
    Variable1.exit()
