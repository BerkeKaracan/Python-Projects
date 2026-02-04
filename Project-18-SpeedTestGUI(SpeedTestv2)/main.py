import tkinter as tk
import speedtest
from tkinter import messagebox
def SpeedTest():
    start.config(text="Ölçülüyor...", state="disabled")
    menu.update()
    try:
        test = speedtest.Speedtest(secure=True)
        mssg1.config(text="Searching for server...")
        menu.update()
        test.get_best_server()
        mssg2.config(text="Measuring download speed...")
        menu.update()
        download_speed = test.download()
        mssg3.config(text="Measuring upload speed...")
        menu.update()
        upload_speed = test.upload()
        ping = test.results.ping
        down_speed.config(text=f"Download Speed: {(download_speed/1024/1024):.2f} Mbps")
        upl_speed.config(text=f"Upload Speed: {(upload_speed/1024/1024):.2f} Mbps")    
        ping_value.config(text=f"Ping : {ping} ms")
        mssg1.config(text="Test Completed.",fg="green")
        mssg2.config(text="")
        mssg3.config(text="")
    except Exception as e:
        mssg1.config(text="Something went wrong!", fg="red")
        messagebox.showerror("Error", f"Connection error: {e}")
    finally:
        start.config(text="Start Test", state="normal")
menu = tk.Tk()
menu.title("Speed Test v2")
menu.geometry("300x400")
title = tk.Label(menu,text="SpeedTest")
title.pack(pady=5)
mssg1 = tk.Label(menu,text="")
mssg1.pack(pady=5)
mssg2 = tk.Label(menu,text="")
mssg2.pack(pady=5)
mssg3 = tk.Label(menu,text="")
mssg3.pack(pady=5)
down_speed = tk.Label(menu,text="Download Speed:")
down_speed.pack(pady=5)
upl_speed = tk.Label(menu,text="Upload Speed:")
upl_speed.pack(pady=5)
ping_value = tk.Label(menu,text="Ping:")
ping_value.pack(pady=5)
start = tk.Button(menu,text="Start Test",command=SpeedTest)
start.pack(pady=5)

menu.mainloop()

