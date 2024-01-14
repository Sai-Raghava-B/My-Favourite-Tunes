To login Create a user in the terminal with "python manage.py createsuperuser"
and run the server with  this command " python manage.py runserver  "

and login in the end point "/accounts/login/"

and check the end points :-   songs 
                              songs/int:song_id/
                                    to check the songs and the artists for the respective album and with id
                              
                              artist-song-count/
                                    to check all the artists and there number of albums
                              
                              favorite-songs/
                                    to check all the song which you added from the songs list as your favorite
                                  
                              add-favorite-song/<int:song_id>/
                              all-songs/
                                    to add songs either by id or from the list off all songs where you can add the song to ur favorite collection


you can check add more songs by the role of admin.
