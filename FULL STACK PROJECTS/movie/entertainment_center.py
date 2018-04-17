import fresh_tomatoes
import media

# Avatar: movie title, storyline, movie poster and movie trailer

Avatar = media.Movie(
"Avatar",
"A marine on an alien planet",
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",       # NOQA
"https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Ghost_In_The_Shell: movie title, storyline, movie poster and movie trailer

Ghost_in_the_shell = media.Movie(
"Ghost in the shell",
"The year is 2029. The world has become intensively"
"information oriented and humans are well-connected to the network.",
"https://upload.wikimedia.org/wikipedia/en/c/ca/Ghostintheshellposter.jpg",      # NOQA
"https://www.youtube.com/watch?v=SvBVDibOrgs")

# Prometheus: movie title, storyline, movie poster and movie trailer

Prometheus = media.Movie(
"Prometheus",
"A team of scientist go to space in search of mans origins",
"https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",      # NOQA
"https://www.youtube.com/watch?v=HHcHYisZFLU")

# The_Signal: movie title, storyline, movie poster and movie trailer

The_Signal = media.Movie(
"The signal",
"Three college students track a hacker in the desert and find the unexpected",   # NOQA
"https://upload.wikimedia.org/wikipedia/en/2/24/The_Signal_poster.jpg",
"https://www.youtube.com/watch?v=CHln1wPlBWw")

# Kung_Fu_Hustle: movie title, storyline, movie poster and movie trailer

Kung_Fu_Hustle = media.Movie(
"Kung Fu Hustle",
"a wannabe gangster aspires to join the notorious Axe Gang",
"https://upload.wikimedia.org/wikipedia/en/0/00/KungFuHustleHKposter.jpg",       # NOQA
"https://www.youtube.com/watch?v=VSfJZ6B4P6Y")

# Batman_Under_The_Red_Hood: movie title,storyline,movie poster and movie trailer   # NOQA

Batman_Under_The_Red_Hood = media.Movie(
"Batman Under The Red Hood",
"Batman faces a vigilante who aims to clean up"
"Gotham City but does not follow his moral code.",
"https://upload.wikimedia.org/wikipedia/en/4/4c/Batman_under_the_red_hood_poster.jpg",  # NOQA
"https://www.youtube.com/watch?v=YLymYj2Thfc")

# Boku_dake_ga_Inai_Machi: movie title,storyline,movie poster and movie trailer

Boku_dake_ga_Inai_Machi = media.Movie(
"Boku dake ga Inai Machi(Erased)",
"The story follows Satoru Fujinuma, a man who"
"somehow possesses an ability to time travel",
"https://upload.wikimedia.org/wikipedia/en/6/60/Boku_Dake_ga_Inai_Machi_vol1.jpg",  # NOQA
"https://www.youtube.com/watch?v=SUKevBJ703o")

# set the movies that will be passed to the movie file

movies = [
    Avatar,
    Ghost_in_the_shell,
    Prometheus,
    The_Signal,
    Kung_Fu_Hustle,
    Batman_Under_The_Red_Hood,
    Boku_dake_ga_Inai_Machi]

# Open the HTML file in webbrowser via the fresh_tomatoes.py file

fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
