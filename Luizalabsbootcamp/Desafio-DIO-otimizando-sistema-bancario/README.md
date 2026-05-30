<img width="1001" height="157" alt="Captura de tela de 2025-11-30 14-53-13" src="https://github.com/user-attachments/assets/7739b94e-318f-4315-a38e-9a13c354d736" />


## 📌 Sobre o projeto
Este projeto foi desenvolvido como parte do desafio **"Otimizando o Sistema Bancário com Funções Python"**, cujo objetivo é melhorar a estrutura de um sistema bancário simples, aplicando **funções reutilizáveis** para organizar melhor o código e facilitar sua manutenção.

O sistema permite realizar operações básicas de um banco:
- Depósito  
- Saque  
- Extrato  
- Criação de usuário  
- Criação de conta  
- Listagem de contas  

---

## 🎯 Objetivo do desafio
O desafio propôs a otimização de um sistema bancário previamente criado, transformando suas operações em **funções específicas**.  
Isso trouxe benefícios como:
- **Organização**: cada operação isolada em uma função.  
- **Reutilização**: funções podem ser chamadas em diferentes partes do programa.  
- **Legibilidade**: código mais fácil de entender e manter.  
- **Eficiência**: fluxo mais claro e otimizado.  

---

## 🛠️ Tecnologias utilizadas
- **Python 3**  
- Biblioteca padrão (`textwrap`)  

---

## 📂 Estrutura do código
Principais funções implementadas:
- `depositar()` → responsável por depósitos.  
- `sacar()` → responsável por saques, com limite de valor e quantidade.  
- `exibir_extrato()` → mostra todas as movimentações e saldo atual.  
- `criar_usuario()` → cadastra novos usuários.  
- `filtrar_usuario()` → busca usuários pelo CPF.  
- `criar_conta()` → cria contas vinculadas a usuários.  
- `listar_contas()` → lista todas as contas criadas, exibindo CPF mascarado conforme LGPD.  

---

## 🔒 LGPD
Para proteger dados sensíveis, o CPF dos usuários é exibido de forma **mascarada** no extrato de contas, seguindo boas práticas da LGPD.  
Exemplo de saída:

```
Titular: João da Silva (123.***.789-**)
```

---

## ▶️ Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/TNSCloss/Desafio-DIO.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd Desafio-DIO
   ```
3. Execute o programa:
   ```bash
   python desafio_dio.py
   ```

---

## 📖 Exemplo de uso
```
=============== MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> d
Informe o valor do depósito: 100

=== Depósito realizado com sucesso! ===
```

---

## 🚀 Aprendizados
- Uso de funções posicionais e nomeadas (`/` e `*`).  
- Estruturação de código em funções reutilizáveis.  
- Boas práticas de programação em Python.  
- Aplicação de conceitos da **LGPD** para mascaramento de dados.  


