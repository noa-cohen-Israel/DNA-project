from Data import Data
from Parser import Parser


class Dup:
    def __init__(self,seq):
        self.receiver = "Create"
        self.id= Parser().get_id_by_sequence(seq)
        self.seq=seq

    def get_name(self):
        print(self.id)
        if self.id:
            self.name =Data.getInstance().get_name_by_id(self.id)
            i=1
            while not Data.getInstance().valid_name(self.name+"_"+str(i)):
                i+=1
            return self.name+"_"+str(i)

    def get_sequence(self):
        if not self.id:
            print("<seq> not valid\n you can use load or new")
        return self.seq

    def getReceiver(self):
        return self.receiver




