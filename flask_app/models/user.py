from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        print(users)
        return users

    # @classmethod
    # def select_last(cls, data ):
    #     query = 'SELECT id FROM users ORDER BY id DESC LIMIT 1;'
    #     return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def save(cls, data ):
        query = 'INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );'
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def select_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('users_schema').query_db( query, data )
        return User(results[0])


    @classmethod
    def change(cls, data ):
        query = 'UPDATE * SET last_name = adsfasd WHERE (id = {{ user.id }});'
        return connectToMySQL('users_schema').query_db( query, data )


    @classmethod
    def remove(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        connectToMySQL('users_schema').query_db( query, data )


    @classmethod
    def change(cls, data):
        query = 'UPDATE users SET  first_name = %(fname)s , last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;'
        connectToMySQL('users_schema').query_db( query, data )