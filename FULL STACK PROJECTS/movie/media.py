import webbrowser


class Movie():
    """ This docstring should explain what the Movie() class does """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        """ This docstring should explain the constructor method """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def show_trailer(self):
        """ This docstring should explain what the show_trailer() function does """  # NOQA
        webbrowser.open(self.trailer_youtube_url)

    
