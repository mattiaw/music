import easygui
import sys

# importing pafy module 
import pafy 

# importing time and vlc 
import time, vlc 

def controller(player,vlc_instance):
    image = "earth.gif"
    while True:
        choice = easygui.buttonbox(title="@biglesp Audio Player",msg="Press Play to start",image=image,choices=["Play","Pause","Stop","New","Exit"])
        print(choice)
        if choice == "Play":
            player.play()
        elif choice == "Pause":
            player.pause()
        elif choice == "Stop":
            player.stop()
        elif choice == "New":
            source = easygui.fileopenbox(title="Choose media to open")
            # creating a media 
            media = vlc_instance.media_new(source) 
      
            # setting media to the player 
            player.set_media(media) 
        elif choice == "Exit":
            # exits the program 
            sys.exit("Exit button pressed")     

        else:
            break

# creating a vlc instance 
vlc_instance = vlc.Instance() 

# creating a media player 
player = vlc_instance.media_player_new()

player.toggle_fullscreen()
'''
# creating a media 
media = vlc_instance.media_new(source) 
      
# setting media to the player 
player.set_media(media) 
'''
controller(player,vlc_instance)