import json
import random
import csv
from datetime import datetime

DATA_FILE = "quiz_data.json"
CSV_FILE = "results.csv"
TEACHER_PASSWORD = "rohan123"


# Utility Functions 

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError
            if max_val is not None and value > max_val:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Data Handling 

class DataManager:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"questions": [], "results": []}

    def save(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)


#  Question Class 

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def is_correct(self, choice):
        return choice == self.answer

    def to_dict(self):
        return {
            "question": self.text,
            "options": self.options,
            "answer": self.answer
        }


#  Quiz System 

class QuizSystem:
    def __init__(self):
        self.manager = DataManager(DATA_FILE)
        self.data = self.manager.load()

    #  Teacher 
    def add_question(self):
        password = input("Enter teacher password: ")
        if password != TEACHER_PASSWORD:
            print("Wrong password!\n")
            return

        text = input("Enter question: ")
        options = []
        for i in range(4):
            options.append(input(f"Option {i+1}: "))

        answer = input_int("Correct option (1-4): ", 1, 4)
        q = Question(text, options, answer)
        self.data["questions"].append(q.to_dict())
        self.manager.save(self.data)

        print("Question added successfully!\n")

    #  Student
    def take_quiz(self):
        if not self.data["questions"]:
            print("No questions available!\n")
            return

        name = input("Enter your name: ")
        questions = self.data["questions"].copy()
        random.shuffle(questions)

        score = 0
        for q in questions:
            print("\n" + q["question"])
            for i, opt in enumerate(q["options"], start=1):
                print(f"{i}. {opt}")

            choice = input_int("Your answer: ", 1, 4)
            if choice == q["answer"]:
                score += 1

        result = {
            "name": name,
            "score": score,
            "total": len(questions),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        self.data["results"].append(result)
        self.manager.save(self.data)
        self.export_csv()

        print(f"\n{name}, your score is {score}/{len(questions)}")

    # CSV Export
    def export_csv(self):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Score", "Total", "Date"])
            for r in self.data["results"]:
                writer.writerow([r["name"], r["score"], r["total"], r["date"]])

    #  View Results 
    def view_results(self):
        if not self.data["results"]:
            print("No results.\n")
            return

        print("\n--- Quiz Results ---")
        for r in self.data["results"]:
            print(f"{r['name']} | {r['score']}/{r['total']} | {r['date']}")

    # Menu 
    def run(self):
        while True:
            print("\nQUIZ SYSTEM")
            print("1. Add Question (Teacher)")
            print("2. Take Quiz (Student)")
            print("3. View Result")
            print("4. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_question()
            elif choice == "2":
                self.take_quiz()
            elif choice == "3":
                self.view_results()
            elif choice == "4":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    QuizSystem().run()
