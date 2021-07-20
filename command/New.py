from File import File
from Parser import Parser
from Data import Data
from Print import Print
class New:
    def __init__(self,str):
        self.receiver="Create"
        print(str)
        self.sequence=str
    def get_name(self):
        print("dddd")
        return Data.getInstance().get_new_name()
    def get_sequence(self):
        return self.sequence
    def getReceiver(self):
        return self.receiver




