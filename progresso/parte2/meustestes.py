class Seila():
    def oloko(self):
        print('keissooooooo')


#instancia temporariamente e executa a func
Seila().oloko()

#somente usa a funcao sem instanciar nada
#porisso falta o self, pois nao tem instancia atual
#deve-se usar um staticmethod
Seila.oloko()