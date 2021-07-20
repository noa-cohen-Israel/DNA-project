from Data import Data
from Parser import Parser
from Print import Print
from command.New import New


class Manipulate:
    def __init__(self, command, string):
        self.command = command(string)
        self.string=string




    def perform_action(self):
        self.name=False
        string=self.string
        if string[0][0] == "#":
            self.id = int(string[0][1:])
            self.command.get_sequence_by_id(self.id)

        elif string[0][0] == "@":
            self.id = Data.getInstance().get_id_by_name(Parser().name(string[0]))
            self.command.get_sequence_by_id(self.id)
        else:
            return False
        for i in range(len(string)):
            if string[i] == ":":
                string = string[i+1:]
                if string[0] == "@@":
                    self.name = self.command.get_name()
                    self.result = self.command.add_sequence(self.name)
                else:
                    self.name = string[0][1:]
                    self.result = self.command.add_sequence(self.name)
                Print().sequence(self.result)
                return
        if not self.name:
            self.name = self.command.save_seq()

        Print().sequence({"id":self.id,"name":self.name,"sequence":self.command.print_sequence()})

