import webbrowser


class Movie:
    """This class provides a way to store movie related information

    Args:
        movie_title (str): Movie's title
        movie_storyline (str): Short explanation of storyline of movie
        poster_image (str): Link to the poster image of the movie
        trailer_youtube (str): Link to the trailer of the movie on YouTube

    Attributes:
        title (str): Movie's title
        storyline (str): Short explanation of storyline of movie
        poster_image_url (str): Link to the poster image of the movie
        trailer_youtube_url (str): Link to the trailer of the movie on YouTube

    Methods:
        show_trailer : Plays the trailer from YouTube in the browser
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # opens the link to the trailer in the browser
        webbrowser.open(self.trailer_youtube_url)
