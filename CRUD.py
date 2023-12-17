from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    
    def __init__(self, username, password):
        """
        Initialize a connection to a MongoDB database.

        Args:
        - username: Username for authentication.
        - password: Password for authentication.

        This method initializes a connection to a MongoDB database using the provided username and password.
        It slso sets up the necessary connection variables like the host, port, database name, and collection name.
        If an exception occurs during initialization, it prints an error message indicating an invalid initialization.
        """

        try: 
            # Intializing MongoDB connection Variables
            USER = username
            PASS = password
            HOST = 'nv-desktop-services.apporto.com'
            PORT = 32426
            DB = 'AAC'
            COL = 'animals'

            # Initialize MongoDB Connection
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
            
        except Exception as e:           
            print(f'Invalid Initialization: {e}')


    def create(self, data):
        """
        Create a new document in the 'animals' collection.

        Args:
            - data: A dictionary containing the data for the new document.

        Returns:
            - "True" if a document was inserted successfully.
            - "False" if a document was not inserted.
        """

        try:
            inserted = "False"
            
            if data is not None:
                result = self.database.animals.insert_one(data)
                
                if result.inserted_id:
                    inserted = 'True'
                
                else:
                    
                    inserted = 'False'
                    
            print(inserted)

        except Exception as e:           
            print(f'Invalid Entry: {e}')


    def read(self, query):
        """
        Retrieve documents from the 'animals' collection based on the provided query.

        Args:
            - query: A dictionary representing the query to find documents.

        Returns:
            - List of documents matching the query.
        """

        try:
            result = list(self.database.animals.find(query))
            return result

        except Exception as e:
            print(f'Invalid Query: {e}')
            return []
        

    def update(self, query, update):
        """
        Update documents in the 'animals' collection based on the provided query and update.

        Args:
            - query: A dictionary representing the query to find documents for updating.
            - update: A dictionary containing the fields and values to be updated.

        Returns:
            - Number of documents that were updated.
        """

        try:
            if update is not None and query is not None:
                docs_to_update = list(self.database.animals.find(query))
                
                if len(docs_to_update) == 0:
                    return print('Invalid Update: Document does not exist.')
                
                else:
                    for doc in docs_to_update:
                        self.database.animals.update_one({'_id': doc['_id']}, {'$set' : update})
                    return print(str(len(docs_to_update)) + ' document(s) were updated.')
        
            else:
                print('Invalid Update: Query is empty.')
                
            
        except Exception as e:
                print(f'Invalid Update: {e}')
                

    def delete(self, query):
        """
        Delete documents from the 'animals' collection based on the provided query.

        Args:
            - query: A dictionary representing the query to find documents for deletion.

        Returns:
            - Number of documents that were deleted.
        """

        try:
            if query is not None:
                deleted_docs = self.database.animals.delete_many(query)
                
                if deleted_docs.deleted_count == 0:
                    return print('Invalid Deletion: Document does not exist.')
                
                else:
                    return print(str(deleted_docs.deleted_count) + ' document(s) were deleted.')
            
            else:
                print('Invalid Deletion: Query is empty.')  
            
            
        except Exception as e:
                print(f'Invalid Deletion: {e}')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    