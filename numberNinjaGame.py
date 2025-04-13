import tkinter as tk
import random
import time

class MathSpeedChallenge:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Speed Challenge")
        self.root.geometry("400x300")
        
        self.time_limit = 30  # Set time limit for the game
        self.score = 0
        self.time_left = self.time_limit
        self.problem = ""
        
        # Setup UI elements
        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)
        
        self.problem_label = tk.Label(root, text="Press 'Start' to begin", font=("Helvetica", 16))
        self.problem_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_game, font=("Helvetica", 12))
        self.start_button.pack(pady=10)
        
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left}s", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        self.update_timer()

    def start_game(self):
        self.score = 0
        self.time_left = self.time_limit
        self.update_score()
        self.next_problem()
        self.start_button.config(state=tk.DISABLED)
        self.answer_entry.focus()
        
    def next_problem(self):
        # Generate a random arithmetic problem
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*', '/'])
        
        self.problem = f"{num1} {operator} {num2}"
        self.problem_label.config(text=self.problem)
        
        self.answer_entry.delete(0, tk.END)
        
        # Check the answer when user presses Enter
        self.answer_entry.bind("<Return>", self.check_answer)
        
    def check_answer(self, event):
        try:
            correct_answer = eval(self.problem)
            user_answer = float(self.answer_entry.get())
            if user_answer == correct_answer:
                self.score += 1
                self.update_score()
            self.next_problem()
        except Exception as e:
            pass
        
    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        
    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()
            
    def end_game(self):
        self.problem_label.config(text="Game Over!")
        self.answer_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.timer_label.config(text=f"Final Score: {self.score}")

# Create the main window
root = tk.Tk()
game = MathSpeedChallenge(root)

root.mainloop()
