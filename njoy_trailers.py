import play_trailer
import fresh_tomatoes
'''Give your all time favourite movies with 4 parameters each:
movie_name,movie_release_year,movie_poster_link,movie_trailer_link'''
MS_Dhoni=play_trailer.Trailer("MSDhoni",2016,
                              "http://media.glamsham.com/download/poster/images/m.s.dhoni/05-m.s.dhoni.jpg",
                              "https://www.youtube.com/watch?v=6L6XqWoS8tw")
Dangal=play_trailer.Trailer("Dangal",2016,
                              "https://3.bp.blogspot.com/-eRCZzx7dfow/V3uDs7hZNKI/AAAAAAADz8g/D96eJVsBGJg5yzgwtzp_OEntolQe7DJiwCHM/w650/13592569_1380230285324067_6698582262276363961_n",
                              "https://www.youtube.com/watch?v=x_7YlGv9u1g")
Chakde_India=play_trailer.Trailer("Chakde India",2007,
                              "data:image/jpeg;base64,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",
                              "https://www.youtube.com/watch?v=6a0-dSMWm5g")
Bhaag_Milka_Bhaag=play_trailer.Trailer("Bhaag Milka Bhaag",2013,
                              "http://media.glamsham.com/download/poster/images/bhaag-milkha-bhaag/04-bhaag-milkha-bhaag.jpg",
                              "https://www.youtube.com/watch?v=3uICXnnW86U")
Three_Idiots=play_trailer.Trailer("3 Idiots",2009,
                              "https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                              "https://www.youtube.com/watch?v=xvszmNXdM4w")
Lagaan=play_trailer.Trailer("Lagaan",2001,
                              "data:image/jpeg;base64,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",
                              "https://www.youtube.com/watch?v=oSIGQ0YkFxs")
#creating a list and add all the movies into that list which we declared above
Movies_List=[MS_Dhoni,Dangal,Chakde_India,Bhaag_Milka_Bhaag,Three_Idiots,Lagaan]
#passing the movies list and opening the trailers webpage
fresh_tomatoes.open_movies_page(Movies_List)