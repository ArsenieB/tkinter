from pytube import YouTube
from tkinter import Tk, Label, Entry, Button, messagebox

def download_video():
    url = entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams(only_audio=True).first() # Doar audio
        stream.download(output_path="downloads").filter
        messagebox.showinfo("Succes", "Descarcarea a fost finalizata!")
    except Exception as e:
        messagebox.showerror("Eroare", f"A aparut o eroare: {e}")

# Interfata grafica
app = Tk()
app.title("YouTube Video Downloader")
app.geometry("400x150")

Label(app, text="Introdu URL-ul videoclipului:").pack(pady=10)
entry = Entry(app, width=40)
entry.pack(pady=10)

Button(app, text="Descarca", command=download_video).pack(pady=10)
app.mainloop()
