import pytube
import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
#pytube patch: python -m pip install git+https://github.com/Zeecka/pytube@fix_1060
#cipher.py workaround: https://stackoverflow.com/questions/68945080/pytube-exceptions-regexmatcherror-get-throttling-function-name-could-not-find

window = tk.Tk()
window.title("Youtube to mp3")

disclaimer = tk.Label(text="(more features coming later)")
disclaimer.pack() #add to window

prompt = tk.Label(text="Paste a YT link: ")
prompt.pack()

#link field
entry = tk.Entry(fg="black", bg="white", width=50)
entry.pack()   

prompt2 = tk.Label(text="Choose download location (optional): ")
prompt2.pack()
entry2 = tk.Entry(fg="black", bg="white", width=50)
entry2.pack()

convert = tk.Button(
    window,
    text="Convert to mp3",
    width=25,
    #height=5,
    bg="white",
    fg="blue",
    command = lambda: func("clicked")
    )
convert.pack()

#after button press
def func(args):
    #entry.delete(0,32)
    download_path = "."
    pathname = entry2.get()
    #print(pathname)
    if pathname != "":
        download_path = pathname
        #print(download_path)
    link = entry.get() #get text, assign to var link
    #print(link)
    yt = pytube.YouTube(link)#.streams.first().download()
    stream = yt.streams.filter(only_audio=True).first()#get_by_itag(140)
    outfile = stream.download(output_path=download_path)
    base, ext = os.path.splitext(outfile)
    newfile = base + '.mp3'
    os.rename(outfile, newfile)
    success = tk.Label(text=yt.title + "success!").pack()

"""
    if sys.platform == 'win32':
        subprocess.Popen('explorer "C:\Downloads"') #Windows
    else:
        subprocess.call(["open", "-R", "/Downloads"]) #darwin/MacOS
"""    

window.mainloop()


