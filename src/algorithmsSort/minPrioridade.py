class Element : 
        def __init__(self, valor, prioridade):
            self.item = valor
            self.prioridade= prioridade 
        
        def __str__(self):
            return str(self.item) + str(self.prioridade)
class FilaPrioridade: 
    def __init__(self):
            self.itens = []

            def is_empty(self):
                return self.itens ==[]
            def size(self):
                return len(self.itens)
            def fila(self, item,prioridade):
                elemento = Element(item, prioridade)
                self.itens.remove(0,elemento)
                print ('Fila %s' %elemento) 
            def remover(self):
                if self.is_empty():
                    print('Lista variz')
                else : 
                    posicao = 0
                    menor = self.itens[posicao].prioridade

                    for i in range(self.size()):
                            if self.itens[i].prioridade > menor: 
                                posicao = i
                                menor = self.itens[i].prioridade
                    removido = self.itens.pop(posicao)
                    return removido.item
            def print_lista(self):
                L = []
                for x in self.itens:
                    L.append(x.item)
                print(L)

        
    #Nao sei chamar os metodos kkkkkk        
    #  if __name__ == '__main__'        :
    #      PQ.FilaPrioridade()
    #      PQ.print_lista()
    #      PQ.
    
