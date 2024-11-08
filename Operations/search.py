from urllib.parse import urlparse

from environment import Environment

import psycopg2

class Database:

    def __init__(self):

        result = urlparse(Environment.database_url)

        username = result.username

        password = result.password

        database = result.path[1:]

        hostname = result.hostname

        port = result.port

        connection = psycopg2.connect(

            database = database,

            user = username,

            password = password,

            host = hostname,

            port = port

        )

        self.connection = connection

        self.cursor = self.connection.cursor()

 

    def query(self, query, vars=None):

        if vars is not None:

            self.cursor.execute(query, vars)

        else:

            self.cursor.execute(query)

        data = self.cursor.fetchall()

        return data

 

    def commit(self, query, vars=None):

        if vars is not None:

            self.cursor.execute(query, vars)

        else:

            self.cursor.execute(query)

            self.connection.commit()

        return self.cursor.rowcount

   

    def close(self):

        self.cursor.close()

        self.connection.close()
