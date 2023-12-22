import subprocess
import tkinter as tk

stop_process = 'no'  # Assuming you have defined stop_process somewhere
git_commit_push_count = 0  # Assuming you have defined git_commit_push_count somewhere
seconds_intervals = 1000  # Adjust this interval as needed

app = tk.Tk()
STATUS = tk.Label(app, text="")
STATUS.pack()

output_text = tk.Text(app, height=10, width=50)
output_text.pack()

def has_changes():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error checking Git status: {e}")
        return False

def git_commit_push():
    global stop_process, git_commit_push_count, STATUS, app
    if stop_process != 'yes':
        git_directory = "C:\Users\HEZRON WEKESA\Desktop\python Project\git_Commit_App\Auto_git_commit_push"
        if has_changes():
            try:
                # Redirect subprocess output
                result_add = subprocess.run(["git", "add", "--all"], cwd=git_directory, capture_output=True, text=True, check=True)
                result_commit = subprocess.run(["git", "commit", "-m", "Your commit message"], cwd=git_directory, capture_output=True, text=True, check=True)
                result_push = subprocess.run(["git", "push"], cwd=git_directory, capture_output=True, text=True, check=True)

                # Display output in Tkinter Text widget
                output_text.insert(tk.END, f"git add:\n{result_add.stdout}\n\n")
                output_text.insert(tk.END, f"git commit:\n{result_commit.stdout}\n\n")
                output_text.insert(tk.END, f"git push:\n{result_push.stdout}\n\n")

                git_commit_push_count += 1
                STATUS.config(text=f'Committed and Pushed made: {git_commit_push_count} ')
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
