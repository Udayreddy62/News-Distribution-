from environment import Environment

from database import Database

def create_dummy_news_table():

    query = '''CREATE TABLE news_data(

        news_id TEXT PRIMARY KEY,

        companyname TEXT,

        isin TEXT,

        ticker_id TEXT,

        ticker_region TEXT,

        country_code TEXT,

        keywords TEXT,

        headline TEXT,

        story TEXT,

        deliverytimestamputc timestamp

    );'''

 

    connection = Database()

    print(connection.commit(query))

    connection.close()

 

def insert_values_into_dummy_news_table():

    query = '''INSERT INTO news_data (news_id,companyname,isin,ticker_id,ticker_region,country_code,keywords,headline,story,deliverytimestamputc) VALUES

    ("1",

    "Factset",

    "US3030751057",

    "FDS",

    "United States",

    " USA",

    " Financial data, Analytics, Investment, Software, Information, Research",

    "FactSet Revolutionizes Financial Analytics with New Software Suite",

    " FactSet Research Systems Inc., a global leader in financial data and analytic software, has unveiled its latest software suite designed to revolutionize the way investment professionals analyze data. The new suite offers enhanced capabilities for data visualization, advanced analytics, and real-time market insights, empowering users to make informed investment decisions with confidence. Leveraging cutting-edge technology and decades of industry expertise, FactSet's software suite sets a new standard for efficiency and accuracy in financial analysis. This launch reaffirms FactSet's commitment to innovation and its dedication to empowering clients with the tools they need to succeed in today's dynamic markets.",

    "2024-05-21 08:30:00"

     ),

    ("2",

     "StellarTech Solutions",

     "US85914J1025",

     "STS",

     " United States",

     " USA",

     "Technology, Solutions, Innovation, Software",

     "StellarTech Solutions Unveils Groundbreaking AI Software for Business Optimization",

     " StellarTech Solutions, a leading provider of innovative technology solutions, announced the launch of their latest AI software aimed at optimizing business processes. The software, equipped with advanced machine learning algorithms, promises to revolutionize the way companies manage their operations, improve efficiency, and drive growth.",

     "2024-05-21 08:00:00"

     ),

    (

        "3",

        "GreenHarvest Energy",

        " CA39348V1040",

        "GHE",

        "Canada",

        "CAN",

        "Renewable Energy, Sustainability, Clean Technology, Environment",

        "GreenHarvest Energy Expands Renewable Energy Portfolio with New Solar Farm Acquisition",

        " GreenHarvest Energy, a leading player in the renewable energy sector, announced the acquisition of a new solar farm as part of its expansion strategy. This move further solidifies the company's commitment to sustainable energy practices and contributes to reducing carbon emissions while meeting the growing demand for clean power.",

        "2024-05-21 09:30:0"

 

    ),

    (

        "4",

        "Meditech Pharma",

        " DE000A2NBMD3",

        "MTP",

        "Germany",

        "DEU",

        "Healthcare, Pharmaceuticals, Research, Innovation",

        "Meditech Pharma Announces Breakthrough Drug for Rare Genetic Disorder",

        "Meditech Pharma, a leading pharmaceutical company specializing in cutting-edge medical solutions, unveiled a breakthrough drug for the treatment of a rare genetic disorder. The drug, developed after years of intensive research and clinical trials, offers new hope to patients and represents a significant milestone in the field of genetic medicine.",

        "2024-05-21 11:00:00"

    ),

    (

        "5",

        "AeroSky Technologies",

        "FR0014003B87",

        "AST",

        "France",

        "FRA",

        "Aerospace, Aviation, Technology, Innovation",

        " AeroSky Technologies Unveils Next-Generation Drone with Advanced Surveillance Capabilities",

        "AeroSky Technologies introduced its latest innovation in the field of unmanned aerial vehicles (UAVs), unveiling a next-generation drone equipped with advanced surveillance capabilities. The new drone promises enhanced performance, longer flight times, and improved data gathering capabilities, making it ideal for a wide range of applications including security, monitoring, and surveying.",

        "2024-05-21 13:00:00"

    );'''

    connection = Database()

    print(connection.commit(query))

    connection.close()

def fetch_all_data_from_news_table():

    query =  '''SELECT news_data.*, topics.*

                FROM news_data

                INNER JOIN topics

                ON news_data.news_id = topics.news_id  LIMIT 5;'''

    connection = Database()

    print(connection.query(query))

    connection.close()

 

insert_values_into_dummy_news_table()
