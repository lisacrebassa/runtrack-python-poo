class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def print_operation(self):
        print(f'le nombre 1 est {self.nombre1}')
        print(f'le nombre 1 est {self.nombre2}')

#permet d'instancier la classe 
operation1 = Operation(12,3)

#imprime l'operation
print(operation1.print_operation())