from pytube import YouTube
import json
from moviepy.editor import *
from ast import literal_eval
from pprint import pprint
#import matplotlib.pyplot as plt
import glob
from pathlib import Path
import math
import collections
import numpy as np
import datetime
import time
import pprint
from retry import retry

import gui
import get_comment
import make_folder as ma

###GUI表示、youtube_urlを入力
youtube_url,word = gui.main()
#youtube_url = youtube_url

###video_idを取得
video_id = ma.make_videoid(youtube_url)
##出力
print("URL:",youtube_url,"\nvideo_id:",video_id)

##フォルダ作成
folder_name = ma.make_folder(youtube_url, path='')
##出力
print("フォルダ作成：",folder_name)

##動画ダウンロード
youtube = YouTube(youtube_url).streams.first().download(folder_name)

###コメント取得
comment_data = []
comment_data = get_comment.get_chat_replay_data(video_id)

##テキストに保存
comment_data_path = folder_name + '/' + 'コメント.txt'
with open(comment_data_path, mode='w', encoding="utf-8") as f:
  f.writelines(pprint.pformat(comment_data))

###特定の単語の頻度を抽出
word = "w|W|草|笑|すごい|!"    ##特定の単語
if word=='':
    time = ma.get_time(comment_data)
else:
    time = ma.get_word_time(comment_data, word)

###秒数の単位を指定
count = 10  #10秒ごと
time = np.array(time)
time_10 = time / count
for x in range(len(time)):
  time_10[x] = int(time_10[x]) * count
time_10co = collections.Counter(time_10)
time_10co = sorted(time_10co.items())

hilight_list = sorted(time_10co, key = lambda x:x[1], reverse=True)  ##大きい順にソート
recommend_count = 5  ##推薦個数
video_path = folder_name + '/' + folder_name +'.mp4'
for count in range(recommend_count):
    video_name = folder_name + "/ハイライト" + str(count+1) + ".mp4"
    video = VideoFileClip(video_path).subclip(int(hilight_list[count][0]-110), int(hilight_list[count][0]+10))
    video.write_videofile(video_name) #動画の書き込み
    print("ランク:", count+1, "時間:",datetime.timedelta(seconds=hilight_list[count][0]), "-", datetime.timedelta(seconds=hilight_list[count][0]+10) , "コメント数:",hilight_list[count][1] )
