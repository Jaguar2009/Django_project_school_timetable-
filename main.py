from school_timetable.models import Subject, Teacher, Class, Student, Schedule, Grade


def create_subject():
    name = input("Введіть назву предмету: ")
    description = input("Введіть опис предмету: ")
    subject = Subject.objects.create(name=name, description=description)
    print(f"Предмет '{subject.name}' створено.")


def create_teacher():
    first_name = input("Введіть ім'я вчителя: ")
    last_name = input("Введіть прізвище вчителя: ")
    subject_id = input("Введіть ID предмету, який викладає вчитель: ")
    subject = Subject.objects.get(id=subject_id)
    teacher = Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
    print(f"Вчителя '{teacher.first_name} {teacher.last_name}' створено.")


def create_class():
    name = input("Введіть назву класу: ")
    year = input("Введіть рік навчання: ")
    student_class = Class.objects.create(name=name, year=year)
    print(f"Клас '{student_class.name}' створено.")


def create_student():
    first_name = input("Введіть ім'я учня: ")
    last_name = input("Введіть прізвище учня: ")
    class_id = input("Введіть ID класу: ")
    student_class = Class.objects.get(id=class_id)
    student = Student.objects.create(first_name=first_name, last_name=last_name, student_class=student_class)
    print(f"Учня '{student.first_name} {student.last_name}' створено.")


def create_schedule():
    day_of_week = input("Введіть день тижня: ")
    start_time = input("Введіть час початку (HH:MM): ")
    subject_id = input("Введіть ID предмету: ")
    teacher_id = input("Введіть ID вчителя: ")
    class_id = input("Введіть ID класу: ")
    subject = Subject.objects.get(id=subject_id)
    teacher = Teacher.objects.get(id=teacher_id)
    student_class = Class.objects.get(id=class_id)
    schedule = Schedule.objects.create(day_of_week=day_of_week, start_time=start_time, subject=subject, teacher=teacher, student_class=student_class)
    print(f"Розклад на {day_of_week} о {start_time} створено.")


def create_grade():
    student_id = input("Введіть ID учня: ")
    subject_id = input("Введіть ID предмету: ")
    grade_value = input("Введіть оцінку: ")
    date = input("Введіть дату (YYYY-MM-DD): ")
    student = Student.objects.get(id=student_id)
    subject = Subject.objects.get(id=subject_id)
    grade = Grade.objects.create(student=student, subject=subject, grade=grade_value, date=date)
    print(f"Оцінка {grade_value} для {student.first_name} {student.last_name} з предмету {subject.name} створена.")


def main():
    while True:
        print("Оберіть дію:")
        print("1. Створити предмет")
        print("2. Створити вчителя")
        print("3. Створити клас")
        print("4. Створити учня")
        print("5. Створити розклад")
        print("6. Створити оцінку")
        print("0. Вийти")

        choice = input("Введіть номер дії: ")

        if choice == '1':
            create_subject()
        elif choice == '2':
            create_teacher()
        elif choice == '3':
            create_class()
        elif choice == '4':
            create_student()
        elif choice == '5':
            create_schedule()
        elif choice == '6':
            create_grade()
        elif choice == '0':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == '__main__':
    main()