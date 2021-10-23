import sys
import easygui
import asyncio

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if (i == 1):
            input_file = arg
        print(f"Argument {i:>6}: {arg}")

# importing pafy module 
import pafy 

# importing time and vlc 
import time, vlc 

import pandas as pd

def load_media_data(filename):
    return pd.read_csv(filename,header=None)
  
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

async def format4yt(url):
    vid = pafy.new(url)
    best = vid.getbest()
    video(best.url)
    #time.sleep(vid.length)
    #asyncio.run(controller(player))	
    await asyncio.sleep(vid.length)

async def controller(player,url):
    #image = "bigles.gif"
    image = "earth.gif"
    #player.play()
    while True:
        asyncio.run(format4yt(url))
        #await asyncio.sleep(10)
        choice = easygui.buttonbox(title="@biglesp Audio Player",msg="Press Play to start",image=image,choices=["Play","Pause","Stop","New"])
        print(choice)
        if choice == "Play":
            player.play()
        elif choice == "Pause":
            player.pause()
        elif choice == "Stop":
            player.stop()
        elif choice == "New":
            media = easygui.fileopenbox(title="Choose media to open")
            #player = vlc.MediaPlayer(media)
        else:
            break
toggle = 0
# creating a vlc instance 
vlc_instance = vlc.Instance() 

# creating a media player 
player = vlc_instance.media_player_new()
#asyncio.run(controller(player))
player.toggle_fullscreen()

# call the video method 
media = load_media_data(input_file)
media.columns =["URL","Name","Index"]


df = media.sample(frac=1.0)

for i, row in df.iterrows():
    print(df.at[i,"Name"])	
    try:
    	#format4yt(df.at[i,"URL"])
        asyncio.run(controller(player,df.at[i,"URL"]))
        
        
    except:
        print("Encountered exception while accessing: ",df.at[i,'URL']," waiting 15 seconds before proceding....")
        time.sleep(15) 
        continue

'''
    if (toggle == 0):
        controller(player)
        toggle = 1
        player.play()
    else:
        player.play() 
'''