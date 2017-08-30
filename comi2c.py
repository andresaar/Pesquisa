import smbus
import time

class ComI2C:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.componentes = []
        self.achaComponentes()

    def __str__(self):
        string = ""
        for c in self.componentes:
            string += str(c) + " - " + str(c.endereco) + "\n"
        return string

    def novoComp(self):
        try:
            tipo = self.bus.read_byte(3)
            print ("Novo Componente Ativo\nFazendo mudanca de endereco...\n")
            if self.enderecosDisponiveis() == []:
                print ("Nao ha enderecos disponiveis!!")
                return 1
            endereco = self.enderecosDisponiveis()[0]
            self.bus.write_byte(3,endereco)
            print ("Novo componente no endereco " + str(endereco))
            self.bus.write_byte(endereco, 0)
            ID = self.bus.read_byte(endereco)
            for c in self.componentes:
                if c.ID == ID:
                    self.componentes.remove(c)
                    break
            novoComponente = Componente(ID, tipo, endereco)
            self.componentes.append(novoComponente)
            print(novoComponente)
            print("\n")
            return 0
        except:
            print("Sem novo componente\n")
            return 1

    def enderecosDisponiveis(self):
        enderecos = []
        for i in range(4,120):
            try:
                self.bus.read_byte(i)
            except:
                enderecos.append(i)
        return enderecos

    def achaComponentes(self):
        for i in range(4,120):
            try:
                self.bus.write_byte(i, 0)
                ID = self.bus.read_byte(i)
                for c in self.componentes:
                    if c.ID == ID:
                        pass
                self.bus.write_byte(i, 1)
                tipo = self.bus.read_byte(i)
                self.componentes.append(Componente(ID,tipo,i))
            except:
                pass



class Componente:
    def __init__(self, ID, tipo, endereco):
        self.ID = ID
        self.tipo = tipo
        self.endereco = endereco

    def __str__(self):
        return str(self.ID) + "/" + str(self.tipo)

