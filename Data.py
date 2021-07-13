import json

from DnaSequence import DnaSequence
from File import File


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
                print(self.data)
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


    def get_new_id(self):
        self.id +=1
        return self.id

    def get_new_name(self):
        self.name += 1
        self.updete="11"
        return "seq" + str(self.name)

    def get_id_by_name(self, name):
        try:
            return int(self.name_and_id[name])
        except:
            return False
        # for i in self.name_and_id.keys():
        #     if self.name_and_id[i] == name:
        #         return i
        # return False

    def get_name_by_id(self, id):
        try:
            return self.id_and_name[int(id)]
        except:
            return False

    # def get_sequence_by_id(self, id):
    #     for i in self.data:
    #         if i["id"] == id:
    #             return i["sequence"]
    #     return False

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
        # for i in self.data:
        #     if i[info] == value_info:
        #         return i["sequence"]
        # return False

    def get_id_by_sequence(self,sequence):
        for i in self.sequence.keys():
            if self.sequence[i] == sequence:
                return int(i)
        return False
    # def get_info_by_sequence(self,sequence,info="name"):
        # for i in self.data:
        #     if i["sequence"] == sequence:
        #         return i[info]
        # return False

    def valid_name(self, name):
        if name =="seq" + str(self.name) and self.updete[0]=="1":
            self.updete="01"
            return True
        if name in list(self.name_and_id.keys())+["seq" + str(self.name)]:
            return False
        if name=="seq" + str(self.name+1):
            self.name+=1
        return True
    def update_sequence_by_id(self,id,seq):
        self.sequence[int(id)]=seq
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
        #לעדכן את הדטה
        sequence_json={"id":id,"name":name,"sequence":str(sequence)}
        return sequence_json
# d=Data(File())
# # print(d.valid_name("AA"))
# print(d.add_sequence("seq","AAA"))
# print(d.add_sequence("seq1","AAAs"))
# print(d.add_sequence("3seq","AAA"))
# print(d.get_new_name())
# print(d.get_id_by_name("seq"))
# f=Data.getInstance()
# print(f.get_new_name())
