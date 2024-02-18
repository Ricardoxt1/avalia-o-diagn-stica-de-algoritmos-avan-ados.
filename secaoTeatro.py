class Teatro:
    def __init__(self, linhas, colunas, valor_ingresso):
        self.linhas = linhas
        self.colunas = colunas
        self.valor_ingresso = valor_ingresso
        self.total_cadeiras = linhas * colunas
        self.cadeiras = [['Livre' for _ in range(colunas)] for _ in range(linhas)]
        self.vendas = 0
        self.reservas = 0

    def iniciar_teatro(self):
        if self.vendas + self.reservas == 0:
            print("Teatro iniciado.")
        else:
            print("Não é possível iniciar o teatro enquanto houver espetáculo em andamento.")
        


    def reservar_lugar(self, linhas, colunas):
        if self.cadeiras[linhas][colunas] == 'Livre':
            self.cadeiras[linhas][colunas] = 'Reservado'
            self.reservas += 1
            print("Lugar reservado com sucesso!")
            menu()
            main()
        else:
            print("Este lugar já está reservado. Por favor, escolha outro.")
            main()


    def comprar_lugar(self, linhas, colunas):
        if self.cadeiras[linhas][colunas] == 'Livre':
            self.cadeiras[linhas][colunas] = 'Vendido'
            self.vendas += 1
            print("Lugar comprado com sucesso!")
            menu()
            main()
        elif self.cadeiras[linhas][colunas] == 'Reservado':
            self.cadeiras[linhas][colunas] = 'Vendido'
            self.reservas -= 1
            self.vendas += 1
            print("Lugar comprado com sucesso!")
            menu()
            main()
        else:
            print("Este lugar já está ocupado.")
            main()

    def liberar_lugar(self, linhas, colunas):
        if self.cadeiras[linhas][colunas] == 'Reservado':
            self.cadeiras[linhas][colunas] = 'Livre'
            self.reservas -= 1
            print("Reserva liberada com sucesso!")
            menu()
            main()
        elif self.cadeiras[linhas][colunas] == 'Vendido':
            self.cadeiras[linhas][colunas] = 'Livre'
            self.vendas -= 1
            print("Venda liberada com sucesso!")
            menu()
            main()
        else:
            print("Este lugar já está livre.")
            main()

    def listar_poltronas(self):
        total_livres = sum(row.count('Livre') for row in self.cadeiras)
        total_reservadas = sum(row.count('Reservado') for row in self.cadeiras)
        total_vendidas = sum(row.count('Vendido') for row in self.cadeiras)
        print(f"Total Geral de Cadeiras: {self.total_cadeiras}")
        print(f"Total de Cadeiras Vazias: {total_livres}")
        print(f"Total de Cadeiras Reservadas: {total_reservadas}")
        print(f"Total de Cadeiras Vendidas: {total_vendidas}")
        print(f"Total do Espetáculo em R$: {self.vendas * self.valor_ingresso:.2f}")
        print(f"Total não recebido em R$: {self.reservas * self.valor_ingresso * 0.3:.2f}")
        print(f"Total em reservas R$: {self.reservas * self.valor_ingresso * 0.7:.2f}")
        main()

    def encerrar_espetaculo(self):
        ocupacao_total = self.vendas + self.reservas
        if ocupacao_total >= 0.6 * self.total_cadeiras:
            print("Espetáculo encerrado.")
            self.listar_poltronas()
            self.reiniciar_espetaculo()
            menu()
            main()
        else:
            print("Não é possível encerrar o espetáculo, ocupação mínima não atingida.")
            main()

    def reiniciar_espetaculo(self):
        self.cadeiras = [['Livre' for _ in range(self.colunas)] for _ in range(self.linhas)]
        self.vendas = 0
        self.reservas = 0
        print("Espetáculo reiniciado.")
        menu()
        main()


def menu():
    print("=== Menu ===")
    print("[1] - Iniciar o teatro")
    print("[2] - Reservar lugar")
    print("[3] - Comprar lugar")
    print("[4] - Liberar lugar")
    print("[5] - Listar poltronas")
    print("[6] - Encerrar o espetáculo")
    print("[7] - Reiniciar o espetáculo")
    print("[0] - Sair")


def main():
  
    linhas = int(input("Selecione a fileira: "))
    colunas = int(input("Selecione a coluna: "))
    valor_ingresso = float(input("Selecione o valor do ingresso: "))

    teatro = Teatro(linhas, colunas, valor_ingresso)

    menu()
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            teatro.iniciar_teatro()
        case 2:
            linhas = int(input("Informe a linha da poltrona: "))
            colunas = int(input("Informe a coluna da poltrona: "))
            teatro.reservar_lugar(linhas, colunas)
        case 3:
            linhas = int(input("Informe a linha da poltrona: "))
            colunas = int(input("Informe a coluna da poltrona: "))
            teatro.comprar_lugar(linhas, colunas)
        case 4:
            linhas = int(input("Informe a linha da poltrona: "))
            colunas = int(input("Informe a coluna da poltrona: "))
            teatro.liberar_lugar(linhas, colunas)
        case 5:
            teatro.listar_poltronas()
        case 6:
            teatro.encerrar_espetaculo()
        case 7:
            teatro.reiniciar_espetaculo()
        case 0:
            print("Encerrando o programa.")
        case _:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


