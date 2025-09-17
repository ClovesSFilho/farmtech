# Sistema de Agricultura
# Cloves Silva Filho
# RM 567250

# Armazenamento de dados
culturas = ["Milho", "Café"]
areas = [0, 0]
insumos = []

import pandas as pd
import os

def salvar_insumos():
    if len(insumos) == 0:
        print("⚠ Nenhum insumo para salvar.")
        return

    # Caminho seguro para salvar
    pasta_segura = os.path.join(os.path.expanduser("~"), "Documents")
    os.makedirs(pasta_segura, exist_ok=True)
    caminho_csv = os.path.join(pasta_segura, "insumos.csv")

    try:
        df = pd.DataFrame(insumos)
        df.to_csv(caminho_csv, index=False, encoding="utf-8")
        print(f"✅ Insumos salvos com sucesso em: {caminho_csv}")
    except Exception as e:
        print(f"❌ Erro ao salvar insumos: {e}")


while True:
    print("\n=== Sistema de Gestão da Lavoura ===")
    print("1 - Cadastrar área de plantio")
    print("2 - Cadastrar manejo de insumos")
    print("3 - Listar dados")
    print("4 - Atualizar área")
    print("5 - Deletar manejo de insumo")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")


    # 1. Cadastro da área de plantio
    if opcao == "1":
        while True:
            num = 1
            print("\nCulturas disponíveis:")
            for c in culturas:
                print(f"{num}. {c}")
                num += 1
            escolha = (input("Escolha a cultura: "))

            if escolha == "1" or escolha == "2":
                escolha = int(escolha)
                if escolha > 0 and escolha <= len(culturas):
                    print("Você escolheu:", culturas[escolha - 1])

                    while True:
                        tipo = input("O plantio é em (R)etângulo ou (T)rapézio? ").upper()
                        if tipo in ["R", "T"]:
                            break
                        else:
                            print("❌ Opção inválida! Digite R para Retângulo ou T para Trapézio.")

                    if tipo == "R":
                        while True:
                            try:
                                largura = float(input("Digite a largura do plantio (m): "))
                                if  largura > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        while True:
                            try:
                                comprimento = float(input("Digite o comprimento do plantio (m): "))
                                if  comprimento > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        area = largura * comprimento
                    else:  # Trapézio
                        while True:
                            try:
                                base_maior = float(input("Digite a base maior do trapézio (m): "))
                                if  base_maior > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        while True:
                            try:
                                base_menor = float(input("Digite a base menor do trapézio (m): "))
                                if  base_menor > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        while True:
                            try:
                                altura = float(input("Digite a altura do trapézio (m): "))
                                if  altura > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        area = ((base_maior + base_menor) / 2) * altura
                    areas[escolha - 1] = area
                    print(f"✅ Área de {culturas[escolha - 1]} cadastrada: {area} m²")
                    break
                else:
                    print("❌ Opção inválida! Tente novamente.")
            else:
                print("❌ Entrada inválida! Digite apenas números inteiros.")


    # 2. Cadastro de manejo de insumos
    elif opcao == "2":
        while True:
            num = 1
            print("\nCulturas disponíveis:")
            for c in culturas:
                print(f"{num}. {c}")
                num += 1
            escolha = (input("Escolha a cultura: "))
            if escolha == "1" or escolha == "2":
                escolha = int(escolha)
                if escolha > 0 and escolha <= len(culturas):
                    produto = input("Nome do insumo/produto: ")
                    while True:
                            try:
                                qtd_por_metro = float(input("Quantidade a aplicar por metro de rua: "))
                                if qtd_por_metro > 0:
                                    break
                                else:
                                    print("❌ A quantidade deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                    while True:
                            try:
                                ruas = int(input("Quantas ruas a lavoura tem? "))
                                if ruas > 0:
                                    break
                                else:
                                    print("❌ A quantidade deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                    total = qtd_por_metro * ruas
                    insumos.append({"cultura": culturas[escolha - 1], "produto": produto, "qtd_por_metro": qtd_por_metro, "ruas": ruas, "total": total})
                    print(f"✅ Manejo cadastrado: {produto} em {culturas[escolha - 1]} - Total: {total} mL")
                    salvar_insumos()
                    break
                else:
                    print("❌ Opção inválida! Tente novamente.")
            else:
                print("❌ Entrada inválida! Digite apenas números inteiros.")

    # 3. Listagem de dados
    elif opcao == "3":
        while True:
            num = 1
            print("\nCulturas disponíveis:")
            for c in culturas:
                print(f"{num}. {c}")
                num += 1
            escolha = (input("Escolha a cultura: "))
            if escolha == "1" or escolha == "2":
                print("\n=== Áreas de Plantio ===")
                for i in range(len(culturas)):
                    print(f"{culturas[i]}: {areas[i]} m²")

                print("\n=== Manejo de Insumos ===")
                if len(insumos) == 0:
                    print("Nenhum manejo cadastrado.")
                else:
                    num = 1
                    for i in insumos:
                        print(f"{num}. {i['produto']} - {i['cultura']} - Total: {i['total']} mL")
                        num += 1
            else:
                print("❌ Entrada inválida! Digite apenas números inteiros.")


    # 4. Atualização de áreas
    elif opcao == "4":
        while True:
            num = 1
            print("\nCulturas disponíveis:")
            for c in culturas:
                print(f"{num}. {c}")
                num += 1
            escolha = (input("Escolha a cultura: "))
            if escolha == "1" or escolha == "2":
                escolha = int(escolha)
                if escolha > 0 and escolha <= len(culturas):
                    print("Você escolheu:", culturas[escolha - 1])

                    while True:
                        tipo_novo = input("O novo plantio é em (R)etângulo ou (T)rapézio? ").upper()
                        if tipo_novo in ["R", "T"]:
                            break
                        else:
                            print("❌ Opção inválida! Digite R para Retângulo ou T para Trapézio.")

                    if tipo_novo == "R":
                        while True:
                            try:
                                largura = float(input("Digite a largura do plantio (m): "))
                                if  largura > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        while True:
                            try:
                                comprimento = float(input("Digite o comprimento do plantio (m): "))
                                if  comprimento > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        area = largura * comprimento
                    else:  # Trapézio
                        while True:
                            try:
                                base_maior = float(input("Digite a base maior do trapézio (m): "))
                                if  base_maior > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        while True:
                            try:
                                base_menor = float(input("Digite a base menor do trapézio (m): "))
                                if  base_menor > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        while True:
                            try:
                                altura = float(input("Digite a altura do trapézio (m): "))
                                if  altura > 0:
                                    break
                                else:
                                    print("❌ A largura deve ser maior que zero.")
                            except ValueError:
                                print("❌ Entrada inválida! Digite um número válido.")
                        area = ((base_maior + base_menor) / 2) * altura
                    areas[escolha - 1] = area
                    print(f"✅ Área de {culturas[escolha - 1]} cadastrada: {area} m²")
                    break
            else:
                print("❌ Opção inválida! Tente novamente.")


    # 5. Deletar manejo
    elif opcao == "5":
        if len(insumos) == 0:
            print("Não há manejos cadastrados para deletar.")
        else:
            num = 1
            print("\nManejos cadastrados:")
            for i in insumos:
                print(f"{num}. {i['produto']} - {i['cultura']} - Total: {i['total']} mL")
                num += 1

            while True:
                try:
                    indice = int(input("Escolha o número do manejo a deletar: "))
                    if 0 < indice <= len(insumos):
                        removido = insumos.pop(indice - 1)
                        salvar_insumos()
                        print(f"🗑 Manejo '{removido['produto']}' removido com sucesso!")
                        break
                    else:
                        print("❌ Índice inválido!")
                except ValueError:
                    print("❌ Entrada inválida! Digite um número válido.")


    # 6. Sair
    elif opcao == "6":
        print("👋 Saindo do programa... Até logo!")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")