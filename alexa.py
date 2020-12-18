from lib import *
from commands import *
if __name__ == '__main__':
    # erros()
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query :
            print('searching Wikipedia.....')
            speak('searching Wikipedia.....')
            query = query.replace('search wikipedia for', '')
            results = wikipedia.summary(query, sentences = 2)
            print('According to wikipedia...')
            speak('According to wikipedia...')
            print(results)
            speak(results)
            os.system('cls')
        elif 'witch window' in query:
            switch_windows()
            os.system('cls')
        elif 'witch tab' in query:
            switch_tab()
            os.system('cls')
        elif 'notification' in query:
            notifications()
            os.system('cls')
        elif 'close window' in query:
            close_window()
            os.system('cls')
        elif 'unmute' in query :
            unmute()
            os.system('cls')
        elif 'open start' in query :
            menu()
        elif 'open search' in query :
            menusearch()
        elif 'open youtube' in query :
            print('opening youtube...')
            speak('opening youtube for you...')
            webbrowser.open('https://www.youtube.com')
            speak('yotube is opened')
            os.system('cls')
        elif 'show timeline' in query:
            recents()
            os.system('cls')
        elif 'open chrome' in query :
            print('opening chrome....')
            speak('opening chrome....')
            webbrowser.open('chrome.exe')
            speak('chrome is opened')
            os.system('cls')
        elif 'open edge' in query :
            print('opening msedge....')
            speak('opening msedge....')
            webbrowser.open('msedge.exe')
            speak('msedge is opened')
            os.system('cls')
        elif 'open firefox' in query :
            print('opening firefox....')
            speak('opening firefox....')
            webbrowser.open('firefox.exe')
            speak('firefox is opened')
            os.system('cls')
        elif 'open code' in query :
            print('opening code...')
            speak('opening code...')
            os.startfile("C:\\Users\\rohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak('vscode is now opened.')
            os.system('cls')
        elif 'the time' in query :
            strtime = datetime.datetime.now().strftime('%H:%M')
            print(f'the time is {strtime}')
            speak(f'the time is {strtime}')
            os.system('cls')
        elif query == 'hi' :
            print('hi sir.!')
            speak('hi sir.!')
            os.system('cls')
        elif query == 'hai' :
            print('hi sir.!')
            speak('hi sir.!')
            os.system('cls')
        elif 'bye' in query :
            print('bye sir lets meet next time')
            speak('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif query == 'bhai' :
            print('bye sir lets meet next time')
            speak('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'quit' in query :
            print('bye sir lets meet next time')
            speak('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'exit' in query :
            print('bye sir lets meet next time')
            speak('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'close' in query :
            print('bye sir lets meet next time')
            speak('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'open practically' in query :
            print('opening practically...')
            speak('opening practically...')
            webbrowser.open('https://www.practically.com')
            speak('practically is now opened!')
            os.system('cls')
        elif 'open whatsapp' in query :
            print('opening whatsapp...')
            speak('opening whatsapp...')
            webbrowser.open('https://web.whatsapp.com')
            speak('whatsapp is now opened!')
            os.system('cls')
        elif 'google' in query :
            print('searching Google.....')
            speak('searching Google.....')
            query = query.replace('google', '')
            webbrowser.open('https://www.google.com/search?q=' + query)
            speak(f'searched google for {query}')
            os.system('cls')
        elif 'youtube' in query :
            print('searching YouTube....')
            speak('searching YouTube.....')
            query = query.replace('youtube', '')
            webbrowser.open('https://www.youtube.com/results?search_query=' + query)
            speak(f'Youtube google for {query}')
            os.system('cls')
        elif 'stack overflow' in query :
            print('searching stackoverflow.....')
            speak('searching stackoverflow.....')
            query = query.replace('stack overflow', '')
            webbrowser.open('https://stackoverflow.com/search?q=' + query)
            speak(f'searched stackoverflow for {query}')
            os.system('cls')
        elif 'stackoverflow' in query :
            print('searching stackoverflow.....')
            speak('searching stackoverflow.....')
            query = query.replace('stackoverflow', '')
            webbrowser.open('https://stackoverflow.com/search?q=' + query)
            speak(f'searched stackoverflow for {query}')
            os.system('cls')
        elif 'brainly' in query :
            print('searching brainly.....')
            speak('searching brainly.....')
            query = query.replace('brainly', '')
            webbrowser.open('https://brainly.in/app/ask?entry=hero&q=' + query)
            speak(f'searched brainly for {query}')
            os.system('cls')
        elif 'quora' in query :
            print('searching quora.....')
            speak('searching quora.....')
            query = query.replace('quora', '')
            webbrowser.open('https://www.quora.com/search?q=' + query)
            speak(f'searched quora for {query}')
            os.system('cls')
        elif 'github' in query :
            print('searching github.....')
            speak('searching github')
            query = query.replace('github', '')
            webbrowser.open('https://github.com/search?q=' + query)
            speak(f'searched github for {query}')
            os.system('cls')
        elif 'open zoom' in query :
            sp('opening zoom...')
            os.startfile('C:\\Users\\rohit.ANUMALASETTY\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
            os.system('cls')
        elif 'what\'s your name' in query :
            sp('I dont have a name but i work for Rohith')
            os.system('cls')
        elif 'what are you doing' in query :
            import random
            choices1 = ['I am checking for bugs in my code to get you experienced more','I am looking for new features to get more developed','I am checking the code bugs while opening apps, you can also open apps with help of me']
            sp(random.choice(choices1))
            os.system('cls')
        elif 'what can you do' in query :
            sp('I can open apps, and serach google,brainly,youtube,stackoverlow,quora,github for you, and get results from wikipedia. and there are many features going to be added in me')
            os.system('cls')
        elif 'game' in query :
            sp('opening the numberguessing game')
            game()
            os.system('cls')
        elif 'join practically' in query :
            practically.join_practically()
            os.system('cls')
        elif 'instant meet' in query :
            os.startfile('meet_automate.py')
            os.system('cls')
        elif 'refresh the web page' in query :
            refresh_web_page()
            os.system('cls')
        elif 'open explorer' in query :
            webbrowser.open('c://users/rohith')
            os.system('cls')
        elif "create a repo" in query :
            speak('starting repository creator')
            os.startfile('github_repository_create.py')
            os.system('cls')
        elif 'play' in query :
            query = query.replace('play', '')
            pywhatkit.playonyt(query)
            sp(f'started playing {query} on youtube')
            os.system('cls')
        elif 'thank' in query :
            sp('that\'s ok')
        else :
            time.sleep(1)
            os.system('cls')