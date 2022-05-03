from database_connection import get_database_connection


class LeaderboardRepository:

    def __init__(self, connection):
        """A class that represents the Leaderboard repository."
    
        Attributes:
        self._connection = Database connection.
        """
        self._connection = connection

    def find_high_score(self):
        ''' Finds the highest score from the leaderboard database.
        Returns: The highest score.
        '''
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT MAX(points) FROM leaderboard''')
        high_score = cursor.fetchone()

        return high_score

    def create_new_score(self, name, points):
        ''' Adds new score to the leaderboard database. '''
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO leaderboard (name, points) VALUES (?, ?)''', [
            name, points])
        self._connection.commit()

    def delete_all(self):
        '''Deletes all scores form the leaderboard database.'''
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM leaderboard''')
        self._connection.commit()


leaderboard_repository = LeaderboardRepository(get_database_connection())
