from pytube import YouTube
import tkinter as tk # tkinter is a very baseic 2D library that lets you build graphical user interface , we are going to use to select a dicectory for the file to be saved
from tkinter import filedialog

def download_video(url , save_path):
    try:
        yt = YouTube(url) #yt captues an instance of the youtube video you want tot download
        streams = yt.streams.filter(progressive=True , file_extension = "mp4") #streams is all the places we can download the video from
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video downloaded successflully!")
    except Exception as e:
        print(e)

url = "https://www.youtube.com/watch?v=7zyq3_R1piY"
save_path = "C:\\Users\\ayush\\OneDrive\\Desktop"

download_video(url, save_path)