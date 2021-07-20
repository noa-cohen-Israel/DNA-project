from Data import Data
from Parser import Parser
from Print import Print


class Save:
    def __init__(self,string):
        self.receiver = "Management"
        if string[0][0] == "#":
            self.id = string[0][1:]
            self.name = Data.getInstance().get_name_by_id(self.id)
        else:
            self.name = string[0][1:]
            self.id = Data.getInstance().get_id_by_name(self.name)
        self.seq=Data.getInstance().get_sequence_by_id(self.id)
        try:
            self.file_name=string[1]+".rawdna"
        except:
            self.file_name=self.name+".rawdna"



    def getReceiver(self):
        return self.receiver
    def run(self):
        with open(self.file_name+".txt","w") as f:
            f.write(f'[{self.id}] {self.name}: {self.seq}')





