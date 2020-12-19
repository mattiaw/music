import pandas as pd
import easygui
import sys

# importing pafy module 
import pafy 

# importing time and vlc 
import time, vlc 

def controller(player):
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
            kickoff(source)
        elif choice == "Exit":
            # exits the program 
            sys.exit("Exit button pressed")     

        else:
            break

def load_media_data(filename):
    return pd.read_csv(filename,header=None)

def kickoff(input_file):
    media = load_media_data(input_file)
    media.columns =["URL","Name","Index"]

    #set playlist to random
    df = media.sample(frac=1.0)

    for i, row in df.iterrows():
        print(df.at[i,"Name"])	
        try:
            format4yt(df.at[i,"URL"])
        except:
            print("Encountered exception while accessing: ",df.at[i,'URL']," waiting 15 seconds before proceding....")
            time.sleep(15) 
            continue

# method to play video 
def video(source): 
     
    # creating a media 
    media = vlc_instance.media_new(source) 
      
    # setting media to the player 
    player.set_media(media) 

 
    # play the video 
    player.play() 
      
    # wait time 
    time.sleep(0.5) 
      
    # getting the duration of the video 
    duration = player.get_length() 
      
    # printing the duration of the video 
    print("Duration : " + str(duration)) 

def format4yt(url):
    vid = pafy.new(url)
    best = vid.getbest()
    video(best.url)
    time.sleep(vid.length)
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
controller(player)

