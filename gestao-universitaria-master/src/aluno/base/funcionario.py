class Funcionario:

    def getNome(self) -> str:
        nome = input(print('Digite seu nome'))
        return nome

    def getCpf(self) -> str:
        cpf = input(print('Digite seu cpf'))
        if cpf != "a-z":
            return cpf
        else:
            print('CPF INVALIDO!!!')
            return False

    def getSalario(self) -> float:

        return 0.0
