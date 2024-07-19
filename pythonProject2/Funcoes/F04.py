class Area_Retangulo(object):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def perimetro(self):
        return (2*self.largura) + (2*self.altura)