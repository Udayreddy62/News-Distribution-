from environment import Environment

from database import Database

def create_dummy_topic_table():

    tmp = '''CREATE TABLE topics(

    news_id TEXT PRIMARY KEY,

    topic TEXT ,

    topic_score INT,

    reviewed BOOL,

    CONSTRAINT topic_ex

    FOREIGN KEY(news_id)

    REFERENCES news_data(news_id))'''

 

    database = Database()

    database.commit(tmp)

    database.close()

 

#def insert_into_dummy_topic

def insert_into_dummy_news():

    tmp = '''

    INSERT INTO topics (news_id, topic, topic_score, reviewed)

    VALUES (%s, %s, %s, %s)

    '''

    records = [

        ('101', 'Technology', 85, False),

        ('102', 'Health', 90, False),

        ('103', 'Sports', 75, False),

        ('104', 'Entertainment', 80, False),

        ('105', 'Politics', 95, False)

    ]

 

   

   

    connection = Database()

    connection.commit(tmp)

 

    '''cursor = database.cursor()

    cursor.executemany(tmp, records)

    database.commit()

    cursor.close()

    database.close()'''

 

#insert into topic table

 

#get all rows from news table with topics

def retrieve_news_by_topic(topic):

    query = '''

    SELECT news.*

    FROM news

    JOIN topics ON news.news_id = topics.news_id

    WHERE topics.topic = %s

    '''

 

   

    connection = Database()

    connection.commit(query)

   

    '''

    cursor = database.cursor()

    cursor.execute(query, (topic,))

    result = cursor.fetchall()

    cursor.close()

    database.close()

    return result'''

 

#get all rows from news table with topics along with limits

 

def retrieve_top_news_by_topic(topic, limit=5):

    query = '''

    SELECT news.*

    FROM news

    JOIN topics ON news.news_id = topics.news_id

    WHERE topics.topic = %s

    ORDER BY topics.topic_score DESC

    LIMIT %s

    '''

   

    database = Database()

    database.commit(query,(topic,limit))

   

   ''' cursor = database.cursor()

    cursor.execute(query, (topic, limit))

    result = cursor.fetchall()

    cursor.close()

    database.close()

    return result'''

 

 

create_dummy_topic_table()

insert_into_dummy_news()

 

topic = 'Technology'

news_items = retrieve_news_by_topic(topic)

for item in news_items:

    print(item)

 

retrieve_news_by_topic(topic)

retrieve_top_news_by_topic(topic, limit=5)

 

class topic:

    def __init__(self, news_id, topic, topic_score, reviewed):

        self.news_id = news_id

        self.topic = topic

        self.topic_score = topic_score

        self.reviewed = reviewed
