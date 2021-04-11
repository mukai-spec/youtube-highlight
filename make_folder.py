import re
import os
from pytube import YouTube

###youtube_urlからvideo_idを抜き出す
def make_videoid(youtube_url):
    video_id = re.search("=.*",youtube_url)
    video_id = video_id.group()
    video_id = re.sub("=","",video_id)
    return(video_id)

###フォルダを作成
def make_folder(youtube_url, path):
    path = ''
    youtube = YouTube(youtube_url)
    title = youtube.title
    print("動画タイトル：",title)
    ##youtube.titleに/が入っているときの操作
    if '/' in youtube.title:
      title = youtube.title.replace('/','')
    if '#' in title:
      title = title.replace('#','')
    ###pathの指定用
    folder_name = path + title
    os.makedirs(folder_name,exist_ok=True)
    return(folder_name)

###特定の単語の頻度を抽出
def get_word_time(comment_data, word):
  time = []
  for i in range(len(comment_data)):
    result = re.search(word, comment_data[i]['text'])
    if not result:
      continue
    else:
      sec = int(comment_data[i]['time'].replace(':',''))
      if sec < 0:
          sec = sec * -1
          hour,min = divmod(sec,10000)
          min,sec = divmod(min,100)
          sec = -1 * (3600*hour + 60*min +sec)
      else:
          hour,min = divmod(sec,10000)
          min,sec = divmod(min,100)
          sec = 3600*hour + 60*min +sec
      time.append(sec)
  return(time)

###コメント数のみを抽出
def get_time(comment_data):
  time = []
  for i in range(len(comment_data)):
    sec = int(comment_data[i]['time'].replace(':',''))
    if sec < 0:
      sec = sec * -1
      hour,min = divmod(sec,10000)
      min,sec = divmod(min,100)
      sec = -1 * (3600*hour + 60*min +sec)
    else:
      hour,min = divmod(sec,10000)
      min,sec = divmod(min,100)
      sec = 3600*hour + 60*min +sec
    time.append(sec)
  return(time)

###秒数単位
