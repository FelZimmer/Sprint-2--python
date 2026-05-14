# 📸 Galeria de Fotos em Python

Sistema de gerenciamento de galeria de fotos desenvolvido em Python utilizando JSON para armazenamento de dados.
O projeto permite adicionar, visualizar, pesquisar e excluir fotos, além de oferecer suporte para fotos temporárias com remoção automática.

---

## 🚀 Funcionalidades

* 📂 Visualizar galeria de fotos
* 🔎 Procurar fotos por nome ou descrição
* ➕ Adicionar novas fotos
* ❌ Excluir fotos
* ⏳ Criar fotos temporárias
* 🧠 Detecção automática de categoria
* 📅 Cálculo do tempo de vida das fotos
* 🗃️ Armazenamento em arquivo JSON

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* Threading
* Datetime

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
    "fotos": []
}
```

Exemplo:

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
    ]
}
```

---

## ▶️ Como Executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/FelZimmer/Sprint-2--python.git
```

### 2️⃣ Acesse a pasta

```bash
cd Sprint-2--python
```

### 3️⃣ Execute o projeto

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
6 - Calcular tempo de vida
```

---

## 🧠 Categorias Automáticas

O sistema detecta automaticamente categorias com base no nome e descrição da foto.

### Categorias disponíveis:

* 🐶 Animal
* 🌳 Natureza
* 📚 Estudos
* 🍔 Comida
* 💻 Tecnologia
* 📦 Outros

---

## ⏳ Fotos Temporárias

As fotos temporárias são removidas automaticamente após um determinado tempo.

### Opções disponíveis:

| Opção | Tempo       |
| ----- | ----------- |
| 1     | 1 dia       |
| 2     | 1 semana    |
| 3     | 1 mês       |
| 4     | 1 ano       |
| 5     | 15 segundos |

---

## 📅 Cálculo de Tempo de Vida

O sistema calcula há quantos dias a foto foi adicionada e organiza em listas:

* Fotos com mais de 3 meses
* Fotos com mais de 6 meses
* Fotos com mais de 1 ano

---

## Projeto em desenvolvimento ⚙️
