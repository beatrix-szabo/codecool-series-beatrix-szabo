from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated(order_by_value="rating"):
    return data_manager.execute_select(f'''
    SELECT shows.*, STRING_AGG(genres.name,', ') as genre FROM shows
        JOIN show_genres on show_genres.show_id = shows.id
        JOIN genres on show_genres.genre_id = genres.id
    GROUP BY shows.id
    ORDER BY {order_by_value}  DESC ;''')


def get_show(id):
    return data_manager.execute_select(f'''
    SELECT shows.*, STRING_AGG(genres.name,', ') as genre FROM shows
        JOIN show_genres on show_genres.show_id = shows.id
        JOIN genres on show_genres.genre_id = genres.id
         where shows.id ={id}
    GROUP BY shows.id
    ORDER BY rating DESC ;
    ''')


def get_seasons_for_show(id):
    return data_manager.execute_select(f'SELECT seasons.*  FROM seasons join shows on shows.id = seasons.show_id where show_id = {id} ORDER BY season_number')


def get_actors_for_show(id):
    return data_manager.execute_select(f'''
    SELECT STRING_AGG(actors.name, ' | ') FROM  shows
	    JOIN show_characters on shows.id = show_characters.show_id
	    JOIN actors on show_characters.actor_id = actors.id
	WHERE shows.id = {id}
    GROUP BY shows.id''')