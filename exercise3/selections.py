student_id = input("Please enter a student ID: ")


while True:
    try:
        midterm_exam = input("Please enter the student's midterm exam mark (0-100): ")
        midterm_exam = float(midterm_exam)
        if midterm_exam < 0 or midterm_exam > 100:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid exam mark (0-100)")

while True:
    try:
        final_exam = input("Please enter the student's final exam mark (0-100): ")
        final_exam = float(final_exam)
        if final_exam < 0 or final_exam > 100:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid exam mark (0-100)")

total_mark = (midterm_exam * 0.4) + (final_exam * 0.6)
if 80 <= total_mark <= 100:
    grade = "A"
    print(f"{student_id} has total mark as {total_mark:.2f} and grade as {grade}")
elif 70 <= total_mark < 80:
    grade = "B"
    print(f"{student_id} has total mark as {total_mark:.2f} and grade as {grade}")
elif 60 <= total_mark < 70:
    grade = "C"
    print(f"{student_id} has total mark as {total_mark:.2f} and grade as {grade}")
elif 50 <= total_mark < 60:
    grade = "D"
    print(f"{student_id} has total mark as {total_mark:.2f} and grade as {grade}")
elif 0 == total_mark < 50:
    grade = "F"
    print(f"{student_id} has total mark as {total_mark:.2f} and grade as {grade}")
