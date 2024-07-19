class AlternaSinal(object):
    def __init__(self, valor):
        self.valor = valor

    def valor1(self):
            count = 0
            while count < self.valor:
                if count%2==0:
                    print(f"-{count} ", end="")
                else:
                    print(f"{count} ",end="")
                count += 1