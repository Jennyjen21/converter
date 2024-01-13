import os
import tkinter as tk
from tkinter import messagebox, colorchooser
from pytube import YouTube
import customtkinter as ctk

# Initialize the root variable as a Tk instance
root = tk.Tk()

# System Settings Frame
def open_color_picker():
  color = colorchooser.askcolor()
  if color:
      root['bg'] = color[1]

system_settings_frame = tk.Frame(root)
system_settings_frame.pack(side='top', fill='x')

theme_label = ctk.CTkLabel(system_settings_frame, text='Theme:')
theme_label.pack(side='left')

change_theme_button = ctk.CTkButton(system_settings_frame, text='Change Theme', command=open_color_picker)
change_theme_button.pack(side='left')

# App Frame
app_frame = ctk.CTkFrame(root, width=400, height=200)
app_frame.place(relx=0.5, rely=0.5, anchor='center')

label = ctk.CTkLabel(app_frame, text='Enter YouTube URL:')
label.pack()

url_input = ctk.CTkEntry(app_frame, width=50)
url_input.pack()

def download_video():
  try:
      url = url_input.get()
      YouTube(url).streams.first().download(output_path='.')
      messagebox.showinfo('Success', 'Video Downloaded Successfully!')
  except Exception as e:
      messagebox.showerror('Error', str(e))

download_button = ctk.CTkButton(app_frame, text='Download Video', command=download_video)
download_button.pack()

def convert_to_mp3():
  try:
      video_files = [file for file in os.listdir('.') if file.endswith('.mp4')]
      if not video_files:
          messagebox.showerror('Error', 'No Video Files Found!')
          return
      video_file = video_files[0]
      mp3_file = video_file.replace('.mp4', '.mp3')
      os.system(f'ffmpeg -i {video_file} -vn -ab 128k -ar 44100 -y {mp3_file}')
      os.remove(video_file)
      messagebox.showinfo('Success', 'Video Converted to MP3 Successfully!')
  except Exception as e:
      messagebox.showerror('Error', str(e))

convert_button = ctk.CTkButton(app_frame, text='Convert to MP3', command=convert_to_mp3)
convert_button.pack()

root.mainloop()
