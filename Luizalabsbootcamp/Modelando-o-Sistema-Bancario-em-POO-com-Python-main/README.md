# Sistema Bancário 🏦

![Imagem de Referência](https://github.com/Valmario/Modelando-o-Sistema-Bancario-em-POO-com-Python/blob/main/Refer%C3%AAncia.png)

Este repositório contém um sistema bancário simples desenvolvido em Python, utilizando os princípios de Programação Orientada a Objetos (POO). O projeto permite gerenciar clientes, contas bancárias, e realizar transações como depósitos, saques e visualização de extratos.

> 🚀 Projeto desenvolvido como parte do Bootcamp **Suzano - Python Developer** da [DIO](https://web.dio.me/track/suzano-python-developer), baseado no desafio proposto pela plataforma.

## 🔧 Funcionalidades

- ✅ **Criação de Clientes:** Cadastro de clientes com dados pessoais e endereço.
- ✅ **Abertura de Contas Bancárias:** Associadas aos clientes, com controle de saldo e histórico.
- ✅ **Depósitos e Saques:** Operações bancárias básicas com verificação de limites.
- ✅ **Extrato Bancário:** Listagem das transações realizadas na conta.

## 🧱 Estrutura do Projeto

O sistema é modularizado com classes que representam entidades reais do contexto bancário:

### 📦 Classes

| Classe           | Descrição |
|------------------|-----------|
| `Cliente`        | Representa um cliente do banco, contendo uma lista de contas. |
| `PessoaFisica`   | Subclasse de `Cliente` com nome, CPF e data de nascimento. |
| `Conta`          | Classe base para contas bancárias com saldo, número e agência. |
| `ContaCorrente`  | Subclasse de `Conta` com limites de saque e saldo negativo. |
| `Historico`      | Armazena o histórico de transações de uma conta. |
| `Transacao`      | Classe abstrata para operações bancárias. |
| `Saque`          | Representa uma transação de saque. |
| `Deposito`       | Representa uma transação de depósito. |

### ⚙️ Funções

| Função                      | Finalidade |
|-----------------------------|------------|
| `menu()`                    | Exibe o menu principal. |
| `filtrar_cliente()`         | Busca cliente por CPF. |
| `recuperar_conta_cliente()` | Retorna a conta associada ao cliente. |
| `depositar()`               | Realiza um depósito. |
| `sacar()`                   | Realiza um saque. |
| `exibir_extrato()`          | Mostra o extrato da conta. |
| `criar_cliente()`           | Cria um novo cliente. |
| `criar_conta()`             | Associa uma nova conta ao cliente. |
| `listar_contas()`           | Lista todas as contas cadastradas. |
| `main()`                    | Executa o sistema. |

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Valmario/Modelando-o-Sistema-Bancario-em-POO-com-Python.git
   ```

2. Acesse o diretório:
   ```bash
   cd Modelando-o-Sistema-Bancario-em-POO-com-Python
   ```

3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

4. Utilize o menu para navegar pelas opções do sistema.

## 📌 Requisitos

- Python 3.10 ou superior
- Terminal ou IDE compatível com execução de scripts Python

## 💡 Motivação

Este projeto foi desenvolvido com o objetivo de aplicar os conceitos de orientação a objetos aprendidos durante o bootcamp. Ele serve como um ponto de partida para soluções mais robustas e completas em sistemas bancários e administrativos.

## 🙌 Contribuições

Contribuições são muito bem-vindas! Se você encontrar algum bug, tiver sugestões de melhorias ou quiser adicionar novas funcionalidades, fique à vontade para abrir uma issue ou enviar um pull request.

---

## 🔗 Links Importantes

- 🔍 Desafio original: [Repositório oficial do desafio na DIO](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/01%20-%20Estrutura%20de%20dados/desafio.py)
- 💡 Meu repositório: [https://github.com/Valmario/Modelando-o-Sistema-Bancario-em-POO-com-Python](https://github.com/Valmario/Modelando-o-Sistema-Bancario-em-POO-com-Python)
- 📚 Bootcamp: [Suzano - Python Developer](https://web.dio.me/track/suzano-python-developer)
