

class Batch():
    __instance = None

    @staticmethod
    def getInstance(command=None,str=None):
         """ Static access method. """
         if Batch.__instance == None:
             Batch(command,str)
         return Batch.__instance

    def get_batch(self):
        return self.batch.keys()
    def batchshow(self,name):
        return self.batch[name]
    def __init__(self,command=None,str=None):
        # if command== 'run':
        #     self.get_batch()
        self.command=command
        self.str=str
        if command!='Run' and command!=None:
            self.run =str[0]
        else:
            if Batch.__instance != None:
                raise Exception("This class is a singleton!,you need to call to method: getInstance()")
            self.batch=dict()
            self.run=False


    def execute_batch(self,name_batch):
        string = input(str("> batch >>>"))
        while string!="end":
            self.batch[name_batch].append(string)
            string = input(str("> batch >>>"))


    def switch_batch(self,name):
        try:
            self.batch[name[0]]
        except:
            self.batch[name[0]]=[]
        self.execute_batch(name[0])
    def get_run(self,str):
        if str:
            return self.batch[str][:]
        return []
    def perform_action(self):
        if self.command=="batchlist":
            return self.batchshow[self.str]
        pass
    def getReceiver(self):
        return Batch
