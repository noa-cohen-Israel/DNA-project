from Data import Data
from Parser import Parser


class Slice:
    def __init__(self,string):
        self.receiver="Manipulate"
        self.string=string

    def get_sequence_by_id(self,id):
        self.id=id
        self.name=Data.getInstance().get_name_by_id(id)
        self.seq=Data.getInstance().get_sequence_by_id(id)


    def save_seq(self):
        Data.getInstance().update_sequence_by_id(self.id,self.get_sequence())
        return self.name

    def get_name(self):
        i = 1
        while not Data.getInstance().getInstance().valid_name(self.name + "_s" + str(i)):
            i += 1
        return self.name + "_s" + str(i)
    def add_sequence(self,name):
        self.seq=str(self.seq)
        return Data.getInstance().add_sequence(name,self.seq[int(self.string[1]):int(self.string[2])])
    def get_sequence(self):
        print(int(self.string[2]),self.seq)
        maxi=min(int(self.string[2]),len(self.seq))
        print(maxi)
        mini=min (int(self.string[1]),len(self.seq))
        print(mini)
        return str(self.seq[mini:maxi])
    def getReceiver(self):
        return self.receiver
    def print_sequence(self):
        return self.get_sequence()
