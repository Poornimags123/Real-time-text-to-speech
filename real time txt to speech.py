import os
import tkinter as tk
from gtts import gTTS
 
def speak(text):
    obj=gTTS(text=text,lang='en')
    path="speech.mp3"

    if os.path.exists(path):
        os.remove(path)
    
    obj.save(path)
    os.system(f"start{path}")

def converter():
    input=text.get()
    speak(input)

root = tk.Tk()
root.title("Real-time text to speech converter")

text=tk.Entry(root,width=100)
text.pack(pady=50)

convert_button = tk.Button(root, text="Convert to speech", command=converter)
convert_button.pack(pady=20)
 
root.mainloop()
