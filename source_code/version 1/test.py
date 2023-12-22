import tkinter as tk
import sys

class RedirectText:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)  # Auto-scroll to the bottom

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Terminal on Tkinter")

        self.text_widget = tk.Text(root, wrap="word", font=("Courier New", 12))
        self.text_widget.pack(expand=True, fill="both")

        # Redirect stdout and stderr
        sys.stdout = RedirectText(self.text_widget)
        sys.stderr = RedirectText(self.text_widget)

        # Add a button to clear the text widget
        clear_button = tk.Button(root, text="Clear", command=self.clear_text)
        clear_button.pack()

    def clear_text(self):
        self.text_widget.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
