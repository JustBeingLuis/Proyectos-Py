from pytube import YouTube
import os
import tkinter
import customtkinter

download_folder=os.path.join(os.path.expanduser('~'), 'Downloads')

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download(download_folder)
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text=" Youtube link is invalid ", text_color="red")

def on_progress(stream, chunck, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completition = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completition))
    pPercentage.configure(text=per + "%")
    pPercentage.update()
    
    #Update progress bar
    progressBar.set(float(percentage_of_completition) / 100)
    progressBar.update()
    

#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title(" Youtube Downloader ")

#Adding UI Elements
title = customtkinter.CTkLabel(app,text="Insert a YoutubeL Link")
title.pack(padx=10,pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=20, textvariable=url_var)
link.pack()

#Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress Button
pPercentage= customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10,pady=10)
#Run app 
app.mainloop()
