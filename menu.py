import threading
import datetime
import json
import os

# Listas de palavras-chave para detecção automática de categorias

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

# Mapeamento das categorias para facilitar a seleção nos menus
CATEGORIAS = {
    1: "animais",
    2: "natureza",
    3: "estudos",
    4: "comida",
    5: "tecnologia",
    6: "outros"
}

# Limpa o terminal
def limpar():
    os.system("cls" if os.name == "nt" else "clear")    

# Carrega os dados do arquivo JSON
def carregar_dados():
    default = {"fotos": [], "lixeira": []}
    if not os.path.exists("galeria.json"):
        return default
    try:
        with open("galeria.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return default

# Salva o dicionário de dados no arquivo JSON
def salvar_dados(dados):
    try:
        with open("galeria.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

# Funções de menus
def menu():
    print("\nBem vindo à galeria do seu celular!\n")
    print("1 - Ver galeria")
    print("2 - Procurar foto")
    print("3 - Adicionar foto")
    print("4 - Excluir foto")
    print("5 - Foto temporária")
    print("6 - Ver fotos antigas")
    print("7 - Ver Lixeira")
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

# Mostra todas as fotos na galeria

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
            f"\nTempo de vida: {f"{foto['tempo_vida']} segundos" if foto['tempo_vida'] != None else "---"}"
        )

# Interface da lixeira: permite ver, recuperar ou limpar lixeira
def lixeira():
    dados = carregar_dados()

    if not dados["lixeira"]:
        print("Lixeira vazia.")
        return

    for foto in dados["lixeira"]:
        print(
            f"\nFoto: {foto['foto'].capitalize()}"
            f"\nDescrição: {foto['descricao'].capitalize()}"
            f"\nCategoria: {foto['categoria'].capitalize()}"
            f"\nData: {foto['data']}"
            f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
            f"\nTempo de vida: {f"{foto['tempo_vida']} segundos" if foto['tempo_vida'] != None else "---"}"
        )
    
    print("\nOpções:")
    print("1 - Esvaziar lixeira")
    print("2 - Recuperar item da lixeira")
    print("3 - Voltar para o menu")
    
    try:
        opcao = int(input("Digite o número: "))
        if opcao == 1:
            dados["lixeira"].clear()
            salvar_dados(dados)
            print("Lixeira esvaziada.")
        elif opcao == 2:
            nome = input("Digite o nome da foto que deseja recuperar: ").lower()
            foto_recuperada = None
            for foto in dados["lixeira"]:
                if foto["foto"].lower() == nome:
                    foto_recuperada = foto
                    break
            
            if foto_recuperada:
                dados["fotos"].append(foto_recuperada)
                dados["lixeira"].remove(foto_recuperada)
                salvar_dados(dados)
                print(f"Foto '{nome}' recuperada com sucesso!")
            else:
                print("Foto não encontrada na lixeira.")
        elif opcao == 3:
            return
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite apenas números.")
        

def procurar_foto():

    dados = carregar_dados()

    if not dados["fotos"]:
        print("Galeria vazia.")
        return

    menu_pesquisa()

    try:

        match int(input("Digite o número: ")):
            case 1:
                busca = input(
                    "Digite o nome ou descrição da foto: "
                ).lower()

                encontrada = False

                for foto in dados["fotos"]:

                    nome = foto['foto'].lower()
                    descricao = foto['descricao'].lower()

                    if busca in nome or busca in descricao:
                        tempo = f"{foto['tempo_vida']} segundos" if foto['tempo_vida'] != None else "---"
                        print(
                            f"\nFoto: {foto['foto'].capitalize()}"
                            f"\nDescrição: {foto['descricao'].capitalize()}"
                            f"\nCategoria: {foto['categoria'].capitalize()}"
                            f"\nData: {foto['data']}"
                            f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                            f"\nTempo de vida: {tempo}"
                        )
                        encontrada = True

                if not encontrada:
                    print("Nenhuma foto encontrada.")

            case 2:
                menu_categoria()
                try:
                    cat_num = int(input("Digite o número correspondente à categoria desejada: "))
                    if cat_num not in CATEGORIAS:
                        print("Opção de categoria inválida.")
                        return
                    categoria_escolhida = CATEGORIAS[cat_num]
                    encontrada = False
                    for foto in dados["fotos"]:
                        if foto["categoria"] == categoria_escolhida:
                            tempo = f"{foto['tempo_vida']} segundos" if foto['tempo_vida'] != None else "---"
                            print(
                                f"\nFoto: {foto['foto'].capitalize()}"
                                f"\nDescrição: {foto['descricao'].capitalize()}"
                                f"\nCategoria: {foto['categoria'].capitalize()}"
                                f"\nData: {foto['data']}"
                                f"\nTemporária: {'Sim' if foto['is_temporaria'] else 'Não'}"
                                f"\nTempo de vida: {tempo}"
                            )
                            encontrada = True
                    
                    if not encontrada:
                        print(f"Nenhuma foto encontrada na categoria '{categoria_escolhida}'.")
                except ValueError:
                    print("Digite apenas números.")
            case _:
                print("Opção inválida.")
    except ValueError:
        print("Digite apenas números.")
    
# Analisa o nome e descrição para definir uma categoria automaticamente
def detectar_categoria(nome, descricao):

    texto = f"{nome} {descricao}".lower()

    categorias = {
        "animais": animais_chave,
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

# Adiciona uma nova foto na galeria
def adicionar_foto(nome, descricao, is_temporaria=False, tempo_vida=None):
    dados = carregar_dados()
    
    for foto in dados["fotos"]:
        if nome.lower() == foto["foto"].lower():
            print("Erro: Já existe uma foto com esse nome.")
            return

    agora = datetime.datetime.now()
    expira_em = None
    
    # Verifica se a foto é temporária e calcula o momento da expiração
    if is_temporaria and tempo_vida:
        expira_em = (agora + datetime.timedelta(seconds=tempo_vida)).strftime("%d-%m-%Y %H:%M")

    nova_foto = {
        "foto": nome.lower(),
        "descricao": descricao,
        "data": agora.strftime("%d-%m-%Y %H:%M"),
        "is_temporaria": is_temporaria,
        "tempo_vida": tempo_vida,
        "expira_em": expira_em,
        "categoria": detectar_categoria(nome, descricao)
    }

    dados["fotos"].append(nova_foto)
    salvar_dados(dados)
    print("Foto adicionada com sucesso!")

# Verifica se alguma foto temporária expirou e move para a lixeira
def verificar_temporarias():
    dados = carregar_dados()
    agora = datetime.datetime.now()
    remover = []
    
    for foto in dados["fotos"]:
        if foto["is_temporaria"] == True and foto["expira_em"] != None:
            expiracao = datetime.datetime.strptime(foto["expira_em"], "%d-%m-%Y %H:%M")
            if agora >= expiracao:
                remover.append(foto)
    
    # Se houver fotos expiradas, move para a lixeira e salva o arquivo
    if remover:
        for foto in remover:
            dados["fotos"].remove(foto)
            dados["lixeira"].append(foto)
        salvar_dados(dados)
        print(f"\n{len(remover)} fotos temporárias expiraram e foram apagadas.")

def excluir_foto(nome, mensagem=None, salvar=True):
    dados = carregar_dados()
    foto_para_remover = None
    for foto in dados["fotos"]:
        if foto["foto"].lower() == nome.lower():
            foto_para_remover = foto
            break
    
    if foto_para_remover:
        dados["fotos"].remove(foto_para_remover)
        dados["lixeira"].append(foto_para_remover)
        if salvar:
            salvar_dados(dados)
        if mensagem:
            print(mensagem)
        return True
    return False

def foto_temporaria():

    nome = input("Digite o nome da foto temporária: ")
    descricao = input("Digite a descrição da foto temporária: ")
    mensagem = f"\nFoto '{nome}' excluída com sucesso!"
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
            lambda: excluir_foto(nome, mensagem)
        )

        temporizador.start()

    except ValueError:
        print("Digite apenas números.")

# Analisa e exibe fotos com base no tempo que estão armazenadas
def calcular_tempo_vida():

    dados = carregar_dados()

    if not dados["fotos"]:
        print("Nenhuma foto cadastrada.")
        return

    print("\nFOTOS ANTIGAS\n")

    encontrou_foto_antiga = False

    for foto in dados["fotos"]:
        data_atual = datetime.datetime.now()
        try:
            data_foto = datetime.datetime.strptime(foto["data"], "%d-%m-%Y %H:%M")
        except ValueError:
            print(f"Erro ao converter data da foto '{foto['foto']}'.")
            continue

        diferenca = (data_atual - data_foto).days

        # Classifica a "idade" da foto
        if diferenca >= 365:
            anos = diferenca // 365
            tempo = f"Mais de {anos} ano(s)"
        elif diferenca >= 180:
            tempo = "Mais de 6 meses"
        elif diferenca >= 90:
            tempo = "Mais de 3 meses"
        else:
            continue

        encontrou_foto_antiga = True
        print(
            f"\nFoto: {foto['foto'].capitalize()}"
            f"\nDescrição: {foto['descricao'].capitalize()}"
            f"\nCategoria: {foto['categoria'].capitalize()}"
            f"\nData: {foto['data']}"
            f"\nTempo armazenado: {tempo}"
        )

    if not encontrou_foto_antiga:
        print("Nenhuma foto antiga encontrada.")
        return
    print("\nDeseja apagar as fotos com mais de 1 ano de armazenamento?\n1 - Sim\n2 - Não")
    try:
        escolha = int(input("Digite o número: "))
        if escolha == 1:
            menu_categoria()
            try:
                cat_num = int(input("Digite o número da categoria que deseja excluir: "))
                if cat_num not in CATEGORIAS:
                    print("Categoria inválida.")
                    return
                categoria_alvo = CATEGORIAS[cat_num]
                removidas = 0
                for foto in dados["fotos"]:
                    try:
                        data_foto = datetime.datetime.strptime(foto["data"], "%d-%m-%Y %H:%M")
                        diferenca = (datetime.datetime.now() - data_foto).days
                        
                        if diferenca >= 365 and foto["categoria"] == categoria_alvo:
                            dados["fotos"].remove(foto)
                            dados["lixeira"].append(foto)
                            removidas += 1
                    except ValueError:
                        continue
                
                if removidas > 0:
                    salvar_dados(dados)
                    print(f"\n{removidas} foto(s) da categoria '{categoria_alvo}' movida(s) para a lixeira.")
                else:
                    print(f"Nenhuma foto com mais de 1 ano encontrada na categoria '{categoria_alvo}'.")
                        
            except ValueError:
                print("Digite apenas números.")             
        elif escolha == 2:
            print("Fotos antigas mantidas.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite apenas números.")

# Loop principal do programa
while True:
    verificar_temporarias()
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
                nome = input("Digite o nome da foto que deseja excluir: ").lower()
                mensagem = f"\nFoto '{nome}' excluída com sucesso!"
                excluir_foto(nome, mensagem)
            case 5:
                foto_temporaria()
            case 6:
                calcular_tempo_vida()
            case 7:
                lixeira()
            case 0:
                print("Encerrando sistema...")
                break
            case _:
                print("Opção inválida.")

    except ValueError:
        print("Digite apenas números.")

    input("\nPressione ENTER para continuar.")