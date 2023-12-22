import subprocess
import tkinter as tk

stop_process = 'no'  # Assuming you have defined stop_process somewhere
git_commit_push_count = 0  # Assuming you have defined git_commit_push_count somewhere
seconds_intervals = 1000  # Adjust this interval as needed

# Specify the directory where you want to perform Git operations
git_directory = "/path/to/your/git/directory"

app = tk.Tk()
STATUS = tk.Label(app, text="")
STATUS.pack()

output_text = tk.Text(app, height=10, width=50, state=tk.DISABLED)
output_text.pack()

# Define a global variable to store the Popen object
git_process = None

def has_changes():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], cwd=git_directory, capture_output=True, text=True, check=True)
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error checking Git status: {e}")
        return False

def enable_text_widget():
    output_text.config(state=tk.NORMAL)

def disable_text_widget():
    output_text.config(state=tk.DISABLED)

def git_commit_push():
    global stop_process, git_commit_push_count, STATUS, app, git_process
    if stop_process != 'yes':
        if has_changes():
            try:
                enable_text_widget()  # Enable text widget
                # Redirect subprocess output
                git_process = subprocess.Popen(["git", "add", "--all"], cwd=git_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                result_add, _ = git_process.communicate()
                git_process = subprocess.Popen(["git", "commit", "-m", "Your commit message"], cwd=git_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                result_commit, _ = git_process.communicate()
                git_process = subprocess.Popen(["git", "push"], cwd=git_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                result_push, _ = git_process.communicate()

                # Display output in Tkinter Text widget
                output_text.insert(tk.END, f"git add:\n{result_add}\n\n")
                output_text.insert(tk.END, f"git commit:\n{result_commit}\n\n")
                output_text.insert(tk.END, f"git push:\n{result_push}\n\n")

                git_commit_push_count += 1
                STATUS.config(text=f'Committed and Pushed made: {git_commit_push_count} ')
                print(seconds_intervals)
                app.after(seconds_intervals, git_commit_push)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
                # Handle the error as needed
            finally:
                disable_text_widget()  # Disable text widget after processing
        else:
            print("No changes to commit and push.")
            app.after(seconds_intervals, git_commit_push)

# Function to terminate the subprocess
def terminate_subprocess():
    global git_process
    if git_process:
        git_process.terminate()

# Call the function to start the process
git_commit_push()

# You can call the terminate_subprocess function when you want to terminate the subprocess
# For example, you can bind it to a button or an event
# Button(app, text="Terminate", command=terminate_subprocess).pack()

app.mainloop()
