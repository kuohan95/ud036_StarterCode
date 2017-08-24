import fresh_tomatoes
import media

# List of movies
# Trailers from Youtube

xxx_return_of_xander_cage = media.Movie(
    "xXx",
    "A story of a man hired to perform dangerous stunts",
    "https://upload.wikimedia.org/wikipedia/en/9/9c/"
    "Xxx_return_of_xander_cage_film_poster.jpeg",
    "https://www.youtube.com/watch?v=cvYqGWgkvV8")

the_lego_batman_movie = media.Movie(
    "The LEGO Batman",
    "A Batman movie in LEGO form",
    "https://upload.wikimedia.org/wikipedia/en/6/61/"
    "The_Lego_Batman_Movie_PromotionalPoster.jpg",
    "https://www.youtube.com/watch?v=rGQUKzSDhrg")

john_wick_chapter_2 = media.Movie(
    "John Wick",
    "A movie about a man who takes revenge after his dog gets murdered",
    "https://upload.wikimedia.org/wikipedia/en/9/98/"
    "John_Wick_TeaserPoster.jpg",
    "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

logan = media.Movie(
    "Logan",
    "A movie about a wolverine that reunites with his daughter",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=DekuSxJgpbY")

power_rangers = media.Movie(
    "Power Rangers",
    "A team of 5 superhumans with awesome ootd",
    "https://upload.wikimedia.org/wikipedia/en/7/78/"
    "Power_Rangers_%282017_Official_Theatrical_Poster%29.png",
    "https://www.youtube.com/watch?v=5kIe6UZHSXw")

wonder_woman = media.Movie(
    "Wonder Woman",
    "A story of a medieval woman in the future",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/"
    "Wonder_Woman_%282017_film%29.jpg",
    "https://www.youtube.com/watch?v=VSB4wGIdDwo")


# Add movies to an array
movies = [xxx_return_of_xander_cage, the_lego_batman_movie,
          john_wick_chapter_2, logan, power_rangers, wonder_woman]
    

# Parse list of movies to fresh tomatoes
fresh_tomatoes.open_movies_page(movies)
