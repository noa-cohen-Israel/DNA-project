from Data import Data

class New:
    def __init__(self,str):
        self.receiver="Create"
        self.sequence=str

    def get_name(self):
        return Data.getInstance().get_new_name()

    def get_sequence(self):
        return self.sequence

    def getReceiver(self):
        return self.receiver




