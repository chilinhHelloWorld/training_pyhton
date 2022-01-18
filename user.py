# class User:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age 
#         self.address = address

#     def getName(self):
#         return self.name
#     def getAge(self):
#         return self.age
#     def getAddress(self):
#         return self.address

#     def getUser(self):
#         return self
import json

class StudentDB:
    def __init__(self):
        self.__data = None
    def connect(self, data_file):
        with open(data_file) as json.file:
            self.__data = json.load(json.file)
    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student