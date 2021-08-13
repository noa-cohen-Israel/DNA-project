from Create import Create
from Management import Management
from command.Reenum import Reenum
from command.Rename import Rename
from command.Save import Save
from command.Del import Del
from command.New import New
from command.Load import Load
from command.Dup import Dup
from command.Replace import Replace
from command.Slice import Slice
from Manipulate import Manipulate

class Factory():
    def __init__(self):
        self.commands ={"new":New,"load":Load, "dup":Dup,"slice":Slice,"replace":Replace,"del":Del,"save":Save,"rename":Rename,"reenum":Reenum}
        self.state={"Create":Create,"Manipulate":Manipulate,"Management":Management}

    def creating(self, string):
        string=string.split(" ")
        command=self.commands[string[0]]
        return self.state[command(string[1:]).getReceiver()](command,string[1:])
