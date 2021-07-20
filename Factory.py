from Create import Create
from Management import Management
from command.Save import Save
from command.Batchlist import Batchlist
from command.Del import Del
from command.New import New
from command.Load import Load
from command.Dup import Dup
from command.Replace import Replace
from command.Run import Run
from command.Slice import Slice
from Manipulate import Manipulate

from Batch import Batch

class Factory():
    def __init__(self):
        self.commands ={"new":New,"load":Load, "dup":Dup,"slice":Slice,"run":Run,"batchlist":Batch,"replace":Replace,"del":Del,"save":Save}
        self.state={"Create":Create,"Manipulate":Manipulate,"Batch":Batch().getInstance,"Management":Management}

    def creating(self, string):
        string=string.split(" ")
        command=self.commands[string[0]]
        return self.state[command(string[1:]).getReceiver()](command,string[1:])

#
# n=New("AAA")
# print(n.get_name())
# f=Factory()
# f.creating("new AAA @ggg")
# slice #1 2 6
# new AAAAAAAAGGGG