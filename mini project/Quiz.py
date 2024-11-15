import tkinter as tk
from tkinter import messagebox
import random
import csv
from tkinter import ttk

class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Application")
        self.master.geometry("1920x1080")
        
        # Title Label
        self.title_label = tk.Label(master, text="Choose Difficulty", font=("Amasis MT Pro Black", 36, "bold"))
        self.title_label.pack(pady=20)

        # Difficulty Selection Dropdown
        self.difficulty_var = tk.StringVar(value="Select Difficulty")  # Default text
        self.difficulty_dropdown = ttk.Combobox(master, textvariable=self.difficulty_var,
                                                 values=["easy", "medium", "hard"],
                                                 state='readonly',
                                                 font = ("Helvetica", 14))
        self.difficulty_dropdown.pack(pady=10)

        # Start Quiz Button
        self.start_button = tk.Button(master, text="Start Quiz", font=("Amasis MT Pro Black", 18), command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        difficulty = self.difficulty_var.get().lower()  # Get the selected difficulty in lowercase
        if difficulty == "select difficulty":
            messagebox.showwarning("Warning", "Please select a difficulty level.")
            return

        # Hide dropdown and start button
        self.title_label.pack_forget()
        self.difficulty_dropdown.pack_forget()
        self.start_button.pack_forget()

        # Load questions based on difficulty
        self.questions = self.load_questions(difficulty)
        if not self.questions:
            messagebox.showerror("Error", "No questions found for this difficulty.")
            return

        self.score = 0
        self.question_index = 0
        self.display_question()

    def load_questions(self, difficulty):
        questions = []
        file_path = f"C:\\Users\\User\\OneDrive\\Desktop\\mini project\\{difficulty}.csv"  # Assuming each difficulty has its own file
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    question, *options, answer = row
                    questions.append({"question": question, "options": options, "answer": answer})
        except FileNotFoundError:
            messagebox.showerror("File Error", f"File {file_path} not found.")
            return None
        return random.sample(questions, min(10, len(questions)))

    def display_question(self):
        if self.question_index >= len(self.questions):
            self.show_score()
            return

        # Display question
        question_data = self.questions[self.question_index]
        question_text = question_data["question"]
        
        # Question Label
        self.question_label = tk.Label(self.master, text=question_text, font=("Amasis MT Pro Black", 18))
        self.question_label.pack(pady=20)

        # Option Buttons
        self.option_buttons = []
        for idx, option in enumerate(question_data["options"]):
            button = tk.Button(self.master, text=option, font=("Amasis MT Pro Black", 14), 
                               command=lambda selected_option=option: self.check_answer(selected_option))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
        
        # Move to the next question
        self.question_index += 1
        self.clear_question()
        self.display_question()

    def clear_question(self):
        # Remove the question and options from the screen
        self.question_label.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()

    def show_score(self):
        # Show the final score
        messagebox.showinfo("Quiz Complete", f"Your final score is: {self.score}/{len(self.questions)}")
        self.master.destroy()  # Close the quiz window after showing the score
