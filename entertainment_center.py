import media
import webbrowser
import fresh_tomatoes

# Create movie objects
ironMan = media.Movie("Iron Man", "Iron Man vs Bigger Iron Man",
                        "https://www.youtube.com/watch?v=8hYlB38asDY",
                        "http://www.freemovieposters.net/posters/iron_man_2008_101_poster.jpg")
captainAmerica = media.Movie("Captain America", "Cap vs A Redhead",
                        "https://www.youtube.com/watch?v=JerVrbLldXw",
                        "http://www.movieposter.com/posters/archive/main/124/MPW-62001")
thorRagnarok = media.Movie("Thor Ragnarok", "Sibling Rivalry",
                        "https://www.youtube.com/watch?v=ue80QwXMRHg",
                        "http://www.joblo.com/posters/images/full/thor-ragnarok-poster-main.jpg")
blackPanther = media.Movie("Black Panther", "Catfight",
                        "https://www.youtube.com/watch?v=xjDjIWPwcPU",
                        "https://www.dvdsreleasedates.com/posters/800/B/Black-Panther-2018-movie-poster.jpg")
spiderMan = media.Movie("Spider-Man Homecoming", "Spooderman fights a bird",
                        "https://www.youtube.com/watch?v=39udgGPyYMg",
                        "http://s3.birthmoviesdeath.com/images/made/Spider-Man-Homecoming-Poster_1200_1823_81_s.jpg")
doctorStrange = media.Movie("Doctor Strange", "Sherlock Christmas Special",
                        "https://www.youtube.com/watch?v=HSzx-zryEgM",
                        "http://findingsanityinourcrazylife.com/wp-content/uploads/2016/11/Doctor-Strange-Movie-Poster.jpg")

# Create array of the movie objects
movies = [ironMan, captainAmerica, thorRagnarok, blackPanther, spiderMan, doctorStrange]

# Call fuction to open webpage and display my movies array
fresh_tomatoes.open_movies_page(movies)
