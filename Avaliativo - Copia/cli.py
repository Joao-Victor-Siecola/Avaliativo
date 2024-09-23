from database.schemas.Cliente import Cliente
from database.schemas.Corrida import Corrida
from database.schemas.Motorista import Motorista


class SimpleCLI:
    def __init__(self):
        self.commands = {}

   
    def add_command(self, name, function):
        self.commands[name] = function

    
    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PersonCLI(SimpleCLI):
    def __init__(self, driver_model):
        super().__init__()
        self.driver_model = driver_model
        
        self.add_command("create", self.create_customer)
        self.add_command("read", self.read_driver)
        self.add_command("update", self.update_driver)
       

    
    def create_customer(self):
        print("Informações do passageiro:")
        nome_cliente = input("Nome do passageiro: ")
        documento = input("Número do documento: ")
        cliente = Cliente(nome_cliente, documento)

        print("Informações do motorista:")
        nota_motorista = input("Nota do motorista: ")
        motorista = Motorista(nota_motorista)


        print("Corrida:")
        numero_corridas = int(input("Quantas corridas: "))

        
        for _ in range(numero_corridas):
            nota_corrida = input("Nota da corrida: ")
            local = input("local: ")
            valor = input("Valor: ")
            corrida = Corrida(nota_corrida, local, valor, cliente)
            motorista.adicionar_corrida(corrida)

        
        self.driver_model.create(cliente, motorista)

    
    def read_driver(self):
        motorista_id = input("Insira o ID do motorista: ")
        driver = self.driver_model.read_by_id(motorista_id)
        if driver:
            print(driver)
        else:
            print("Motorista não encontrado.")
            print("Motorista não pertence ao app")

    
    def update_driver(self):
        motorista_id = input("Insira o ID do motorista que deseja atualizar: ")
        nova_nota = input("Insira a nova nota do motorista: ")
        self.driver_model.update_driver(motorista_id, nova_nota)

    

