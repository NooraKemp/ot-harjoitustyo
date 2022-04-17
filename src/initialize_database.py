from database_connection import get_database_connection


def drop_table(connection):
    cursor = connection.cursor()
    cursor.execute('''drop table if exists leaderboard''')
    connection.commit()


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table leaderboard (
            name text,
            points integer
            );
        ''')
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_table(connection)
    create_table(connection)


if __name__ == '__main__':
    initialize_database()
