from Data import Data
from Print import Print


class Del:
    def __init__(self,string):
        self.receiver = "Management"
        if string[0][0] == "#":
            self.id = string[0][1:]
            self.name = Data.getInstance().get_name_by_id(self.id)
        else:
            self.name = string[0][1:]
            self.id = Data.getInstance().get_id_by_name(self.name)
        self.seq=Data.getInstance().get_sequence_by_id(self.id)

    def getReceiver(self):
        return self.receiver

    def run(self):
        if self.name==False or self.id==False:
            print("the sequense not exist")
        else:
            print("Do you really want to delete ",self.name,":",self.seq)
            print("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
            result_input=input(">confirm>>>")
            while str(result_input) not in ['Y','N','n','y']:
                print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
                result_input = input(">confirm>>>")
            if str(result_input) in ['y','Y']:
                if Data.getInstance().delete_seq(self.id):
                    print("Deleted:",end=" ")
                    Print().sequence({"id":self.id,"name":self.name,"sequence":self.seq})
                else:
                    print("the delete not success")


