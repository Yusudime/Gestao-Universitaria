from abc import ABC, abstractmethod

from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class IRHService(ABC):
    @abstractmethod
    def cadastrar(self, funcionario: Funcionario) -> bool:
        self.funcionario = + funcionario
        return self.funcionario

    @abstractmethod
    def remover(self, cpf: str) -> bool:
        CPF = cpf
        exit = input(print('digite o cpf q vc deseja'))
        if CPF == exit:
            del cpf
            return True
        else:
            print('CPF INVALIDO!!!')
            return False


    @abstractmethod
    def obterFuncionario(self, cpf: str) -> Funcionario:
        if cpf != "a-z":
            self.cadastrar()
        else:
            print('CPF INVALIDO!!!')
            return False

    @abstractmethod
    def getFuncionarios(self) -> list:
        return self.obterFuncionario()

    @abstractmethod
    def getFuncionariosPorCategorias(self, tipo: Tipo) -> list:
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
            nivel = input(print("qual o nivel do STAS"))
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

    @abstractmethod
    def getTotalFuncionarios(self) -> int:
        print(self.funcionario)
        return self.funcionario
    @abstractmethod
    def solicitarDiaria(self, cpf: str) -> bool:
        if cpf != "a-z":
            diaria = 100
            return diaria
        else:
            print('CPF INVALIDO!!!')
            return False
    @abstractmethod
    def partilharLucros(self, valor: float) -> bool:
         valor= valor/self.funcionario
         return valor
    @abstractmethod
    def iniciarMes(self):
        pass

    @abstractmethod
    def calcularSalarioDoFuncionario(self, cpf: str) -> float:
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
    @abstractmethod
    def calcularFolhaDePagamento(self) -> float:
        print(self.calculasalarioDofuncionario())
        return self.calculasalarioDofuncionario()
