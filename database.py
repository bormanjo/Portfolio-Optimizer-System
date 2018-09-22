import mysql.connector
from mysql.connector import Error

class Dataloader:
    def __init__(self, config):
        self.config = config
        
        if(self.test_connection()):
            self.connection = self.get_connection()
        else:
            print("Dataloader was unable to connect to the Database")
            self.connection = None
    
    def test_connection(self):
        '''Tests connection (True/False) to the database with the initialized parameters'''
        try:
            connection = mysql.connector.connect(**self.config)
            
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Succesfully Connected to MySQL database. MySQL Server version on ", db_info)
                result = True
                
            connection.close()
            
        except Error as e:
            print ("Error while connecting to MySQL", e)
            result = False
            
        return result
    
    def get_connection(self):
        '''Returns a connection object to the database'''
        try:
            connection = mysql.connector.connect(**self.config)
            if connection.is_connected():
                return connection
            else:
                print("Connection failed.")
        except Error as e:
            print("Error while connecting to MySQL", e)
            exit(1)
            
    def get_cursor(self):
        '''Returns a cursor object from the provided connection'''
        try:
            cursor = self.connection.cursor()
            return cursor
        except Error as e:
            print("Error while getting SQL cursor", e)
            exit(1)
    
    def create_database(self, DB_NAME):
        '''Attempts to create a new database for the provided DB_NAME'''
        try:
            cursor = self.get_cursor()
            cursor.execute("CREATE DATABASE {}".format(DB_NAME))
            cursor.close()
        except Error as e:
            print("Failed creating database: {}".format(e))
            exit(1)
            
    def get_tables(self):
        try:
            cursor = self.get_cursor()
            
            cursor.execute("USE portfolio_optimizer_db;")
            cursor.execute("SHOW TABLES;")
            
            result = cursor.fetchall()
            cursor.close()
            
            return result
        except Error as e:
            print("Failed to get tables: {}".format(e))
            exit(1)
            