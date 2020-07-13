import ValidationFunctions as Validation


class Student:
    def __init__(self, id, first_name, last_name, age, gender, average):
        self.id = Validation.validate_id(id)
        self.first_name = Validation.validate_name(first_name, 'first')
        self.last_name = Validation.validate_name(last_name, 'last')
        self.age = Validation.validate_age(age)
        self.gender = Validation.validate_gender(gender)
        self.average = Validation.validate_average(average)

    def __str__(self):
        if self.gender == 0:
            return 'ID:{} , First Name:{} , Last Name:{} , Age:{} , Gender:{} , Average:{} ,'.format(
                self.id, self.first_name, self.last_name, self.age, 'Female', self.average)
        return 'ID:{} , First Name:{} , Last Name:{} , Age:{} , Gender:{} , Average:{} ,'.format(
            self.id, self.first_name, self.last_name, self.age, 'Male', self.average)
