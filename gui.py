import PySimpleGUI as sg
import sys
from pytube import YouTube

def main():
    ###ウインドウテーマ
    sg.theme('Topanga')
    ###レイアウト
    layout = [
            [sg.Text('YouTube ハイライト作成',text_color ='white', size=(25, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE ,pad=((20,20),(20,0)))],
            [sg.Text('概要',font=('',18),size=(12,1))],
            [sg.Text("",size=(1, 2)),sg.Text('　YouTubeLiveのアーカイブからコメント情報を取得し、\n　その動画のハイライトを作成します。',text_color ='white',
            size=(45, 2), relief=sg.RELIEF_RIDGE)],
            [sg.Text('YouTube URL:',size=(12,1),justification='right'),sg.Input("", key='youtube_url' ,size=(50,1))],
            [sg.Text('特定の単語:',size=(12,1),justification='right'),sg.Input("w|W|草|笑|すごい|!", key='word' ,size=(50,1))],
            [sg.Button('作成', size=(5,1)),sg.Button('終了', size=(5,1)),sg.Text('',key='-出力-',size=(30,1))],
            ]

    window = sg.Window('ハイライト', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (None,'終了'):
            sys.exit()
        elif event in ('作成'):
            try:
                YouTube(values['youtube_url'])
                break
            except:
                window['-出力-'].update('正しく入力できてません。',font=('',18))
    ###ウインドウ削除
    window.close()
    return(values['youtube_url'],values['word'])
