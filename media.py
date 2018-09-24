import webbrowser


# Create movie class
class Movie():
    # Create constructor
    def __init__(self, movieTitle, movieStoryline, trailerURL, posterURL):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.trailer_youtube_url = trailerURL
        self.poster_image_url = posterURL

    # Create Method to play trailer
    def playTrailer(self):
        webbrowser.open(self.trailer)
