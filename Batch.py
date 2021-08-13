import json


class Batch():
    __instance = None

    @staticmethod
    def getInstance(command=None,str=None):
         """ Static access method. """
         if Batch.__instance == None:
             Batch(command)
         return Batch.__instance

    def __init__(self, command=None):
        if Batch.__instance != None:
            raise Exception("This class is a singleton!,you need to call to method: getInstance()")
        self.batch = dict()

    def get_batch(self):
        return [i for i in self.batch.keys()]

    def batchshow(self,name):
        return self.batch.get(name)

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

    def batchsave(self,batch_name,file_name):
        with open(file_name+".dnabatch" + ".txt", "w") as f:
            f.write(json.dumps(self.batchshow(batch_name)))

    def batchload(self,file_name,batch_name=None):
        try:
            with open(file_name) as f:
                if batch_name==None:
                    self.batch[file_name.split(".")[0]] =json.load(f)
                else:
                    self.batch[batch_name]=json.load(f)
        except:
            print("load file failed")

    def perform_action(self,command,str):
        if command=="batch":
            self.switch_batch(str)
        elif command == "batchlist":
            print( self.get_batch())
        elif command=="batchshow":
            if len(str)==1:
                print(self.batchshow(str[0][1:]))
        elif command=="batchsave":
            if len(str)==1:
                self.batchsave(str[0][1:],str[0][1:])
            if len(str)==2:
                self.batchsave(str[0][1:],str[1])
        elif command == "batchload":
            if len(str) == 1:
                self.batchload(str[0])
            elif len(str) == 2:
                self.batchload(str[0], str[0][1:])

