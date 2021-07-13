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


    def run(self):
        while True:
            string = input(str(">cmd>>>"))
            try:
                if str(string.split(" ")[0]) == 'batch':
                    print("lll")
                    self.batch.switch_batch(string.split(" ")[1:])
                else:
                    cmd=self.factory.creating(string)
                    cmd.perform_action()
            except:
                print("command not valid")

#
cli=CLI()
cli.run()
