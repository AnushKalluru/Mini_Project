import tkinter as tk
from PIL import Image, ImageTk
from Quiz import Quiz
from Web import Web

# Create the main window
root = tk.Tk()
root.title("Multitool Desktop App")
root.geometry("1920x1080")
root.configure(bg = "white")
# Welcome Label
title_label = tk.Label(
    root, 
    text="Welcome to our App!!", 
    font=("Helvetica", 24, "bold"),
    fg="white",
    bg="lightblue",
    pady=10
)
title_label.pack(fill=tk.X)

# Load and resize images
quiz_image = Image.open("C:\\Users\\User\\OneDrive\\Desktop\\mini project\\quizlogo.jpg").resize((180, 180), Image.LANCZOS)
quiz_icon = ImageTk.PhotoImage(quiz_image)

scraper_image = Image.open("C:\\Users\\User\\OneDrive\\Desktop\\mini project\\weblogo.jpg").resize((180, 180), Image.LANCZOS)
scraper_icon = ImageTk.PhotoImage(scraper_image)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=50)  # Adds padding above and below the frame


def open_quiz():
    quiz_window = tk.Toplevel(root)
    Quiz(quiz_window)

def open_web():
    web_window = tk.Toplevel(root)
    Web(web_window)  # Assuming Web is a class that takes a Tkinter window as an argument



# Button for "Quizzes" app with image
quiz_button = tk.Button(button_frame, image=quiz_icon, text="Quizzes", compound="top", font=("Helvetica", 12), bg="black", fg="white",command=open_quiz)
quiz_button.grid(row=0, column=0, padx=30, pady=20)

# Button for "Web Scraper" app with image
scraper_button = tk.Button(button_frame, image=scraper_icon, text="APP2", compound="top", font=("Helvetica", 12), bg="black", fg="white",command = open_web)
scraper_button.grid(row=0, column=1, padx=30, pady=20)

# Configure layout to center buttons within the frame
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

# Keep references to images to prevent garbage collection
quiz_button.image = quiz_icon
scraper_button.image = scraper_icon

# Start the GUI event loop
root.mainloop()
