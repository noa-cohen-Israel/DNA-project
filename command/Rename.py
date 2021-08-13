from Data import Data

class Rename:
    def __init__(self,string):
        self.receiver = "Management"
        if string[0][0] == "#":
            self.id = string[0][1:]
            self.name = Data.getInstance().get_name_by_id(self.id)
        else:
            self.name = string[0][1:]
            self.id = Data.getInstance().get_id_by_name(self.name)
        self.new_name=string[1][1:]


    def getReceiver(self):
        return self.receiver

    def run(self):
        message=Data.getInstance().update_name_by_id(self.id,self.name,self.new_name)
        if message!=None:
            print(message)





