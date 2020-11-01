from PIL import Image, ImageDraw, ImageFont
import os
#import imageio
#from moviepy.config import change_settings
#change_settings({"FFMPEG_BINARY":"ffmpeg.exe"})
#fnt=ImageFont.truetype("arial.ttf",55)
def agent():
                
    img = Image.new('RGB', (512, 208))
    d = ImageDraw.Draw(img)
    d.text((100,85), str(i), fill=(255,255,255),font=fnt)
    d.text((225,85), str(j), fill=(255,255,255),font=fnt)
    d.text((350,85), str(k), fill=(255,255,255),font=fnt)

    img.save('data'+os.sep+'karta.jpg')
