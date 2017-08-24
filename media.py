import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        Assigns parameters to instance variables.

        Args:
            move_title (str): Title of the movie.
            movie_storyline (str): Storyline of the movie.
            poster_image (str): Link to the poster image of the movie.
            trailer_youtube (str): Link to the youtube trailer of movie.

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
