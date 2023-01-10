from demo_api.models import Student


def get_student(self):
    return Student.objects.create(first_name=self.first_name, last_name=self.last_name)


def mock_student():
    # print("testing mock")
    student = get_student()
    # print("testing mock student")
    return student
