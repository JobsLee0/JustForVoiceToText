import threading
import tkinter as tk
from tkinter import filedialog

from client.client import Client


class _Gui(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('JustForVoiceToText')

        self.text_area = tk.Text(self.root, height=30, width=100)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.file_path_var = tk.StringVar()
        self.file_path_entry = tk.Entry(self.frame, textvariable=self.file_path_var, state='readonly')
        self.file_path_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.upload_button = tk.Button(self.frame, text='选择文件', command=self.select_and_trans)
        self.upload_button.pack(side=tk.LEFT)

        self.status_label = tk.Label(self.root, text='')
        self.status_label.pack()

    def update_text_area(self, result):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def select_and_trans(self):
        audio_filetypes = [
            ('All supported audio files', '*.mp3;*.wav;*.ogg;*.flac;*.m4a'),
            ('MP3 files', '*.mp3'),
            ('WAV files', '*.wav'),
            ('OGG files', '*.ogg'),
            ('FLAC files', '*.flac'),
            ('M4A files', '*.m4a')
        ]
        file_path = filedialog.askopenfilename(
            title='选择音频文件',
            filetypes=audio_filetypes
        )
        if file_path:
            self.file_path_var.set(file_path)
            self.status_label.config(text='正在转译，请耐心等待…')

            # loading = True

            def thread_trans():
                try:
                    result = self.trans.request(file_path)
                except Exception:
                    result = '转译异常'
                    print('转译异常')
                # 更新主线程的文本域
                self.update_text_area(result)
                self.status_label.config(text='转译完成！')
                # loading = False

            thread = threading.Thread(target=thread_trans)
            thread.start()


gui = _Gui()


def start(trans: Client):
    gui.trans = trans
    gui.root.mainloop()
