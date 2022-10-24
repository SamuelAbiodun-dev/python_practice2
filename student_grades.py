
grade = int(input("Enter grade or -1 to quit: "))


def student_grade():
    total = 0
    grade = 0
    grade_counter = 0
    while grade != -1:
        total = total + grade
        grade_counter = grade_counter + 1
        grade = int(input("Enter grade -1 to quit: "))
    if grade_counter != 0:
        average = total / grade_counter
        print(f"Class average is: {average:.2f}")
    else:
        print("No grades were entered")


if __name__ == '__main__':
    student_grade()
