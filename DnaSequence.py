class DnaSequence:
    def __init__(self,dna):
        for i in dna:
            if i not in ["A","C","T","G"]:
                raise ValueError
        self.dna=dna

    def insert(self,nucleotide,index):
        if nucleotide not in ["A", "C", "T", "G"]:
            raise ValueError
        if index not in range(len(self.dna)):
            raise IndexError
        self.dna=self.dna[:index]+nucleotide+self.dna[index:]

    def assignment(self,another_dna):
         try:
            for i in another_dna:
                if i not in ["A","C","T","G"]:
                    raise ValueError
            self.dna = another_dna
         except:
            if type(another_dna)==type(self):
                self.dna=another_dna[:]
            else:
                raise ValueError
    def __str__(self):
        str=""
        for i in self.dna:
            str+=i
        return str
    def __getitem__(self, item):
        return self.dna[item]
    def __setitem__(self, key, value):
        if value not in ["A", "C", "T", "G"]:
            raise ValueError
        if key not in range(len(self.dna)):
            raise IndexError
        self.insert(value,key)
    def __len__(self):
        return len(self.dna)
    def __eq__(self, other):
        for i in range(len(self.dna)):
            if self.dna[i]!=other[i]:
                return False
        return True



# dna=DnaSequence("AAST")
dna=DnaSequence("AACT")
print(dna)
# dna.insert("A",8)
# dna.insert("g",2)
dna.insert("A",2)
print(dna)
# dna.assignment("AAAggCT")
dna.assignment("AACCCCT")
print(dna)
dna2=DnaSequence("AAGGGGGGG")
dna.assignment(dna2)
print(dna)
print(dna[2])
# dna[2]="l"
# dna[8]="T"
dna[2]="T"
print(dna)
print(len(dna))
print(dna=="wwww")
print(dna=="AATGGGGGGG")
