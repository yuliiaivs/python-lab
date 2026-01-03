class GradeTracker:
    def __init__(self, student_name):
        self.student_name = student_name
        self.grades = []

    # Метод 1: Додавання оцінки (з перевіркою)
    def add_score(self, score):
        if not isinstance(score, (int, float)):
            return "Error: Score must be a number"
        if score < 0 or score > 100:
            return "Error: Score must be between 0 and 100"
        self.grades.append(score)
        return True

    # Метод 2: Середній бал
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    # Метод 3: Чи прохідний бал (наприклад, від 60)
    def check_passing(self, passing_limit=60):
        avg = self.get_average()
        if avg >= passing_limit:
            return f"{self.student_name} passed"
        return f"{self.student_name} failed"