import json

class File():
    def __init__(self):
        with open("db_DNA.json","w") as file:
            try:
                self.data=json.load(file)
            except:
                self.data=[]

    def write_data(self):
        with open("db_DNA.json","w") as file:
            file.write(json.dumps(self.data))

    def update_data(self, object):
        self.data.append(object)

    def get_data(self):
        return self.data