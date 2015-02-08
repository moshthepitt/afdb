import webbrowser

class Movie():
    """
    This class provides a way to store movie information
    """
    def __init__(self, movie_title, storyline, poster_image, youtube_url, watch_url):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url
        self.watch_url = watch_url #a url where you can watch the whole movie

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf-8')

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


