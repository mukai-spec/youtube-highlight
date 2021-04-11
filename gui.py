import PySimpleGUI as sg

def main():
    ###ウインドウテーマ
    sg.theme('Topanga')
    ###レイアウト
    layout = [
            [sg.Text('YouTube ハイライト作成',text_color ='white', size=(25, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE ,pad=((20,20),(20,0)))],
            [sg.Text('概要',size=(12,1))],
            [sg.Text("",size=(1, 2)),sg.Text('　YouTubeLiveのアーカイブからコメント情報を取得し、\n　その動画のハイライトを作成します。',text_color ='white', size=(45, 2), relief=sg.RELIEF_RIDGE)],
            [sg.Text('YouTube URL:',size=(12,1),justification='right'),sg.Input("", key='youtube_url' ,size=(50,1))],
            [sg.Button('作成', size=(5,1)),sg.Button('終了', size=(5,1))]
            ]

    window = sg.Window('ハイライト', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (None, '作成','終了'):
            break
    ###ウインドウ削除
    window.close()
    return(values['youtube_url'])
