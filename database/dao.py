from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return

    @staticmethod
    def get_nodes(n_alb):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select ar.id 
                from album al , artist ar
                where ar.id = al.artist_id 
                group by ar.id 
                having count(*) >= %s
                """
        cursor.execute(query, (n_alb,))
        for row in cursor:
            result.append(row['id'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_art_gen():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select a.id, t.genre_id
                from album al, artist a , track t 
                where a.id = al.artist_id and al.id = t.album_id 
                group by a.id, t.genre_id
                """
        cursor.execute(query)
        for row in cursor:
            result.append((row['id'], row['genre_id']))
        cursor.close()
        conn.close()
        return result
