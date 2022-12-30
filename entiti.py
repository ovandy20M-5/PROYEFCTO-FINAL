import datetime

class Form():
    def __init__(self, id, carnet=None, fullname=None, address=None, gender=None, phone_number=None, birth_date=None, career=None, genre=None, ins_date=None, part_date=None, age = None):
        self.id = id
        self.carnet = carnet
        self.fullname = fullname
        self.address = address
        self.gender = gender
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.career = career
        self.genre = genre
        self.ins_date = datetime.date.today()
        self.part_date = part_date
        self.age = age

class List():
    def __init__(self, carnet=None, fullname=None, address=None, gender=None, phone_number=None, birth_date=None, career=None, genre=None, ins_date=None, part_date=None, age=None):
        self.carnet = carnet
        self.fullname = fullname
        self.address = address
        self.gender = gender
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.career = career
        self.genre = genre
        self.ins_date = ins_date
        self.part_date = part_date
        self.age = age
    def to_json(self):
        return{
            #'carnet': self.carnet,
            'fullname': self.fullname,
            #'address': self.address,
            #'gender': self.gender,
            #'phone_number': self.phone_number,
            #'birth_date': self.birth_date,
            'career': self.career,
            'genre': self.genre,
            #'ins_date': self.ins_date,
            'part_date': self.part_date,
            'age': self.age 

        }