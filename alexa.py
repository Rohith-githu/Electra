from lib import *
from commands import *
wake_words = ['Alexa', 'elaxa', 'hey', 'hi alexa', 'lexa', 'okay', 'ok','computers','help', 'bored', 'wake']
if __name__ == '__main__':
    # erros()
    wishme()
    while True:
        query = takeCommand().lower()
        if 'alexa' in query:
            say('How can i help you?')
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
            elif 'which window' in query:
                switch_windows()
                os.system('cls')
            elif 'which tab' in query:
                switch_tab()
                os.system('cls')
            elif 'write' in query:
                confirm = takeCommand().lower()
                write(confirm)
            elif 'new tab' in query:
                new_tab()
            elif 'notification' in query:
                notifications()
                os.system('cls')
            elif 'close window' in query:
                close_window()
                os.system('cls')
            elif 'unmute' in query :
                unmute()
            elif 'open start' in query :
                menu()
            elif 'open search' in query :
                menusearch()
            elif 'incignito mode' in query :
                incignito()
            elif 'open youtube' in query :
                webbrowser.open('https://www.youtube.com')
                os.system('cls')
            elif 'show timeline' in query:
                recents()
                os.system('cls')
            elif 'minimize all' in query:
                minimize()
                os.system('cls')
            elif 'open pie chart' in query :
                os.startfile(r"C:\Users\rohit\AppData\Local\pycharm\bin\pycharm64.exe")
                os.system('cls')
            elif 'open chrome' in query :
                webbrowser.open('chrome.exe')
                os.system('cls')
            elif 'open edge' in query :
                webbrowser.open('msedge.exe')
                os.system('cls')
            elif 'open firefox' in query :
                webbrowser.open('firefox.exe')
                os.system('cls')
            elif 'open code' in query :
                os.startfile("C:\\Users\\rohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                os.system('cls')
            elif 'open studio' in query :
                webbrowser.open('https://studio.youtube.com/')
            elif 'click' in query :
                click_on_screen()
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
            elif 'open practically' in query :
                webbrowser.open('https://www.practically.com')
                os.system('cls')
            elif 'open whatsapp' in query :
                pyautogui.hotkey('win', '5')
                os.system('cls')
            elif 'google' in query :
                query = query.replace('google', '')
                webbrowser.open('https://www.google.com/search?q=' + query)
                os.system('cls')
            elif 'youtube' in query :
                query = query.replace('youtube', '')
                webbrowser.open('https://www.youtube.com/results?search_query=' + query)
                os.system('cls')
            elif 'stack overflow' in query :
                query = query.replace('stack overflow', '')
                webbrowser.open('https://stackoverflow.com/search?q=' + query)
                os.system('cls')
            elif 'stackoverflow' in query :
                query = query.replace('stackoverflow', '')
                webbrowser.open('https://stackoverflow.com/search?q=' + query)
                os.system('cls')
            elif 'brainly' in query :
                query = query.replace('brainly', '')
                webbrowser.open('https://brainly.in/app/ask?entry=hero&q=' + query)
                os.system('cls')
            elif 'quora' in query :
                query = query.replace('quora', '')
                webbrowser.open('https://www.quora.com/search?q=' + query)
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
                practically()
                os.system('cls')
            elif 'john practically' in query :
                practically()
                os.system('cls')
            elif 'instant meet' in query :
                os.startfile('meet_automate.py')
                os.system('cls')
            elif 'refresh' in query :
                refresh_web_page()
                os.system('cls')
            elif 'open explorer' in query :
                webbrowser.open('explorer.exe')
                os.system('cls')
            elif "create a repo" in query :
                say('starting repository creator')
                os.startfile('github_repository_create.py')
                os.system('cls')
            elif 'play' in query :
                query = query.replace('play', '')
                pywhatkit.playonyt(query)
                os.system('cls')
            elif 'thank' in query :
                sp('that\'s ok')
            elif 'shutdown my pc' in query :
                shutdown()
            elif 'restart my pc' in query :
                restart()
            elif 'full screen' in query :
                full()
            elif 'shutdown my pc' in query :
                shutdown()
            elif 'shut down my pc' in query:
                shutdown()
            elif 'restart my pc' in query :
                restart()
            elif 'lock me' in query :
                lock()
                os.system('cls')
            elif 'sleep my pc' in query :
                sleep()
            elif 'leave meet' in query :
                pyautogui.hotkey('alt','f4')
                pyautogui.press('enter')
            elif 'screenshot' in query :
                pyautogui.screenshot()
            else :
                os.system('cls')
        elif 'minimize all' in query:
            minimize()
            os.system('cls')
        elif 'wich window' in query :
            switch_windows()
        elif 'which tab' in query:
            switch_tab()
            os.system('cls')
        elif 'write' in query:
            confirm = takeCommand().lower()
            write(confirm)
        elif 'new tab' in query:
            new_tab()
        elif 'notification' in query:
            notifications()
            os.system('cls')
        elif 'close window' in query:
            close_window()
            os.system('cls')
        elif 'unmute' in query :
            unmute()
        elif 'open start' in query :
            menu()
        else:
            pass