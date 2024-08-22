# Banco Simples em Python
Este repositório contém um programa simples de simulação bancária em Python feito para o bootcamp **NTT DATA - Engenharia de Dados com Python**. O código permite ao usuário realizar operações básicas como depósito, saque, e consulta de extrato bancário.

## Funcionalidades
- Depósito: Permite adicionar um valor à conta bancária.
- Saque: Permite retirar um valor da conta bancária, respeitando limites de saldo, valor por saque, e número máximo de saques diários.
- Extrato Bancário: Exibe o histórico das transações realizadas (depósitos e saques) e o saldo atual da conta.
- Sair: Encerra a execução do programa.
  
## Como Utilizar
1. Clone o repositório:
   ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
    cd nome-do-repositorio
   ```
3. Execute o script Python:
   ```bash
    python banco_simples.py
   ```
4. Interaja com o menu:
   
 Ao executar o script, o programa exibirá um menu com as seguintes opções:
 ```bash
  Escolha uma opção:

  [1] Depósito
  [2] Saque
  [3] Extrato Bancário
  [4] Sair
  => 
```
- [1] Depósito: Escolha essa opção para adicionar um valor à conta. O programa solicitará que você insira o valor do depósito.
- [2] Saque: Escolha essa opção para retirar um valor da conta. O programa solicitará que você insira o valor do saque. Note que há um limite de três saques diários e um limite máximo para o valor de saque.
- [3] Extrato Bancário: Escolha essa opção para visualizar o histórico de transações e o saldo atual da conta.
- [4] Sair: Escolha essa opção para encerrar o programa.

# Requisitos
- Python 3.6 ou superior

#  Exemplo de Uso
Após iniciar o programa, você verá o menu. Suponha que você queira fazer um depósito de R$100,00 e em seguida, consultar o extrato:
1. Escolha a opção 1 e insira 100 quando solicitado.
2. Escolha a opção 3 para visualizar o extrato. Ele mostrará o depósito realizado e o saldo atualizado.

# Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Basta seguir os passos abaixo:
1. Fork o repositório.
2. Crie uma nova branch para a sua feature ou correção:
```bash
  git checkout -b minha-feature
```
3. Commit suas mudanças:
```bash
git commit -m "Adicionei uma nova feature"
```
4. Envie as mudanças para o repositório remoto:
```bash
git push origin minha-feature
```
5. Abra um Pull Request.

# Licença
Este projeto está licenciado sob a [MIT License.](https://opensource.org/license/mit)
