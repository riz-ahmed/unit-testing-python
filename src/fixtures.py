import json


Class StudentDB(self):
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)              # converts json file to python dict

    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student
