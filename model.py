from flask import jsonify
from db import get_connection
from entiti import List

class ListModel():
    @classmethod
    def get_students(self):
        try:
            connection = get_connection()
            students = []
            with connection.cursor() as cursor:
                cursor.execute("""SELECT carnet, fullname, address, gender, phone_number, birth_date, career, genre, ins_date, part_date, age FROM students 
                ORDER BY fullname ASC""")
                resulset = cursor.fetchall()
                for row in resulset:
                    student = List(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    students.append(student.to_json())
            connection.close()
            return students
        except Exception as ex:
            raise Exception(ex)


class formModel():
    @classmethod
    def form(self, students):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO  students (carnet, fullname, address, gender, phone_number, birth_date, career, genre, ins_date, part_date, age)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s)""".format(), (students.carnet, students.fullname, students.address, students.gender, students.phone_number, students.birth_date, students.career, students.genre, students.ins_date, students.part_date, students.age)) 
                affected_row = cursor.rowcount
                connection.commit()
            connection.close()
            
            return affected_row
        except Exception as ex:
            raise Exception(ex)