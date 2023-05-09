class Calculator:

    def __init__(self):
        self.first_op = float(input("Alege primul operator:"))
        self.second_op = float(input("Alege al doilea operator:"))
        self.op = float(input("Alege operatoratorul:"))

    def adunare(self):
        return self.first_op + self.second_op

    def inmultire(self):
        return self.first_op * self.second_op

    def scadere(self):
        return self.first_op - self.second_op

    def impartire(self):
        if self.second_op != 0:
            return self.first_op / self.second_op
        else:
            return "Nu functioneaza"

    def __str__(self):
        if self.op == '-':
            return str(self.scadere())
        elif self.op == '+':
            return str(self.adunare())
        elif self.op == '*':
            return str(self.inmultire())
        else:
            return str(self.impartire())


obiect1 = Calculator()
obiect2 = Calculator()
obiect3 = Calculator()

print(obiect1)
print(obiect2)
print(obiect3)
