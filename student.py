class Student:
    # class variables
    total_students = 0
    all_students = []

    # for everytime we create an instance, update the all_students array to include the instance you just created

    def __init__(self, first_name, last_name, gender, course):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.course = course
        Student.total_students += 1
        Student.all_students.append(self)

    # instance methods
    # getter method
    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    @property
    def first_name(self):
        return self._first_name

    # setter method
    @first_name.setter
    def first_name(self, name_input):
        if isinstance(name_input, str):
            self._first_name = name_input

        else:
            raise ValueError("First name must be of type string")

    def __repr__(self):
        return str(self.__dict__)


student1 = Student(
    "Frank",
    "Mwangi",
    "Male",
    "Software Engineering",
)


student2 = Student(
    "Brian",
    "Ngoyoni",
    "Male",
    "Software Engineering",
)


student3 = Student(
    "Calvin",
    "Cheptoo",
    "Female",
    "Software Engineering",
)

student4 = Student(
    "Jeremy",
    "Leannan",
    "Male",
    "Software Engineering",
)


student5 = Student(
    "John",
    "Doe",
    "Male",
    "Software Engineering",
)


# print(student2.__dict__)


# access the email of student 1 and student 3
# print(student1.email)
print(student3.email)
# print(Student.total_students)
# print(Student.all_students)


print(student5)
