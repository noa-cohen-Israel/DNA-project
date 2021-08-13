from Data import Data


class Replace:
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
        return self.name + "_r" + str(i)

    def add_sequence(self,name):
        self.seq=str(self.get_sequence())
        return Data.getInstance().add_sequence(name,self.seq)


    def get_sequence(self):
        for i in range(1,len(self.string),2):
            if self.string[i] ==":":
                break
            else:
                self.seq[int(self.string[i])]=self.string[i+1]
        return self.seq

    def print_sequence(self):
        return self.seq

    def getReceiver(self):
        return self.receiver
