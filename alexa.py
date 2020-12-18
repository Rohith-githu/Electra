from lib import *
from commands import *
if __name__ == '__main__':
    # erros()
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query :
            print('searching Wikipedia.....')
            say('searching Wikipedia.....')
            query = query.replace('search wikipedia for', '')
            results = wikipedia.summary(query, sentences = 2)
            print('According to wikipedia...')
            say('According to wikipedia...')
            print(results)
            say(results)
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
            say('opening youtube for you...')
            webbrowser.open('https://www.youtube.com')
            say('yotube is opened')
            os.system('cls')
        elif 'show timeline' in query:
            recents()
            os.system('cls')
        elif 'open chrome' in query :
            print('opening chrome....')
            say('opening chrome....')
            webbrowser.open('chrome.exe')
            say('chrome is opened')
            os.system('cls')
        elif 'open edge' in query :
            print('opening msedge....')
            say('opening msedge....')
            webbrowser.open('msedge.exe')
            say('msedge is opened')
            os.system('cls')
        elif 'open firefox' in query :
            print('opening firefox....')
            say('opening firefox....')
            webbrowser.open('firefox.exe')
            say('firefox is opened')
            os.system('cls')
        elif 'open code' in query :
            print('opening code...')
            say('opening code...')
            os.startfile("C:\\Users\\rohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            say('vscode is now opened.')
            os.system('cls')
        elif 'the time' in query :
            strtime = datetime.datetime.now().strftime('%H:%M')
            print(f'the time is {strtime}')
            say(f'the time is {strtime}')
            os.system('cls')
        elif query == 'hi' :
            print('hi sir.!')
            say('hi sir.!')
            os.system('cls')
        elif query == 'hai' :
            print('hi sir.!')
            say('hi sir.!')
            os.system('cls')
        elif 'bye' in query :
            print('bye sir lets meet next time')
            say('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif query == 'bhai' :
            print('bye sir lets meet next time')
            say('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'quit' in query :
            print('bye sir lets meet next time')
            say('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'exit' in query :
            print('bye sir lets meet next time')
            say('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'close' in query :
            print('bye sir lets meet next time')
            say('bye sir lets meet next time')
            time.sleep(1)
            exit()
            os.system('cls')
        elif 'open practically' in query :
            print('opening practically...')
            say('opening practically...')
            webbrowser.open('https://www.practically.com')
            say('practically is now opened!')
            os.system('cls')
        elif 'open whatsapp' in query :
            pyautogui.hotkey('win', '5')
            os.system('cls')
        elif 'google' in query :
            print('searching Google.....')
            say('searching Google.....')
            query = query.replace('google', '')
            webbrowser.open('https://www.google.com/search?q=' + query)
            say(f'searched google for {query}')
            os.system('cls')
        elif 'youtube' in query :
            print('searching YouTube....')
            say('searching YouTube.....')
            query = query.replace('youtube', '')
            webbrowser.open('https://www.youtube.com/results?search_query=' + query)
            say(f'Youtube google for {query}')
            os.system('cls')
        elif 'stack overflow' in query :
            print('searching stackoverflow.....')
            say('searching stackoverflow.....')
            query = query.replace('stack overflow', '')
            webbrowser.open('https://stackoverflow.com/search?q=' + query)
            say(f'searched stackoverflow for {query}')
            os.system('cls')
        elif 'stackoverflow' in query :
            print('searching stackoverflow.....')
            say('searching stackoverflow.....')
            query = query.replace('stackoverflow', '')
            webbrowser.open('https://stackoverflow.com/search?q=' + query)
            say(f'searched stackoverflow for {query}')
            os.system('cls')
        elif 'brainly' in query :
            print('searching brainly.....')
            say('searching brainly.....')
            query = query.replace('brainly', '')
            webbrowser.open('https://brainly.in/app/ask?entry=hero&q=' + query)
            say(f'searched brainly for {query}')
            os.system('cls')
        elif 'quora' in query :
            print('searching quora.....')
            say('searching quora.....')
            query = query.replace('quora', '')
            webbrowser.open('https://www.quora.com/search?q=' + query)
            say(f'searched quora for {query}')
            os.system('cls')
        elif 'github' in query :
            print('searching github.....')
            say('searching github')
            query = query.replace('github', '')
            webbrowser.open('https://github.com/search?q=' + query)
            say(f'searched github for {query}')
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
            say('starting repository creator')
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