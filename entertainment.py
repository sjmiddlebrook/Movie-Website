import fresh_tomatoes
import media

caddyshack = media.Movie("Caddyshack",
                         "An exclusive golf course has to deal with a brash new member and a destructive dancing gopher",
                         "https://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg",
                         "https://www.youtube.com/watch?v=x9Nl39uWEYk")

happy_gilmore = media.Movie("Happy Gilmore",
                            "A rejected hockey player puts his skills to the golf course to save his grandmother's "
                            "house",
                            "https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",
                            "https://www.youtube.com/watch?v=y1emDAYCfVQ")

gladiator = media.Movie("Gladiator",
                        "When a Roman General is betrayed, and his family murdered by an emperor's corrupt son, "
                        "he comes to Rome as a gladiator to seek revenge.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Two imprisoned men bond over a number of years, finding solace and eventual "
                                   "redemption through acts of common decency.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

lion_king = media.Movie("The Lion King",
                        "Lion cub and future king Simba searches for his identity. His eagerness to please others and "
                        "penchant for testing his boundaries sometimes gets him into trouble.",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

finding_nemo = media.Movie("Finding Nemo",
                           "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid "
                           "clownfish sets out on a journey to bring him home.",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

movies = [caddyshack, happy_gilmore, gladiator, shawshank_redemption, lion_king, finding_nemo]

fresh_tomatoes.open_movies_page(movies)
