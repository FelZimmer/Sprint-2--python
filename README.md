# 📸 Galeria de Fotos em Python

Sistema de gerenciamento de galeria de fotos desenvolvido em Python utilizando JSON para armazenamento de dados.
O projeto permite adicionar, visualizar, pesquisar, recuperar e excluir fotos, além de oferecer suporte para fotos temporárias com remoção automática e sistema de lixeira.

---

## 🚀 Funcionalidades

* 📂 Visualizar galeria de fotos
* 🔎 Procurar fotos por nome, descrição ou categoria
* ➕ Adicionar novas fotos
* ❌ Excluir fotos
* 🗑️ Sistema de lixeira
* ♻️ Recuperar fotos excluídas
* 🧹 Esvaziar lixeira
* ⏳ Criar fotos temporárias
* 🧠 Detecção automática de categoria
* 📅 Identificação de fotos antigas
* 🗃️ Armazenamento em arquivo JSON
* 🖥️ Limpeza automática do terminal

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* Threading
* Datetime
* OS

---

## 📁 Estrutura do Projeto

```bash
📦 galeria-python
 ┣ 📜 main.py
 ┣ 📜 galeria.json
 ┗ 📜 README.md
```

---

## 📄 Estrutura do JSON

O arquivo `galeria.json` deve possuir a seguinte estrutura:

```json
{
    "fotos": [],
    "lixeira": []
}
```

### Exemplo:

```json
{
    "fotos": [
        {
            "foto": "praia",
            "descricao": "Foto da praia ao pôr do sol",
            "data": "13-05-2026 21:30",
            "is_temporaria": false,
            "tempo_vida": null,
            "categoria": "natureza"
        }
    ],
    "lixeira": []
}
```

---

## ▶️ Como Executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/FelZimmer/Sprint-2--python.git
```

### 2️⃣ Acesse a pasta do projeto

```bash
cd Sprint-2--python
```

### 3️⃣ Execute o sistema

```bash
python main.py
```

---

## 📋 Menu do Sistema

```text
1 - Ver galeria
2 - Procurar foto
3 - Adicionar foto
4 - Excluir foto
5 - Foto temporária
6 - Ver fotos antigas
7 - Ver lixeira
0 - Sair
```

---

## 🔎 Sistema de Pesquisa

O sistema permite pesquisar fotos de duas formas:

### 📌 Por nome ou descrição

Busca fotos utilizando palavras presentes no nome ou descrição.

### 📂 Por categoria

Categorias disponíveis:

* 🐶 Animal
* 🌳 Natureza
* 📚 Estudos
* 🍔 Comida
* 💻 Tecnologia
* 📦 Outros

---

## 🧠 Categorias Automáticas

O sistema detecta automaticamente a categoria da foto com base no nome e descrição informados pelo usuário.

Exemplo:

```python
Nome: notebook gamer
Descrição: computador para estudos

Categoria detectada: tecnologia
```

---

## ⏳ Fotos Temporárias

As fotos temporárias são removidas automaticamente após um determinado tempo utilizando `threading.Timer()`.

### Opções disponíveis:

| Opção | Tempo       |
| ----- | ----------- |
| 1     | 1 dia       |
| 2     | 1 semana    |
| 3     | 1 mês       |
| 4     | 1 ano       |
| 5     | 15 segundos |

Quando removidas, as fotos vão automaticamente para a lixeira.

---

## 🗑️ Sistema de Lixeira

As fotos excluídas não são apagadas permanentemente imediatamente.

### Funcionalidades:

* ♻️ Recuperar fotos excluídas
* 🧹 Esvaziar lixeira
* 📂 Visualizar itens removidos

---

## 📅 Sistema de Fotos Antigas

O sistema identifica fotos armazenadas há muito tempo.

### Classificações:

* 📆 Mais de 3 meses
* 📆 Mais de 6 meses
* 📆 Mais de 1 ano

Também é possível excluir automaticamente fotos antigas por categoria.

---

## 🖥️ Limpeza do Terminal

O sistema utiliza a biblioteca `os` para limpar automaticamente o terminal durante a navegação:

```python
os.system("cls" if os.name == "nt" else "clear")
```

Compatível com:

* Windows (`cls`)
* Linux/macOS (`clear`)

---

## ⚠️ Tratamento de Erros

O projeto possui tratamento de erros para:

* Entrada inválida do usuário
* Conversão de datas
* Leitura e escrita do JSON
* Valores não numéricos no menu
* Galeria vazia
* Fotos não encontradas

---

# Projeto em desenvolvimento ⚙️
