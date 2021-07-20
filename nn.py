class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance(var):
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton(var)
        return Singleton.__instance

    def __init__(self,var):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.var=var
            Singleton.__instance = self
    def get(self):
        return self.var

# A little testing

s = Singleton(4) # Ok
#Singleton() # will raise exception
print (s.get())

s = Singleton.getInstance(2)
print (s.get())

s = Singleton.getInstance(3)
print (s.get()) # will print the same instance as before