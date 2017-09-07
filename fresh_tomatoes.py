import webbrowser
import os
import re



# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:500,700|Hind:400,600,300" rel="stylesheet" type="text/css">
    <script src="https://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">

        body {
            padding-top: 80px;
            font-family: "Montserrat Light", arial;
            background-color: #e8e8e8;
            color: black;
        }

        .navbar {
            background: red;
        }

        .navbar>.container .navbar-brand{
            text-align: center;
        }

        .navbar-header {
            float: left;
            padding: 15px;
            text-align: center;
            width: 100%;
        }

        .navbar-brand {
        float:none;
        }

        .navbar-inverse .navbar-brand, .navbar-inverse .navbar-nav>li>a {
            font-family: "Montserrat";
            font-size: 28px;
            color: black;
            -webkit-text-fill-color: white;
            -webkit-text-stroke-width: 1px;
            -webkit-text-stroke-color: black;
            font-weight: bold;
        }

        .top {
            margin-right: 10px;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: auto;
        }

        .movie-info{
            position: fixed;
            background-color: black;
            width: 640px;
            height: 200px;
        }

        .movie-review{
            margin-top: 200px;
        }

        .additional-info{
            margin-top: 20px;
        }

        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
            display: block;
            margin: 0 auto;
        }

        h3{
            color: white;
            text-decoration: underline;
        }

        h2{
            font-size: 20px;
        }

        #writeup{
            margin-top: 20px;
            text-align: center;
            color: white;
            margin-left: 100px;
            margin-right: 100px;
            font-size: 14px;
        }

        #director{
            margin-left: 20px;
            position: bottom;
            color: white;
            float: left;
            font-size 8px;
            font-style: italic;
        }

        #runtime{
            position: bottom;
            color: white;
            margin-left: 480px;
            font-size 10px;
            font-style: italic;
        }

        #movie-title{
            color: white;
            text-align: center;
        }

        .movie-tile {
            width: 30%;
            margin: 10px;
            height: 420px;
            padding: 10px;
            background-color: white;
        }

        .movie-tile:hover {
            background-color: #f5d0d0;
            cursor: pointer;
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }

        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

    </style>



    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
            $(".movie-title h3").empty();
            $(".writeup p").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

            // Displays the movie title whenever the trailer modal is opened
            var movieTitle = $(this).attr("data-movie-title");
            $("#movie-title h3").empty().append(movieTitle);

            // Displays the movie storyline whenever the trailer modal is opened
            var movieStoryline = $(this).attr("data-movie-storyline");
            $("#writeup p").empty().append(movieStoryline);

            // Displays the movie director whenever the trailer modal is opened
            var movieDirector = $(this).attr("data-movie-director");
            $("#director span").empty().append(movieDirector);

            // Displays movie runtime whenever the trailer modal is opened
            var movieRuntime = $(this).attr("data-movie-runtime");
            $("#runtime span").empty().append(movieRuntime);

            // Displays the review section plugin from Powr in an iframe whenever the trailer modal is opened
            var movieReview = $(this).attr("data-movie-review");
            $(".movie-review").empty().append($("<iframe></iframe>", {
              'src': movieReview,
              'width':'100%',
              'height':'600px',
              'frameborder': 0,
              'overflow-y': 'scroll'
            }));

            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
          <div class="movie-info">
              <div id="movie-title">
                  <h3></h3>
              </div>
              <div id="writeup">
                  <p></p>
              </div>
              <div class="additional-info">
                  <div id="director">
                      Directed by: <span></span>
                  </div>
                  <div id="runtime">
                      Runtime: <span></span>
                  </div>
              </div>
          </div>
        </div>
        <div class="movie-review">
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <img class = "top" src="images/glasses.png" alt="where did it go?">
            <a class="navbar-brand" href="#">Amir's Favorite Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" data-movie-storyline="{movie_storyline}" data-movie-title="{movie_title}" data-movie-review="{movie_review}" data-movie-director="{movie_director}" data-movie-runtime="{movie_runtime}">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_storyline=movie.storyline,
            movie_review=movie.review,
            movie_director=movie.director,
            movie_runtime=movie.runtime,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
