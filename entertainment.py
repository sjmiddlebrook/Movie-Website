import fresh_tomatoes
import media

# instance of class Movie for Caddyshack
caddyshack = media.Movie("Caddyshack",
                         "An exclusive golf course has to deal with a brash "
                         "new member and a destructive dancing gopher",
                         "https://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=x9Nl39uWEYk")

# instance of class Movie for Happy Gilmore
happy_gilmore = media.Movie("Happy Gilmore",
                            "A rejected hockey player puts his skills to the "
                            "golf course to save his grandmother's "
                            "house",
                            "https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",    # noqa
                            "https://www.youtube.com/watch?v=y1emDAYCfVQ")

# instance of class Movie for Butch Cassidy
butch_cassidy = media.Movie("Butch Cassidy",
                            "Two Western bank/train robbers flee to Bolivia "
                            "when the law gets too close.",
                            "https://upload.wikimedia.org/wikipedia/en/f/fd/Butch_sundance_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=YdJW2UxvSFQ")

# instance of class Movie for Back to the Future
back_to_the_future = media.Movie("Back to the Future",
                                 "Marty McFly, a 17-year-old high school "
                                 "student, is accidentally sent thirty years "
                                 "into the past in a time-traveling DeLorean "
                                 "invented by his close friend, "
                                 "the maverick scientist Doc Brown.",
                                 "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

# instance of class Movie for Gladiator
gladiator = media.Movie("Gladiator",
                        "When a Roman General is betrayed, and his family "
                        "murdered by an emperor's corrupt son, "
                        "he comes to Rome as a gladiator to seek revenge.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=owK1qxDselE")

# instance of class Movie for Shawshank Redemption
shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Two imprisoned men bond over a number of "
                                   "years, finding solace and eventual "
                                   "redemption through acts of common "
                                   "decency.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")  # noqa

# instance of class Movie for Lion King
lion_king = media.Movie("The Lion King",
                        "Lion cub and future king Simba searches for his "
                        "identity. His eagerness to please others and "
                        "penchant for testing his boundaries sometimes gets "
                        "him into trouble.",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

# List of movies initialized above
movies = [butch_cassidy, back_to_the_future, happy_gilmore, gladiator,
          shawshank_redemption, lion_king, caddyshack]

# create html page from the list of movies
fresh_tomatoes.open_movies_page(movies)
