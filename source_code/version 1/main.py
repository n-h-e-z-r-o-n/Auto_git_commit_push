# Owner: Nangulu Hezron Wekesa
# Phone: +254714415034

import os
import tkinter as tk
import webbrowser
import requests

global PATH_ENTRY, STATUS, TIME_INTERVAL, app, bat_file_c, seconds_intervals, STATUS_2, stop_process
git_commit_push_count = 1


def bat_file_create(file_path):
    with open("auto_git.bat", "w") as f:
        f.write(f"cd {file_path}\n")
        f.write("git add --all\n")
        f.write('git commit -m "Committed %date:~-4%%date:~3,2%%date:~0,2%.%time:~0,2%%time:~3,2%%time:~6,2%"\n')
        #f.write('git push\n')
        f.write('exit\n')
    return "auto_git.bat"


def show_about():
    webbrowser.open('https://github.com/Hezron26/Auto_git_commit_push')


def support_info():
    webbrowser.open('https://www.buymeacoffee.com/hezronna')


def change_bg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


def change_fg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
    button.bind("<Enter>", func=lambda e: button.config(fg=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(fg=colorOnLeave))


def validate_int(input):
    if input.isdigit():
        return True
    elif input == "" or input.startswith("-") and input[1:].isdigit():
        return True
    else:
        return False


def git_comit_push():
    global stop_process
    if stop_process != 'yes':
        global git_commit_push_count, STATUS, app, app
        os.system(bat_file_c)
        STATUS.config(text=f'Committed and Pushed made: {git_commit_push_count} ')
        git_commit_push_count += 1
        print(seconds_intervals)
        app.after(seconds_intervals, git_comit_push)


def stop():
    global stop_process
    stop_process = 'yes'
    STATUS_2.config(text="Process Stopped....", fg='blue')


def start():
    global app, bat_file_c, seconds_intervals, STATUS_2, stop_process
    stop_process = 'no'
    if PATH_ENTRY.get() != "" and TIME_INTERVAL.get() != "":
        STATUS.config(text='')
        # C:/Users/HEZRON WEKESA/Desktop/python Project/Compiler Build/Compiler
        file_path = "C:/Users/HEZRON WEKESA/Desktop/python Project/Compiler Build/Compiler"
        #file_path = PATH_ENTRY.get()
        if os.path.exists(file_path):
            time = int(TIME_INTERVAL.get())
            STATUS.config(fg='green', text=f'Will auto comit and push after Every {time} minute')
            seconds_intervals = time * 60 * 1000
            bat_file_c = bat_file_create(file_path)
            STATUS_2.config(text="RUNNING....", fg='green')
            app.after(1000, git_comit_push)
        else:
            STATUS.config(text='ERROR : directory does not exist, check the path ')
    else:
        STATUS.config(text="ERROR: fill both entry's, (git directory path) and (time interval in minutes)", fg='red')


def download_app_icon():
    url = "https://raw.githubusercontent.com/Hezron26/assets/main/panda.ico"
    filename = 'panda.ico'
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def main():
    global PATH_ENTRY, STATUS, TIME_INTERVAL, app, STATUS_2
    bg_color = "pink"

    app = tk.Tk()
    #app.minsize(650, 200)
    app.minsize(850, 400)
    app.title('Auto - Git')
    # app.attributes("-toolwindow", 1)
    # app.attributes("-topmost", 1)

    try:
        app.iconbitmap("panda.ico")
    except:
        download_app_icon()
        try:
             app.iconbitmap("panda.ico")
        except:
            pass

    on_c = '#EEDC82'
    of_c = '#FFF8DC'

    PATH_lABALE = tk.Label(app, text='PATH :', font=("Courier New", 11), anchor='e', borderwidth=0, border=0)
    PATH_lABALE.place(relx=0.01, rely=0.1, relheight=0.13, relwidth=0.15)

    PATH_ENTRY = tk.Entry(app, bg=of_c, borderwidth=0, border=0)
    PATH_ENTRY.place(relx=0.17, rely=0.1, relheight=0.13, relwidth=0.8)
    change_bg_OnHover(PATH_ENTRY, on_c, of_c)

    TIME_RANGE = tk.Label(app, text='TIME(min):', font=("Courier New", 10), anchor='e', borderwidth=0, border=0)
    TIME_RANGE.place(relx=0.01, rely=0.26, relheight=0.13, relwidth=0.15)

    validation = app.register(validate_int)  # create a validation function that only allows integers
    TIME_INTERVAL = tk.Entry(app, bg=of_c, borderwidth=0, border=0, validate="key", validatecommand=(validation, "%P"))
    TIME_INTERVAL.place(relx=0.17, rely=0.26, relheight=0.13, relwidth=0.8)
    change_bg_OnHover(TIME_INTERVAL, on_c, of_c)

    STATUS = tk.Label(app, font=("Calibri", 10), anchor='w', borderwidth=0, border=0)
    STATUS.place(relx=0.17, rely=0.46, relheight=0.13, relwidth=0.8)


    STATUS_2 = tk.Label(app, font=("Courier New", 12), anchor='w', borderwidth=0, border=0)
    STATUS_2.place(relx=0.17, rely=0.60, relheight=0.13, relwidth=0.8)

    START_B = tk.Button(app, text='START', bg='#F5F5F5', borderwidth=0, border=0, command=start, font=("Courier New", 11))
    START_B.place(relx=0.4, rely=0.86, relheight=0.13, relwidth=0.12)
    change_bg_OnHover(START_B, '#EEEEFF', '#F5F5F5')

    STOP_B = tk.Button(app, text='STOP', bg='#F5F5F5', borderwidth=0, border=0, command=stop, font=("Courier New", 11))
    STOP_B.place(relx=0.53, rely=0.86, relheight=0.13, relwidth=0.12)
    change_bg_OnHover(STOP_B, '#EEEEFF', '#F5F5F5')

    SUPPORT = tk.Button(app, text='support', activeforeground='red', anchor='sw', font=("Courier New italic", 8), borderwidth=0, border=0, command=support_info)
    SUPPORT.place(relx=0.274, rely=0.86, relheight=0.13, relwidth=0.12)
    change_fg_OnHover(SUPPORT, 'red', 'black')

    TERMINAL = tk.Button(app, text='terminal', activeforeground='red', anchor='sw', font=("Courier New italic", 8), borderwidth=0, border=0)
    TERMINAL.place(relx=0.14, rely=0.86, relheight=0.13, relwidth=0.12)
    change_fg_OnHover(TERMINAL, 'red', 'black')

    ABOUT = tk.Button(app, text='about', activeforeground='red', anchor='sw', font=("Courier New italic", 8), borderwidth=0, border=0, command=show_about)
    ABOUT.place(relx=0.01, rely=0.86, relheight=0.13, relwidth=0.12)
    change_fg_OnHover(ABOUT, 'red', 'black')

    app.mainloop()


if __name__ == "__main__":
    main()
