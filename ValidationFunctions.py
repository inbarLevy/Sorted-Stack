def validate_id(id):
    number = id
    counter = 0
    if type(id) != int or id <= 0:
        print('Incorrect Id, so id=Null')
        return
    while number > 0:
        if counter > 9:
            print('Incorrect Id, so id=Null')
            return
        number = number // 10
        counter += 1
    if counter != 9 or number < 0:
        print('Incorrect Id, so id=Null')
        return
    return id


def validate_name(name, type):
    if str(name).isalpha():
        return name
    if type == 'first':
        print('Incorrect First Name, so first_name=Null')
        return
    print('Incorrect Last Name, so last_name=Null')
    return


def validate_age(age):
    if type(age) != int or age < 0:
        print('Incorrect Age, so age=Null')
        return


def validate_gender(gender):
    if gender == 1 or gender == 0:
        return gender
    print('Incorrect Gender, so gender=Null')
    return


def validate_average(average):
    if 0 <= average <= 100:
        return average
    print('Incorrect Average, so average=Null')
    return

