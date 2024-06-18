import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import threading

class ChatAssistant(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chat Assistant")
        self.geometry("500x500")

        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        # Create a scrolled text widget for chat history
        self.chat_history = scrolledtext.ScrolledText(self, state='disabled', wrap='word')
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create an entry widget for user input
        self.user_input = tk.Entry(self)
        self.user_input.pack(padx=10, pady=10, fill=tk.X, expand=False)
        self.user_input.bind("<Return>", self.send_message)

        # Create a button to send messages
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

        # Create a button to wake the assistant
        self.wake_button = tk.Button(self, text="Wake", command=self.start_listening)
        self.wake_button.pack(padx=10, pady=10)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good Morning! ")

        elif hour >= 12 and hour < 17:
            self.speak("Good Afternoon! ")

        elif hour >= 17 and hour < 19:
            self.speak("Good Evening! ")

        else:
            self.speak("Good Night! ")

        self.speak("I am your Virtual Assistant Suzi. Please tell me how may I help you")

    tempp

    def sendEmail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail('your_email@gmail.com', to, content)
        server.close()

    def start_listening(self):
        thread = threading.Thread(target=self.main_loop)
        thread.start()

    def main_loop(self):
        self.wishMe()
        while True:
            query = self.takeCommand().lower()
            if query == "none":
                continue
            if 'wikipedia' in query:
                self.speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia")
                self.print_to_chat(results)
                self.speak(results)

            elif "hello" in query or "hello Suzi" in query:
                hello1 = "Hello ! How May I Help you.."
                self.print_to_chat(hello1)
                self.speak(hello1)

            elif "who are you" in query or "about you" in query or "your details" in query:
                who_are_you = "I am Suzi an AI based computer program but I can help you a lot like your assistant! Try giving me a simple command!"
                self.print_to_chat(who_are_you)
                self.speak(who_are_you)

            elif 'who make you' in query or 'who made you' in query or 'who created you' in query or 'who develop you' in query:
                self.speak("For your information Shrinivas Kulkarni Created me! I can show you his LinkedIn profile if you want to see. Yes or no ...")
                ans_from_user_who_made_you = self.takeCommand().lower()
                print(ans_from_user_who_made_you)
                if 'yes' in ans_from_user_who_made_you or 'ok' in ans_from_user_who_made_you or 'yeah' in ans_from_user_who_made_you:
                    webbrowser.open("https://www.linkedin.com/in/shrinivas-kulkarni-8ab593285/")
                    self.speak('Opening his profile... please wait')
                elif 'no' in ans_from_user_who_made_you or 'no thanks' in ans_from_user_who_made_you or 'not' in ans_from_user_who_made_you:
                    self.speak("All right! OK...")
                else:
                    self.speak("I can't understand. Please say that again!")

            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")
                self.speak("Opening YouTube")

            elif 'open github' in query:
                webbrowser.open("https://www.github.com")
                self.speak("Opening GitHub")

            elif 'open facebook' in query:
                webbrowser.open("https://www.facebook.com")
                self.speak("Opening Facebook")

            elif 'open instagram' in query:
                webbrowser.open("https://www.instagram.com")
                self.speak("Opening Instagram")

            elif 'open google' in query:
                webbrowser.open("google.com")
                self.speak("Opening Google")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                self.speak("Opening Stack Overflow")

            elif 'open yahoo' in query:
                webbrowser.open("https://www.yahoo.com")
                self.speak("Opening Yahoo")

            elif 'open gmail' in query:
                webbrowser.open("https://mail.google.com")
                self.speak("Opening Gmail")

            elif 'open snapdeal' in query:
                webbrowser.open("https://www.snapdeal.com")
                self.speak("Opening Snapdeal")

            elif 'open amazon' in query or 'shop online' in query:
                webbrowser.open("https://www.amazon.com")
                self.speak("Opening Amazon")

            elif 'open flipkart' in query:
                webbrowser.open("https://www.flipkart.com")
                self.speak("Opening Flipkart")

            elif 'play music' in query:
                self.speak("Ok, I am playing music")
                music_dir = 'F:\\songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'video from pc' in query or "video" in query:
                self.speak("Ok, I am playing videos")
                video_dir = 'F:\\All movies'
                videos = os.listdir(video_dir)
                os.startfile(os.path.join(video_dir, videos[0]))

            elif 'good bye' in query:
                self.speak("Good bye")
                exit()

            elif "shutdown" in query:
                self.speak("Shutting down")
                os.system('shutdown -s')

            elif "your name" in query or "sweat name" in query or "what is your name" in query:
                naa_mme = "Thanks for Asking! My name is Suzi"
                self.print_to_chat(naa_mme)
                self.speak(naa_mme)

            elif "you feeling" in query or "how you feeling" in query:
                self.print_to_chat("Feeling very happy to help you")
                self.speak("Feeling very happy to help you")

            elif 'exit' in query or 'stop' in query or 'quit' in query:
                exx_exit = 'See you soon. Bye'
                self.speak(exx_exit)
                exit()

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                self.speak(f"The time is {strTime}")

            elif 'open code' in query:
                codePath = "code"
                os.startfile(codePath)
                self.speak("Opening Visual Studio Code")

            elif 'email to the creator' in query or "email to the shrinivas" in query:
                try:
                    self.speak("What should I say?")
                    content = self.takeCommand()
                    to = "kulkarnishrinivas850@gmail.com"
                    self.sendEmail(to, content)
                    self.speak("Email has been sent!")
                except Exception as e:
                    self.print_to_chat(e)
                    self.speak("Sorry... I am not able to send this email")

            elif 'how are you' in query:
                setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
                ans_qus = random.choice(setMsgs)
                self.speak(ans_qus)
                self.speak(" How are you'")
                ans_from_user_how_are_you = self.takeCommand()
                if 'fine' in ans_from_user_how_are_you or 'happy' in ans_from_user_how_are_you or 'okey' in ans_from_user_how_are_you:
                    self.speak('Great')
                elif 'not' in ans_from_user_how_are_you or 'sad' in ans_from_user_how_are_you or 'upset' in ans_from_user_how_are_you:
                    self.speak('Tell me how can I make you happy')
                else:
                    self.speak("I can't understand. Please say that again!")

            else:
                tempp = query.replace(' ', '+')
                gurl = "https://www.google.com/search?q="
                res = 'Sorry! I can\'t understand but I will search from the internet to give your answer!'
                self.print_to_chat(res)
                self.speak(res)
                webbrowser.open(gurl + tempp)

    def send_message(self, event=None):
        user_message = self.user_input.get()
        self.print_to_chat(f"You: {user_message}")
        self.user_input.delete(0, tk.END)
        # Here you could add logic to handle the user input as needed.

    def print_to_chat(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, message + '\n')
        self.chat_history.configure(state='disabled')
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    app = ChatAssistant()
    app.mainloop()
