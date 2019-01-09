import webbrowser
class Trailer():
    '''This class gives the information about movie trailers'''
    def __init__(self,movie_name,movie_release_year,movie_poster_link,movie_trailer_link):
        '''In this method attributes of movie are intialized using contrsuctor
        movie_name--->For name of the movie,movie_release_year--->In which year
        the movie is released,movie_poster_link--->poster of the particular movie,
        movie_trailer_link--->for viewing the trailer of the movie'''
        self.name=movie_name
        self.release_year=movie_release_year
        self.poster_link=movie_poster_link
        self.trailer_link=movie_trailer_link
    def view_trailer(self):
        '''This method plays the trailer of the movie'''
        webbrowser.open(self.trailer_link)
