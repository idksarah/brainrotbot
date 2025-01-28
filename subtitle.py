#from moviepy import *

# Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# Reduce the audio volume to 80% of its original volume

# clip = (
#     VideoFileClip("bg/mc.mp4")
#     .subclipped(10, 20)
#     .with_volume_scaled(0.8)
# )

# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip(
#     font=None,
#     text="tryna contribute to the ocford study rn tbh",
#     font_size=70,
#     color='white'
# ).with_duration(10).with_position('center')

# # Overlay the text clip on the first video clip
# final_video = CompositeVideoClip([clip, txt_clip])
# final_video.write_videofile("videos/test.mp4")

#
def subtitle(text):
    splitText = text.split(" ")
    subtitles =[]
    charCounter = 0
    currentSubtitle = ""
    maxChar = 10
    for word in splitText:
        if((charCounter +  len(word)) < maxChar):
            currentSubtitle += " " + word
            charCounter += len(word) + 1
        else:
            if(len(word) > maxChar):
                currentSubtitle = word
                print(currentSubtitle)
                subtitles.append(currentSubtitle)
                currentSubtitle = ""
                charCounter=0
            else:
                subtitles.append(currentSubtitle)
                currentSubtitle = word
                charCounter = len(word)
    print(subtitles)

subtitle("tryna contribute to the ocford study rn tbh")