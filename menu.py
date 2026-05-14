import threading
import datetime
import json

animais_chave = [
    "animal", "animais", "cachorro", "gato",
    "passaro", "pássaro", "cobra", "coelho",
    "hamster", "tigre", "leao", "leão",
    "urso", "macaco"
]

natureza_chave = [
    "floresta", "montanha", "rio", "mar",
    "praia", "arvore", "árvore", "campo",
    "flores", "natureza", "céu", "ceu",
    "grama", "sol"
]

estudos_chave = [
    "livro", "caderno", "caneta", "lapis",
    "lápis", "lousa", "professor", "escola",
    "faculdade", "estudo", "matematica",
    "matemática", "mochila"
]

comida_chave = [
    "pizza", "hamburguer", "hambúrguer",
    "bolo", "comida", "macarrao", "macarrão",
    "lanche", "sushi", "café", "cafe"
]

tecnologia_chave = [
    "computador", "notebook", "mouse",
    "teclado", "programacao", "programação",
    "codigo", "código", "celular", "monitor"
]


def menu():
    print("\nBem vindo à galeria do seu celular!\n")
    print("1 - Ver galeria\n")
    print("2 - Procurar foto\n")
    print("3 - Adicionar foto\n")
    print("4 - Excluir foto\n")
    print("5 - foto temporaria\n")


def menu_temporaria():
    print("\nEscolha uma opção de foto temporária: \n")
    print("1 - Em um dia\n")
    print("2 - Uma semana \n")
    print("3 - Um mês\n")
    print("4 - Um ano\n")
    print("5 - 15 segundos\n")


def galeria():
    try:
        with open('galeria.json', "r", encoding="utf-8") as f:
            dados = json.load(f)

            for i in dados["fotos"]:
                print(
                    f" Foto: {i['foto']} - Descrição: {i['descricao']} - Categoria: {i['categoria']} - Data: {i['data']} - Temporária: {i['is_temporaria']} - Tempo de vida: {i['tempo_vida']}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def procurar_foto():
    try:
        with open('galeria.json', "r", encoding="utf-8") as f:
            dados = json.load(f)

        fotos = dados["fotos"]

        busca = input("Digite o nome da foto: ").lower()

        encontrada = False

        for foto in fotos:

            nome = str(foto.get("foto", "")).lower()
            descricao = str(foto.get("descricao", "")).lower()

            if busca == nome or busca == descricao:
                print(
                    f"\nFoto: {foto.get('foto', 'N/A')} | "
                    f"Descrição: {foto.get('descricao', 'N/A')} | "
                    f"Data: {foto.get('data', 'N/A')} | "
                    f"Temporária: {foto.get('is_temporaria', False)} | "
                    f"Tempo de vida: {foto.get('tempo_vida', 'N/A')}"
                )

                encontrada = True
                break

        if not encontrada:
            print("Nenhuma foto encontrada.")

        return

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return


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


def adicionar_foto():
    try:
        while True:
            with open('galeria.json', "r", encoding="utf-8") as f:
                fotos = json.load(f)

            nome = str(input("Digite o nome da foto: ")).lower()
            existe = False

            for i in fotos["fotos"]:
                if nome == i['foto'].lower():
                    print("Foto já existe!")
                    existe = True
                    break

            if existe:
                print("Erro: Já existe uma foto com esse nome!")
                break

            else:
                descricao = str(input("Digite a descrição da foto: "))

                fotos["fotos"].append({
                    "foto": nome,
                    "descricao": descricao,
                    "data": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
                    "is_temporaria": False,
                    "tempo_vida": None,
                    "categoria": detectar_categoria(nome, descricao)
                })
                print("Foto tirada com sucesso!")

            with open('galeria.json', "w", encoding="utf-8") as f:
                json.dump(fotos, f, ensure_ascii=False, indent=4)
                print("Foto tirada com sucesso!")
            break
        return

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def excluir_foto():
    try:

        with open('galeria.json', "r", encoding="utf-8") as f:
            fotos = json.load(f)

        nome = str(input("Digite o nome da foto que deseja excluir: ")).lower()
        for i in fotos["fotos"]:
            if nome == i['foto'].lower():
                fotos["fotos"].remove(i)
                print("Foto excluída com sucesso")

        with open('galeria.json', "w", encoding="utf-8") as f:
            json.dump(fotos, f, ensure_ascii=False, indent=4)

            return
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def remover_foto(nome):
    with open("galeria.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    fotos = dados["fotos"]

    for foto in fotos:
        if foto["foto"] == nome:
            fotos.remove(foto)
            break

    with open("galeria.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print(f"Foto '{nome}' removida!")


def foto_temporaria():
    try:
        with open('galeria.json', "r", encoding="utf-8") as f:
            dados = json.load(f)

        nome = input("Digite o nome da foto temporária: ")
        descricao = input("Digite a descrição da foto temporária: ")

        menu_temporaria()

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

        dados["fotos"].append({
            "foto": nome,
            "descricao": descricao,
            "data": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            "is_temporaria": True,
            "tempo_vida": segundos,
            "categoria": detectar_categoria(nome, descricao)

        })

        with open('galeria.json', "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

        print("Foto temporária adicionada com sucesso!")

        temporizador = threading.Timer(
            segundos,
            lambda: remover_foto(nome)
        )

        temporizador.start()


    except Exception as e:
        print(f"Ocorreu um erro: {e}")

lista_tres_meses = {}
lista_seis_meses = {}
lista_ano = {}

def calcular_tempo_vida():
    with open('galeria.json', "r", encoding="utf-8") as f:
        dados = json.load(f)
    for i in dados["fotos"]:
        data_agr = datetime.datetime.now()
        data_foto = datetime.datetime.strptime(i["data"], "%d-%m-%Y %H:%M")

        delta = data_agr - data_foto
        diferenca = delta.days
        print(diferenca)
        if diferenca >= 90:
            lista_tres_meses['foto', 'descricao']= i["foto"], i["descricao"]
            print(lista_tres_meses)
        elif diferenca >= 180:
            lista_seis_meses['foto', 'descricao'] = i["foto"], i["descricao"]
            print(lista_seis_meses)
        elif diferenca >= 365:
            lista_ano['foto', 'descricao'] = i["foto"], i["descricao"]
            print(lista_ano)
        else:
            continue

    return diferenca

while True:
    ## ...
    menu()
    match int(input("digite o seu numero:")):
        case 1:
            galeria()
        case 2:
            procurar_foto()
        case 3:
            adicionar_foto()
        case 4:
            excluir_foto()
        case 5:
            foto_temporaria()
        case 6:
            calcular_tempo_vida()
        case _:
            # adicionar um if else para tratar erros
            print("Opção inválida, tente novamente.")
