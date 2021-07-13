from Data import Data
from Parser import Parser
from Print import Print
from command.New import New

class Create:
    def __init__(self,command,string):
        self.command=command(string[0])
        if len(string)<=2:
            try:
                self.name=Parser().name(string[1])
            except:
                self.name=self.command.get_name()
            finally:
                self.sequence=self.command.get_sequence()
                print(self.sequence)
        else:
            raise ValueError("new command get just 2 arguments")
    def perform_action(self):
        if not self.sequence:
            return False
        print(self.name,self.sequence)
        result = Data.getInstance().add_sequence(self.name,  self.sequence)
        print(type(result))
        if type(result) == type(""):
            print(result)
            return False
        else:
            Print().sequence(result)
            return True
