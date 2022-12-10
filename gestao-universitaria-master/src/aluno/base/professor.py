from funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        super.__init_subclass__(cpf, nome)
        self.classe = classe
