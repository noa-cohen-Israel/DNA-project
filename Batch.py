class Batch(object):
    __instance = None

    @staticmethod
    def getInstance(command=None,str=None):
         """ Static access method. """
         if Batch.__instance == None:
             Batch()
         return Batch.__instance
    def get_dict_batch(self):
        return self.batch
    def get_batch(self):
        return self.batch.keys()
    def batchshow(self,name):
        return self.batch[name]
    def __init__(self,command=None,str=None):
        # if command== 'batchlist':
        #     self.get_batch()
        if command!=None:
            command=command(str)
            command.run()
        else:
            if Batch.__instance != None:
                raise Exception("This class is a singleton!,you need to call to method: getInstance()")
            self.batch=dict()

    def execute_batch(self,name_batch):
        string = input(str("> batch >>>"))
        while string!="end":
            self.batch[name_batch].append(string)
            string = input(str("> batch >>>"))


    def switch_batch(self,name):
        try:
            self.batch[name]
        except:
            self.batch[name[0]]=[]
        self.execute_batch(name[0])


