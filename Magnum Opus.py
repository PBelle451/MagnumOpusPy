class Nave(object):
    def __init__(self, frota, nome, serie, velocidade=''):
        self.frota = frota
        self.nome = nome
        self.serie = serie
        self.velocidade = velocidade
    def get_frota(self):
        return self.frota
    def set_frota(self, nova_frota):
        self.frota = nova_frota
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_serie(self):
        return self.serie
    def set_serie(self, nova_serie):
        self.serie = nova_serie
    def __str__(self):
        s = f'{self.get_frota(), self.get_nome(), self.get_serie()}'
        return s
    def get_velociade(self):
        return self.velocidade
    def set_velocidade(self, warp):
        if warp > 10:
            print("Barreira excedida")
        elif warp < 0:
            print("Velocidade inválida")
        self.velocidade = warp
if __name__ == '__main__':
    nave1 = Nave('USS', 'Enterprise', 'NCC-1701')
    nave2 = Nave('USS', 'Defiant', 'NCC-1764')
    nave1.set_nome('Minas Gerais')
    nave1.set_frota('FAEB')
    nave1.set_serie('TASM-0463')
    nave2.set_frota('FAEB')
    nave2.set_nome('São Paulo')
    nave2.set_serie('TIH-0185')
    print(nave1.get_nome())
    print(nave1.get_frota())
    print(nave1.get_serie())
    print(nave2.get_frota())
    print(nave2.get_nome())
    print(nave2.get_serie())
    print(nave1.__str__())
    print(nave2.__str__())
    nave1.set_velocidade(1)
    nave2.set_velocidade(5)
    print(f"A velocidade de dobra da {nave1.get_nome()} é: ", nave1.get_velociade())
    print(f"A velocidade de dobra da {nave2.get_nome()} é: ", nave2.get_velociade())