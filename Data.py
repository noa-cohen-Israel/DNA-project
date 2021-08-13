from DnaSequence import DnaSequence

class Data(object):
    __instance = None

    @staticmethod
    def getInstance(file=None):
        """ Static access method. """
        if Data.__instance == None:
            Data(file)
        return Data.__instance

    def __init__(self, file=None):
        if Data.__instance != None:
            raise Exception("This class is a singleton!,you need to call to method: getInstance()")
        else:
            if file !=None:
                self.updete = "00"
                self.data = file.get_data()
                if len(self.data) == 0:
                    self.data.append({"id": 0, "name": 0})
                    self.data.append(dict())
                    self.data.append(dict())
                self.id = self.data[0]["id"]
                self.name = self.data[0]["name"]
                self.id_and_name=self.data[1]
                self.sequence=self.data[2]
                self.name_and_id = dict()
                for i in self.id_and_name.keys():
                    self.name_and_id[self.id_and_name[i]] = i
                Data.__instance = self
            else:
                raise ValueError("the file is None")

    def delete_seq(self,id):
        id=int(id)
        try:
            self.name_and_id.pop(self.get_name_by_id(id))
            self.id_and_name.pop(id)
            self.sequence.pop(id)
            return True
        except:
            return False

    def get_new_id(self):
        self.id +=1
        return self.id

    def get_new_name(self):
        self.name += 1
        while self.name_and_id.get(self.name)!=None:
            self.name += 1
        self.updete="11"
        return "seq" + str(self.name)

    def get_id_by_name(self, name):
        try:
            return int(self.name_and_id[name])
        except:
            return False

    def get_name_by_id(self, id):
        try:
            return self.id_and_name[int(id)]
        except:
            return False

    def get_sequence_by_name(self, name):
        try:
            return self.sequence[self.name_and_id[name]]
        except:
            return False

    def get_sequence_by_id(self, id):
        try:
            return self.sequence[int(id)]
        except:
            return False

    def get_id_by_sequence(self,sequence):
        for i in self.sequence.keys():
            if self.sequence[i] == sequence:
                return int(i)
        return False

    def valid_name(self, name):
        if self.name_and_id.get(name)==None:
            return True
        return False

    def update_sequence_by_id(self,id,seq):
        self.sequence[int(id)]=seq

    def update_name_by_id(self,id,name,new_name):
        if not self.valid_name(new_name):
            return "This name exist"
        self.id_and_name[int(id)]=new_name
        self.name_and_id.pop(name)
        self.name_and_id[new_name]=id

    def add_sequence(self, name,sequence):
        if not self.valid_name(name):
           return "This name exist"
        try:
           sequence=DnaSequence(sequence)
        except:
            if self.updete[1]=="1":
                self.updete="00"
                self.name-=1
            return "The DNA sequence not valid"
        id=self.get_new_id()
        self.id_and_name[id]=name
        self.sequence[id]=sequence
        self.name_and_id[name]=id
        sequence_json={"id":id,"name":name,"sequence":str(sequence)}
        return sequence_json

    def reenum_sequense(self):
        j=1
        for i in range(1,self.id+1):
            name=self.id_and_name.get(i)
            if name!=None:
                if j!=i:
                    self.id_and_name.pop(i)
                    self.id_and_name[j]=name
                    self.name_and_id[name]=j
                    seq=self.sequence.pop(i)
                    self.sequence[j]=seq
                j+=1

