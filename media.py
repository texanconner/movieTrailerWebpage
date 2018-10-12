import webbrowser


# Create movie class
class Movie():
    # Create constructor
    def __init__(self, movieTitle, movieStoryline, trailerURL, posterURL):
        """
        Constructor to create our Moive object with 4 attributes.
        Inputs:
        	movieTitle: Title of the movie.
        	movieStoryline: Short description of the movie.
        	trailerURL: URL to play the trailer video.
			posterURL: URL to the Movie image
		Behavior:
			Makes a movie object with 4 attributes.
		Output:
			New instance of the Movie class.
        """
        self.title = movieTitle
        self.storyline = movieStoryline
        self.trailer_youtube_url = trailerURL
        self.poster_image_url = posterURL

    # Create Method to play trailer
    def playTrailer(self):
        """
        Opens a webbrowser and plays the movie trailer from the URL give.
        """
        webbrowser.open(self.trailer)
        