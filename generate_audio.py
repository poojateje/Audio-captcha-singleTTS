#Import libraries
from gtts import gTTS 
import os
import random
#read symbol file to get alphabets as well as numerical letters
with open('symbols.txt', 'r') as file:
    symbols = file.read().replace('\n', '')
#give range to generate number of train data
for j in range(100000):
  s = ''
  #randomly select 8 letters using 'symbols.txt' file
  for i in range(8):
    s = s + str(symbols[random.randint(0,len(symbols)-1)])
  mytext = s
  #using general English language here
  language = 'en'
  #generate audio
  myobj = gTTS(text=mytext, lang=language, slow=False)
  #Save audio file with same name as that of captcha value  
  myobj.save("audio_captchas/"+s+".mp3")
  #provide indication of train data generation after every 300 iteration
  if j % 300 == 0:
    print(str(j)+' done')

