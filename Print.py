class Print:
    def len_sequence(self,sequence):
        if len(sequence)>40:
            return sequence[:32]+"..."+sequence[-3:]
        return sequence
    def sequence(self,sequence_json):
        print(f'[{sequence_json["id"]}] {sequence_json["name"]}: {self.len_sequence(sequence_json["sequence"])}')
