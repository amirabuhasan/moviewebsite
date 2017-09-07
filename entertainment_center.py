import media
import fresh_tomatoes

boyhood = media.Movie("Boyhood",
                        "Depicts the childhood and adolescence of Mason Evans Jr. from ages six to eighteen as he grows up in Texas with divorced parents" ,
                        "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
                        "https://www.youtube.com/watch?v=Ys-mbHXyWX4",
                        "https://www.powr.io/plugins/comments/view?unique_label=853d733c_1501603925&external_type=iframe",
                        "Richard Linklater",
                        "165 minutes")

#print (toy_story.storyline)


guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                    "In Guardians of the Galaxy, Peter Quill forms an uneasy alliance with a group of extraterrestrial misfits who are fleeing after stealing a powerful artifact." ,
                    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                    "https://www.youtube.com/watch?v=d96cjJhvlMA",
                    "https://www.powr.io/plugins/comments/view?unique_label=826b3dc1_1501604005&external_type=iframe",
                    "James Gunn",
                    "122 minutes")

#print (avatar.storyline)
#avatar.show_trailer()


birdman = media.Movie("Birdman",
                    "A story about a faded Hollywood actor best known for playing the superhero, Birdman." ,
                    "https://upload.wikimedia.org/wikipedia/en/6/63/Birdman_poster.png",
                    "https://www.youtube.com/watch?v=uJfLoE6hanc",
                    "https://www.powr.io/plugins/comments/view?unique_label=148c0c3d_1501603637&external_type=iframe",
                    "Alejandro G. Inarritu",
                    "119 minutes")

#birdman.show_trailer()

before_sunset = media.Movie("Before Sunset",
                    "The film picks up the story in Before Sunrise of the young American man and French woman who spent a passionate night together in Vienna." ,
                    "https://upload.wikimedia.org/wikipedia/en/d/d1/Before_Sunset_poster.jpg",
                    "https://www.youtube.com/watch?v=oI3UuneLcyU",
                    "https://www.powr.io/plugins/comments/view?unique_label=d4814f00_1501604138&external_type=iframe",
                    "Richard Linklater",
                    "80 minutes")

the_darjeeling_limited = media.Movie("The Darjeeling Limited",
                    "A year after their father's funeral, three brothers travel across India by train in an attempt to bond with each other." ,
                    "https://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg",
                    "https://www.youtube.com/watch?v=aO1bYukdvLI",
                    "https://www.powr.io/plugins/comments/view?unique_label=593315b7_1501604391&external_type=iframe",
                    "Wes Anderson",
                    "91 minutes")

beginners = media.Movie("Beginners",
                    "A young man is rocked by two announcements from his elderly father: that he has terminal cancer, and that he has a young male lover." ,
                    "https://upload.wikimedia.org/wikipedia/en/f/f6/Beginners_Poster.jpg",
                    "https://www.youtube.com/watch?v=rXUFUp6vsxg",
                    "https://www.powr.io/plugins/comments/view?unique_label=3b77b0f2_1501604479&external_type=iframe",
                    "Mike Mills",
                    "104 minutes")

the_breakfast_club = media.Movie("The Breakfast Club",
                    "Five high school students meet in Saturday detention and discover how they have a lot more in common than they thought." ,
                    "https://upload.wikimedia.org/wikipedia/en/5/50/The_Breakfast_Club.jpg",
                    "https://www.youtube.com/watch?v=BSXBvor47Zs",
                    "https://www.powr.io/plugins/comments/view?unique_label=15d41675_1501604534&external_type=iframe",
                    "John Hughes",
                    "97 minutes")

the_truman_show = media.Movie("The Truman Show",
                    "An insurance salesman/adjuster discovers his entire life is actually a television show." ,
                    "https://upload.wikimedia.org/wikipedia/en/c/cd/Trumanshow.jpg",
                    "https://www.youtube.com/watch?v=loTIzXAS7v4",
                    "https://www.powr.io/plugins/comments/view?unique_label=8fb288d8_1501604580&external_type=iframe",
                    "Peter Weir",
                    "103 minutes")

inside_llewyn_davis = media.Movie("Inside Llewyn Davis",
                    "A week in the life of a young singer as he navigates the Greenwich Village folk scene of 1961." ,
                    "https://upload.wikimedia.org/wikipedia/en/d/df/Inside_Llewyn_Davis_Poster.jpg",
                    "https://www.youtube.com/watch?v=LFphYRyH7wc",
                    "https://www.powr.io/plugins/comments/view?unique_label=56b0bf07_1501604622&external_type=iframe",
                    "Joel Coen & Ethan Coen",
                    "105 minutes")

movies = [boyhood, guardians_of_the_galaxy, birdman, before_sunset, the_darjeeling_limited, beginners, the_breakfast_club, the_truman_show, inside_llewyn_davis]


fresh_tomatoes.open_movies_page(movies)
