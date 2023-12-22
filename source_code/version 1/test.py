import subprocess
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

stop_process = 'no'  # Assuming you have defined stop_process somewhere
git_commit_push_count = 0  # Assuming you have defined git_commit_push_count somewhere
seconds_intervals = 1000  # Adjust this interval as needed

app = tk.Tk()
STATUS = tk.Label(app, text="")
STATUS.pack()

# Create a Text widget to display the terminal output
terminal_output = ScrolledText(app, height=10, width=50)
terminal_output.pack()


def has_changes():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error checking Git status: {e}")
        return False


def git_commit_push():
    global stop_process, git_commit_push_count, STATUS, app, terminal_output
    if stop_process != 'yes':
        if has_changes():
            try:
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "Your commit message"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                git_commit_push_count += 1
                STATUS.config(text=f'Committed and Pushed made: {git_commit_push_count} ')

                # Display the output in the Text widget
                terminal_output.insert(tk.END, process.stdout.read())

                print(seconds_intervals)
                app.after(seconds_intervals, git_commit_push)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
                # Handle the error as needed
        else:
            print("No changes to commit and push.")
            app.after(seconds_intervals, git_commit_push)


# Call the function to start the process
git_commit_push()

app.mainloop()
