from Data import Data
from Factory import Factory
from File import File
from Batch import Batch


class CLI:
    def __init__(self):
        self.factory=Factory()
        self.file=File()
        self.data=Data(self.file)
        self.batch=Batch()
        self.cmd=[]
        self.list=[]

    def run(self):
        while True:
            if len(self.list) != 0:
                success_command=0
                string=self.list[0]
                self.list.remove(self.list[0])
            else:
                string = input(str(">cmd>>>"))
            if len(self.list) == 0 and str(string.split(" ")[0]) == 'run':
                self.list = self.batch.get_run(string.split(" ")[1])
            else:
                try:
                    if str(string.split(" ")[0]) in ['batch','batchlist','batchshow','batchsave','batchload']:
                        self.batch.perform_action(str(string.split(" ")[0]),string.split(" ")[1:])
                    else:
                        if len(self.list) != 0 and success_command:
                            pass
                        else:
                            cmd=self.factory.creating(string)
                            cmd.perform_action()
                except:
                    print("command not valid")
                    success_command=1


cli=CLI()
cli.run()
