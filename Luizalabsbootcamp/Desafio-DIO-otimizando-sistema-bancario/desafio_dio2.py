import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


# ==========================
# Função - LGPD
# ==========================

def mascarar_cpf(cpf: str) -> str:
    """
    Retorna o CPF mascarado - LGPD:
    Exemplo: 12345678901 -> 123.***.789-**
    """
    cpf = cpf.zfill(11)  # garante 11 dígitos
    return f"{cpf[0:3]}.***.{cpf[6:9]}-**"


# ==========================
# Domínio
# ==========================

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas: list[Conta] = []

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: "Conta"):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y")
        self.cpf = cpf


class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> "Conta":
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> "Historico":
        return self._historico

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False

        if valor > self._saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            print("\n@@@ Operação falhou! Valor excede limite. @@@")
            return False

        if numero_saques >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self) -> str:
        return (
            f"Agência:\t{self.agencia}\n"
            f"C/C:\t\t{self.numero}\n"
            f"Títular:\t{self.cliente.nome} ({mascarar_cpf(self.cliente.cpf)})"
        )


class Historico:
    def __init__(self):
        self._transacoes: list[dict] = []

    @property
    def transacoes(self) -> list[dict]:
        return self._transacoes

    def adicionar_transacao(self, transacao: "Transacao"):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# ==========================
# Interface (I/O)
# ==========================

def menu() -> str:
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf: str, clientes: list[Cliente]) -> Cliente | None:
    return next((c for c in clientes if c.cpf == cpf), None)


def recuperar_conta_cliente(cliente: Cliente) -> Conta | None:
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None

    for i, conta in enumerate(cliente.contas, start=1):
        print(f"[{i}] Conta {conta.numero} - Agência {conta.agencia}")

    escolha = int(input("Escolha a conta: "))
    return cliente.contas[escolha - 1]


def realizar_operacao(clientes: list[Cliente], tipo_transacao: type[Transacao]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor: "))
    transacao = tipo_transacao(valor)

    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes: list[Cliente]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    print(f"Títular: {conta.cliente.nome} ({mascarar_cpf(conta.cliente.cpf)})")
    print(f"Agência: {conta.agencia} | Conta: {conta.numero}")

    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in transacoes:
            print(f"{t['tipo']}:\n\tR$ {t['valor']:.2f} em {t['data']}")

    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes: list[Cliente]):
    cpf = input("Informe o CPF (somente número): ")
    if filtrar_cliente(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta: int, clientes: list[Cliente], contas: list[Conta]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero
