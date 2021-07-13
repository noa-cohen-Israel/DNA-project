from Data import Data


class Parser():
    # def __init__(self):


    def name(self,string):
        if string[0]=="@":
            return string[1:]
        else:
            raise ValueError
    def id(self,string):
        if string[0]=="#":
            return string[1:]
        else:
            raise ValueError
    def get_id_by_sequence(self,seq):
        return Data.getInstance().get_id_by_sequence(seq)
    def get_sequence_by_info(self,string):
        if string[0]=="#":
            return Data.getInstance().get_sequence_by_id(string[1:])
        if string[0]=="@":
            return Data.getInstance().get_sequence_by_name(string[1:])
        return False
    def get_type(self,string):
        if string[0] == "#":
            return "id"
        if string[0] == "@":
            return "name"

