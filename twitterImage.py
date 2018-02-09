# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

import rainbowhat as rh
import datetime
import time

from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

def setVars():
	global temperature 
	global pressure
	global now
	temperature = rh.weather.temperature()
	pressure = rh.weather.pressure()
	now = datetime.datetime.now()

def tweet():
	setVars()
	drawImage()
	message = ""
	with open("/home/pi/RainbowHat/tweetEditted.jpg") as photo:
		twitter.update_status_with_media(status=message, media=photo)
		print("Tweeted")
	time.sleep(300)

def drawImage():
	image = Image.open('/home/pi/RainbowHat/tweet.jpg')
	font_type = ImageFont.truetype("Roboto-Bold.ttf",60)
	draw = ImageDraw.Draw(image)
	draw.text(xy=(250,165),text=now.strftime("%Y-%m-%d %H:%M"),fill=(128,128,128),font=font_type)	
	draw.text(xy=(250,360),text=str(round(temperature, 2)),fill=(128,128,128),font=font_type)
	image.save('tweetEditted.jpg')

while True:
	tweet()



