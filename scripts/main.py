import tkinter
from tkVideoPlayer import TkinterVideo



def launch_video():
    window = tkinter.Tk()
    window.title("game.exe")
    window.geometry("568x320")
    window.aspect(568, 320, 568, 320)

    videoplayer = TkinterVideo(master=window, scaled=True)
    videoplayer.load("video/Video.mov")
    videoplayer.pack(expand=True, fill="both")

    def video_pause(e):
        if videoplayer.is_paused():
            videoplayer.play()
        else:
            videoplayer.pause()
    
    screenState = False
    window.attributes("-fullscreen", screenState)

    def video_escape(e):
        if screenState:
            screenState = False
        else:
            screenState = True
        window.attributes("-fullscreen", screenState)

    def video_resize(e):
        if(e.widget == window.toplevel) and ((window.width != e.width) or (window.height != e.height)):
            videoplayer.set_size((e.width, e.height), True)

    window.bind("<space>", video_pause)
    window.bind("<Escape>", video_escape)

    videoplayer.play()
    def loop(e):
        videoplayer.play()

    videoplayer.bind("<<Ended>>", loop)

    window.mainloop()


if __name__ == "__main__":
    launch_video()