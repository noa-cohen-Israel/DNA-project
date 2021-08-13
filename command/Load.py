class Load:
    def __init__(self,file_namme):
        self.receiver = "Create"
        self.name=file_namme

    def get_name(self):
        return self.name.split(".")[0]

    def get_sequence(self):
        try:
            with open(self.name) as f:
                return f.readline()
        except:
            print("load file failed")
            return False

    def getReceiver(self):
        return self.receiver

