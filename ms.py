import tkinter as tk
from tkinter import ttk, messagebox

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x500")
        self.user_info = {}
        self.subjects = {
            "Science": [
                {
                    "question": "Which of the following is used in pencils?",
                    "options": ["Graphite", "Silicon", "Charcoal", "Phosphorous"],
                    "answer": 0
                },
                {
                    "question": "Chemical formula for water is",
                    "options": ["NaAlO2", "H2O", "Al2O3", "CaSiO3"],
                    "answer": 1
                },
                {
                    "question": "The gas usually filled in the electric bulb is",
                    "options": ["Nitrogen", "Hydrogen", "Carbon Dioxide", "Oxygen"],
                    "answer": 0
                },
                {
                    "question": "Which of the gas is not known as green house gas?",
                    "options": ["Methane", "Nitrous oxide", "Carbon dioxide", "Hydrogen"],
                    "answer": 3
                },
                {
                    "question": "Which of the following is used as a lubricant?",
                    "options": ["Graphite", "Silica", "Iron Oxide", "Diamond"],
                    "answer": 0
                }
            ],
            "Math": [
                {
                    "question": "Find the sum of 111 + 222 + 333",
                    "options": ["700", "666", "10", "100"],
                    "answer": 1
                },
                {
                    "question": "a = 10 & b = 5 then 2a+2b = ?",
                    "options": ["20", "15", "30", "25"],
                    "answer": 2
                },
                {
                    "question": "a = 5 & b = 10 then (2a+2b)^2 = ?",
                    "options": ["400", "150", "300", "900"],
                    "answer": 3
                },
                {
                    "question": "a = 5 & b = 10 then (2a-2b)^2 = ?",
                    "options": ["100", "400", "800", "900"],
                    "answer": 0
                },
                {
                    "question": "a = 5 & b = 10 & c= 1 then (2a+2b+c)^2 = ?",
                    "options": ["100", "300", "49", "900"],
                    "answer": 3
                }
            ],
            "English": [
                {
                    "question": "Choose the correctly spelled word.",
                    "options": ["Recieve", "Receive", "Receeve", "Receve"],
                    "answer": 1
                },
                {
                    "question": "Which is a synonym for 'happy'?",
                    "options": ["Sad", "Angry", "Joyful", "Tired"],
                    "answer": 2
                },
                {
                    "question": "Fill in the blank: She _____ to the market.",
                    "options": ["go", "goes", "going", "gone"],
                    "answer": 1
                },
                {
                    "question": "Which word is a noun?",
                    "options": ["Quickly", "Run", "Happiness", "Blue"],
                    "answer": 2
                },
                {
                    "question": "Choose the correct sentence.",
                    "options": [
                        "He don't like apples.",
                        "He doesn't likes apples.",
                        "He doesn't like apples.",
                        "He don't likes apples."
                    ],
                    "answer": 2
                }
            ]
        }
        self.selected_subject = None
        self.questions = []
        self.current_q = 0
        self.correct = 0
        self.wrong = 0
        self.wrong_list = []
        self.user_answers = []
        self.create_user_info_frame()

    def create_user_info_frame(self):
        self.clear_frame()
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(pady=30)
        tk.Label(self.info_frame, text="Enter Your Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.info_frame)
        self.name_entry.grid(row=0, column=1)
        tk.Label(self.info_frame, text="Mobile Number:").grid(row=1, column=0, sticky="e")
        self.mobile_entry = tk.Entry(self.info_frame)
        self.mobile_entry.grid(row=1, column=1)
        tk.Label(self.info_frame, text="Date of Birth (dd/mm/yy):").grid(row=2, column=0, sticky="e")
        self.dob_entry = tk.Entry(self.info_frame)
        self.dob_entry.grid(row=2, column=1)
        self.submit_btn = ttk.Button(self.info_frame, text="Submit", command=self.submit_user_info)
        self.submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def submit_user_info(self):
        name = self.name_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        dob = self.dob_entry.get().strip()
        if not name or not mobile or not dob:
            messagebox.showerror("Error", "Please fill all fields.")
            return
        self.user_info = {"name": name, "mobile": mobile, "dob": dob}
        self.confirm_user_info()

    def confirm_user_info(self):
        self.clear_frame()
        info = f"Name: {self.user_info['name']}\nMobile: {self.user_info['mobile']}\nDOB: {self.user_info['dob']}"
        tk.Label(self.root, text=info, font=("Arial", 12)).pack(pady=20)
        ttk.Button(self.root, text="Is everything correct?", command=self.create_subject_frame).pack(pady=10)

    def create_subject_frame(self):
        self.clear_frame()
        tk.Label(self.root, text="Select Subject", font=("Arial", 14, "bold")).pack(pady=20)
        self.subject_var = tk.StringVar()
        for subject in self.subjects.keys():
            ttk.Radiobutton(self.root, text=subject, variable=self.subject_var, value=subject).pack(anchor="w", padx=40)
        ttk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        subject = self.subject_var.get()
        if not subject:
            messagebox.showerror("Error", "Please select a subject.")
            return
        self.selected_subject = subject
        self.questions = self.subjects[subject]
        self.current_q = 0
        self.correct = 0
        self.wrong = 0
        self.wrong_list = []
        self.user_answers = []
        self.show_question()

    def show_question(self):
        self.clear_frame()
        if self.current_q >= len(self.questions):
            self.show_result()
            return
        q = self.questions[self.current_q]
        tk.Label(self.root, text=f"Q{self.current_q+1}: {q['question']}", font=("Arial", 13, "bold"), wraplength=500).pack(pady=20)
        self.selected_option = tk.IntVar(value=-1)
        for idx, opt in enumerate(q["options"]):
            ttk.Radiobutton(self.root, text=opt, variable=self.selected_option, value=idx).pack(anchor="w", padx=40)
        ttk.Button(self.root, text="Submit Answer", command=self.submit_answer).pack(pady=20)

    def submit_answer(self):
        selected = self.selected_option.get()
        if selected == -1:
            messagebox.showerror("Error", "Please select an option.")
            return
        q = self.questions[self.current_q]
        self.user_answers.append(selected)
        if selected == q["answer"]:
            self.correct += 1
        else:
            self.wrong += 1
            self.wrong_list.append({
                "question": q["question"],
                "options": q["options"],
                "correct": q["options"][q["answer"]],
                "your": q["options"][selected]
            })
        self.current_q += 1
        self.show_question()

    def show_result(self):
        self.clear_frame()
        total = len(self.questions)
        tk.Label(self.root, text=f"Quiz Completed!", font=("Arial", 15, "bold"), fg="blue").pack(pady=10)
        tk.Label(self.root, text=f"Correct Answers: {self.correct}/{total}", font=("Arial", 13), fg="green").pack()
        tk.Label(self.root, text=f"Wrong Answers: {self.wrong}/{total}", font=("Arial", 13), fg="red").pack(pady=5)
        if self.wrong_list:
            tk.Label(self.root, text="Questions you got wrong:", font=("Arial", 12, "bold")).pack(pady=10)
            for item in self.wrong_list:
                tk.Label(self.root, text=f"Q: {item['question']}", font=("Arial", 11, "bold")).pack(anchor="w", padx=30)
                tk.Label(self.root, text=f"Your answer: {item['your']}", fg="red").pack(anchor="w", padx=50)
                tk.Label(self.root, text=f"Correct answer: {item['correct']}", fg="green").pack(anchor="w", padx=50)
        else:
            tk.Label(self.root, text="Great job! All answers correct!", font=("Arial", 12), fg="green").pack(pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameGUI(root)
    root.mainloop()