from database_connection import get_database_connection


class LeaderboardRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_high_score(self):
        ''' A method that finds high score from the leaderboard database. '''
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT MAX(points) FROM leaderboard''')
        high_score = cursor.fetchone()
        cursor.close()
        return high_score

    def create_new_score(self, name, points):
        ''' A method that creates a new score to the leaderboard database. '''
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO leaderboard (name, points) VALUES (?, ?)''', [
            name, points])
        self._connection.commit()
        cursor.close()


leaderboard_repository = LeaderboardRepository(get_database_connection())
