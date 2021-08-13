from Data import Data

class Reenum:
    def __init__(self,string):
        self.receiver = "Management"

    def getReceiver(self):
        return self.receiver

    def run(self):
        Data.getInstance().reenum_sequense()






