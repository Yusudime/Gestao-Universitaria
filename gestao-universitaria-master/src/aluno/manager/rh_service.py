from src.aluno.base.funcionario import Funcionario
from src.cliente.irh_service import IRHService


class RHService(IRHService):

    def cadastrar(self, funcionario: Funcionario):
        self.funcionario =+ funcionario
        return self.funcionario

    def remover(self, cpf: str):
        CPF = cpf
        exit = input(print('digite o cpf q vc deseja'))
        if CPF == exit:
            del cpf
            return True
        else:
            print('CPF INVALIDO!!!')
            return False



    def obterFuncionario(self, cpf: str):
        if cpf != "a-z":
            self.cadastrar()
        else:
            print('CPF INVALIDO!!!')
            return False



    def getFuncionarios(self):
        return self.obterFuncionario()

    def getFuncionariosPorCategorias(self, tipo):
        if tipo == 1:
            self.tipo = 'professor'
            professor = input(print('diga a classe do professor:'))
            if professor == 'a':
                salario = 3000
                return salario
            elif professor == 'b':
                salario = 5000
                return salario
            elif professor == 'c':
                salario = 7000
                return salario
            elif professor == 'd':
                salario = 9000
                return salario
            elif professor == 'e':
                salario = 11000
                return salario
        elif tipo == 2:
            self.tipo = 'STAS'
            nivel= input(print("qual o nivel do STAS"))
            return nivel
        elif tipo == 3:
            self.tipo = 'TERC'
            insa = input(print('tem insabubridade'))
            if insa == 'sim':
                salario = 1500
                return salario
            else:
                salario = 1000
                return salario
        return self.tipo

    def getTotalFuncionarios(self):
        print(self.funcionario)
        return self.funcionario

    def solicitarDiaria(self, cpf: str):
        if cpf != "a-z":
            diaria = 100
            return diaria
        else:
            print('CPF INVALIDO!!!')
            return False
    def partilharLucros(self, valor: float):
       valor= valor/self.funcionario
        return valor

    def iniciarMes(self):
        pass

    def calcularSalarioDoFuncionario(self, cpf: str):
        if cpf != "a-z":
            if self.tipo() == 1:
                self.tipo = 'professor'
                professor = input(print('diga a classe do professor:'))
                if professor == 'a':
                    salario = 3000
                    return salario
                elif professor == 'b':
                    salario = 5000
                    return salario
                elif professor == 'c':
                    salario = 7000
                    return salario
                elif professor == 'd':
                    salario = 9000
                    return salario
                elif professor == 'e':
                    salario = 11000
                    return salario
        elif self.tipo == 2:
            self.tipo = 'STAS'
            nivel = input(print("qual o nivel do STAS"))
            return nivel
        elif self.tipo == 3:
            self.tipo = 'TERC'
            insa = input(print('tem insabubridade'))
              if insa == 'sim':
                 salario = 1500
                 return salario
              else:
                 salario = 1000
                 return salario



    def calcularFolhaDePagamento(self):
        print(self.calculasalarioDofuncionario())
        return self.calculasalarioDofuncionario()
