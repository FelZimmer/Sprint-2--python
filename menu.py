import threading
import datetime
import json
import os

animais_chave = [
    "animal", "animais", "cachorro", "gato",
    "passaro", "pássaro", "cobra", "coelho",
    "hamster", "tigre", "leao", "leão",
    "urso", "macaco", "elefante", "girafa",
    "zebra", "lobo", "raposa", "papagaio",
    "peixe", "tartaruga", "cavalo", "vaca",
    "porco", "ovelha", "galinha", "pato",
    "coruja", "aguia", "águia", "jacare",
    "jacaré", "golfinho", "baleia", "pinguim"
]

natureza_chave = [
    "floresta", "montanha", "rio", "mar",
    "praia", "arvore", "árvore", "campo",
    "flores", "natureza", "céu", "ceu",
    "grama", "sol", "lua", "estrela",
    "cachoeira", "vento", "chuva", "tempestade",
    "nuvem", "deserto", "selva", "ilha",
    "oceano", "lago", "pedra", "vulcao",
    "vulcão", "neve", "trilha", "paisagem",
    "jardim", "folha", "plantas", "mata"
]

estudos_chave = [
    "livro", "caderno", "caneta", "lapis",
    "lápis", "lousa", "professor", "escola",
    "faculdade", "estudo", "matematica",
    "matemática", "mochila", "aluno", "universidade",
    "apostila", "prova", "lição", "licao",
    "atividade", "classe", "aula", "biblioteca",
    "quadro", "ensino", "curso", "redação",
    "redacao", "geografia", "historia", "história",
    "quimica", "química", "fisica", "física"
]

comida_chave = [
    "pizza", "hamburguer", "hambúrguer",
    "bolo", "comida", "macarrao", "macarrão",
    "lanche", "sushi", "café", "cafe",
    "sorvete", "refrigerante", "suco", "pastel",
    "batata", "batata frita", "chocolate",
    "doce", "biscoito", "cookie", "salada",
    "frango", "carne", "arroz", "feijao",
    "feijão", "torta", "coxinha", "brigadeiro",
    "pão", "pao", "queijo", "lasanha"
]

tecnologia_chave = [
    "computador", "notebook", "mouse",
    "teclado", "programacao", "programação",
    "codigo", "código", "celular", "monitor",
    "internet", "wifi", "wi-fi", "tablet",
    "smartphone", "servidor", "processador",
    "memoria", "memória", "hardware", "software",
    "inteligencia artificial", "ia", "chatbot",
    "site", "aplicativo", "app", "linux",
    "windows", "android", "iphone", "javascript",
    "python", "java", "banco de dados", "rede"
]

def limpar():
    try:
        os.system("cls")
    except:
        os.system("clear")

def carregar_dados():
    try:
        with open("galeria.json", "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def salvar_dados(dados):
    try:
        with open("galeria.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def menu():
    print("\nBem vindo à galeria do seu celular!\n")
    print("1 - Ver galeria")
    print("2 - Procurar foto")
    print("3 - Adicionar foto")
    print("4 - Excluir foto")
    print("5 - Foto temporária")
    print("6 - Ver fotos antigas")
    print("0 - Sair")

def menu_pesquisa():
    print("\nPesquisar por: \n")
    print("1 - Nome / Descrição")
    print("2 - Categoria")

def menu_categoria():
    print("\nCategorias: \n")
    print("1 - Animais")
    print("2 - Natureza")
    print("3 - Estudos")
    print("4 - Comida")
    print("5 - Tecnologia")
    print("6 - Outros")

def menu_temporaria():
    print("\nFoto Temporária\n")
    print("1 - 1 dia")
    print("2 - 1 semana")
    print("3 - 1 mês")
    print("4 - 1 ano")
    print("5 - 15 segundos")

def galeria():
    dados = carregar_dados()

    if not dados["fotos"]:
        print("Galeria vazia.")
        return

    for foto in dados["fotos"]:
        print(
            f"\nFoto: {foto['foto'].capitalize()}"
            f"\nDescrição: {foto['descricao'].capitalize()}"
            f"\nCategoria: {foto['categoria'].capitalize()}"
            f"\nData: {foto['data']}"
            f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
            f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
        )

def procurar_foto():
    dados = carregar_dados()
    menu_pesquisa()
    try:
        match int(input("Digite o número: ")):
            case 1:
                
                busca = input("Digite o nome ou descrição da foto: ").lower()

                encontrada = False

                for foto in dados["fotos"]:

                    nome = foto.get("foto", "").lower()
                    descricao = foto.get("descricao", "").lower()

                    if busca in nome or busca in descricao:

                        print(
                        f"\nFoto: {foto['foto'].capitalize()}"
                        f"\nDescrição: {foto['descricao'].capitalize()}"
                        f"\nCategoria: {foto['categoria'].capitalize()}"
                        f"\nData: {foto['data']}"
                        f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                        f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
                        )

                        encontrada = True

                if not encontrada:
                    print("Nenhuma foto encontrada.")

            case 2:
                menu_categoria()

                match int(input("Digite o número correspondente à categoria desejada: ")):
                    case 1:
                        if not dados["fotos"]:
                            print("Galeria vazia.")
                            return

                        for foto in dados["fotos"]:
                            if foto["categoria"] == "animal":
                                print(
                                    f"\nFoto: {foto['foto'].capitalize()}"
                                    f"\nDescrição: {foto['descricao'].capitalize()}"
                                    f"\nCategoria: {foto['categoria'].capitalize()}"
                                    f"\nData: {foto['data']}"
                                    f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                                    f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
                                )
                    case 2:
                        if not dados["fotos"]:
                            print("Galeria vazia.")
                            return

                        for foto in dados["fotos"]:
                            if foto["categoria"] == "natureza":
                                print(
                                    f"\nFoto: {foto['foto'].capitalize()}"
                                    f"\nDescrição: {foto['descricao'].capitalize()}"
                                    f"\nCategoria: {foto['categoria'].capitalize()}"
                                    f"\nData: {foto['data']}"
                                    f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                                    f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
                                )
                    case 3:
                        if not dados["fotos"]:
                            print("Galeria vazia.")
                            return

                        for foto in dados["fotos"]:
                            if foto["categoria"] == "estudos":
                                print(
                                    f"\nFoto: {foto['foto'].capitalize()}"
                                    f"\nDescrição: {foto['descricao'].capitalize()}"
                                    f"\nCategoria: {foto['categoria'].capitalize()}"
                                    f"\nData: {foto['data']}"
                                    f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                                    f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
                                )
                    case 4:
                        if not dados["fotos"]:
                            print("Galeria vazia.")
                            return

                        for foto in dados["fotos"]:
                            if foto["categoria"] == "comida":
                                print(
                                    f"\nFoto: {foto['foto'].capitalize()}"
                                    f"\nDescrição: {foto['descricao'].capitalize()}"
                                    f"\nCategoria: {foto['categoria'].capitalize()}"
                                    f"\nData: {foto['data']}"
                                    f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                                    f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
                                )
                    case 5:
                        if not dados["fotos"]:
                            print("Galeria vazia.")
                            return

                        for foto in dados["fotos"]:
                            if foto["categoria"] == "tecnologia":
                                print(
                                    f"\nFoto: {foto['foto'].capitalize()}"
                                    f"\nDescrição: {foto['descricao'].capitalize()}"
                                    f"\nCategoria: {foto['categoria'].capitalize()}"
                                    f"\nData: {foto['data']}"
                                    f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                                    f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
                                )
                    case 6:
                        if not dados["fotos"]:
                            print("Galeria vazia.")
                            return

                        for foto in dados["fotos"]:
                            if foto["categoria"] == "outros":
                                print(
                                    f"\nFoto: {foto['foto'].capitalize()}"
                                    f"\nDescrição: {foto['descricao'].capitalize()}"
                                    f"\nCategoria: {foto['categoria'].capitalize()}"
                                    f"\nData: {foto['data']}"
                                    f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                                    f"\nTempo de vida: {'---' if foto['tempo_vida'] is None else f'{foto['tempo_vida']} segundos'}"
                                )
            case _:
                print("Opção inválida.")
                return

    except ValueError:
        print("Digite apenas números.")
    
def detectar_categoria(nome, descricao):

    texto = f"{nome} {descricao}".lower()

    categorias = {
        "animal": animais_chave,
        "natureza": natureza_chave,
        "estudos": estudos_chave,
        "comida": comida_chave,
        "tecnologia": tecnologia_chave
    }

    for categoria, palavras in categorias.items():

        for palavra in palavras:

            if palavra in texto:
                return categoria

    return "outros"

def adicionar_foto(nome, descricao, is_temporaria=False, tempo_vida=None):

    dados = carregar_dados()

    for foto in dados["fotos"]:

        if nome.lower() == foto["foto"].lower():
            print("Erro: Já existe uma foto com esse nome.")
            return

    nova_foto = {
        "foto": nome,
        "descricao": descricao,
        "data": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        "is_temporaria": is_temporaria,
        "tempo_vida": tempo_vida,
        "categoria": detectar_categoria(nome, descricao)
    }

    dados["fotos"].append(nova_foto)

    salvar_dados(dados)

    print("Foto adicionada com sucesso!")

def excluir_foto():

    dados = carregar_dados()

    nome = input("Digite o nome da foto que deseja excluir: ").lower()

    for foto in dados["fotos"]:

        if nome == foto["foto"].lower():

            dados["fotos"].remove(foto)

            salvar_dados(dados)

            print("Foto excluída com sucesso!")
            return

    print("Foto não encontrada.")

def remover_foto(nome):

    dados = carregar_dados()

    for foto in dados["fotos"]:

        if foto["foto"] == nome:

            dados["fotos"].remove(foto)

            salvar_dados(dados)

            print(f"\nFoto '{nome}' removida automaticamente!")
            return

def foto_temporaria():

    nome = input("Digite o nome da foto temporária: ")
    descricao = input("Digite a descrição da foto temporária: ")

    menu_temporaria()

    try:
        match int(input("Digite o número: ")):
            case 1:
                segundos = 86400
            case 2:
                segundos = 604800
            case 3:
                segundos = 2592000
            case 4:
                segundos = 31536000
            case 5:
                segundos = 15
            case _:
                print("Opção inválida.")
                return

        adicionar_foto(nome, descricao, True, segundos)

        temporizador = threading.Timer(
            segundos,
            lambda: remover_foto(nome)
        )

        temporizador.start()

    except ValueError:
        print("Digite apenas números.")

def calcular_tempo_vida():

    dados = carregar_dados()

    if not dados["fotos"]:
        print("Nenhuma foto cadastrada.")
        return

    print("\n FOTOS ANTIGAS \n")

    for foto in dados["fotos"]:

        data_atual = datetime.datetime.now()

        data_foto = datetime.datetime.strptime(
            foto["data"],
            "%d-%m-%Y %H:%M"
        )

        diferenca = (data_atual - data_foto).days

        if diferenca >= 365:
            tempo = diferenca // 365
            tempo = f"Mais de {tempo} ano(s)"

        elif diferenca >= 180:
            tempo = "Mais de 6 meses"

        elif diferenca >= 90:
            tempo = "Mais de 3 meses"

        else:
            continue

        print(
            f"\nFoto: {foto['foto'].capitalize()}"
            f"\nDescrição: {foto['descricao'].capitalize()}"
            f"\nTempo armazenado: {tempo}"
        )

while True:

    limpar()

    menu()

    try:
        opcao = int(input("\nDigite uma opção: "))

        match opcao:

            case 1:
                galeria()

            case 2:
                procurar_foto()

            case 3:
                nome = input("Digite o nome da foto: ")
                descricao = input("Digite a descrição da foto: ")

                adicionar_foto(nome, descricao)

            case 4:
                excluir_foto()

            case 5:
                foto_temporaria()

            case 6:
                calcular_tempo_vida()

            case 0:
                print("Encerrando sistema...")
                break

            case _:
                print("Opção inválida.")

    except ValueError:
        print("Digite apenas números.")

    input("\nPressione ENTER para continuar...")