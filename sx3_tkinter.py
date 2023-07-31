import tkinter as tk
import pyttsx3
import tkinter.ttk as ttk

engine = pyttsx3.init()

def stopAndExit():
    root.destroy()

root = tk.Tk()
root.title("Text to Speech converter")
root.geometry("700x500")
root.configure(background="purple")

head_font = ("Monospace", 30)
text_font = ("Fancy", 22)
sm_txt_font = ("Arial", 14)

def textToSpeech():
    engine.getProperty('rate')
    engine.setProperty("rate", 9.0)
    engine.say(text_box.get('1.0', tk.END))
    engine.runAndWait()

def check_text_input(event):
    if text_box.get("1.0", tk.END).strip():
        speech_btn.config(state=tk.NORMAL, fg='purple')
    else:
        speech_btn.config(state=tk.DISABLED, fg='black')

head = tk.Label(root, text="Python's Text to Speech converter", font=head_font, fg="black", bg='purple')
head.pack(padx=10, pady=(30, 10), anchor='center')

sub_head = tk.Label(root, text="Just Enter the text and let us transform text into Speech for you", font=text_font, bg='purple', fg='grey')
sub_head.pack(padx=20, pady=(5, 15), anchor='center')

text_box = tk.Text(root, width=40, height=7, bd=2, borderwidth=4, bg='white', fg='black', name="enter your text here", font=sm_txt_font)
text_box.pack(pady=(10, 21), padx=30, anchor='center', fill="x")

text_box.bind("<KeyRelease>", check_text_input)  # Bind the text box to check_text_input function

speech_btn = tk.Button(root, text="Convert", fg="purple", bg='black', font=text_font,  command=textToSpeech, state=tk.DISABLED)
speech_btn.pack(ipadx=10, ipady=7, anchor='center')


exit_btn = tk.Button(root, text="Stop & Exit", fg="black", bg='red', font=text_font,  command=stopAndExit)
exit_btn.pack(ipadx=5, ipady=10, pady=(10, 5), anchor='center')

root.mainloop()
