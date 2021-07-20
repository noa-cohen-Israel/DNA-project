from Data import Data
from Parser import Parser


class Management:
    def __init__(self,command,string):
        self.command = command(string)

    def perform_action(self):
        self.command.run()
