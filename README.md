# 📸 Galeria de Fotos em Python

Sistema robusto de gerenciamento de galeria de fotos desenvolvido em Python, utilizando **JSON** para persistência de dados. O projeto oferece funcionalidades avançadas como detecção automática de categorias, sistema de lixeira e suporte a fotos temporárias com persistência.

---

## 🚀 Funcionalidades

*   📂 **Visualizar Galeria**: Listagem completa das fotos com detalhes de descrição, categoria e data.
*   🔎 **Busca Inteligente**: Pesquisa por nome, descrição ou filtro por categorias específicas.
*   ➕ **Adicionar Fotos**: Cadastro de novas fotos com detecção automática de categoria.
*   ❌ **Exclusão Segura**: As fotos deletadas são movidas para a lixeira antes de serem removidas permanentemente.
*   🗑️ **Sistema de Lixeira**: Visualize, recupere ou esvazie todos os itens removidos.
*   ⏳ **Fotos Temporárias**: Defina um tempo de vida para a foto. Ela será movida para a lixeira automaticamente.
*   🧠 **Inteligência de Categoria**: O sistema analisa o nome e a descrição para sugerir a categoria correta (Animais, Natureza, Estudos, Comida, Tecnologia ou Outros).
*   📅 **Gestão de Fotos Antigas**: Identifica fotos armazenadas há mais de 3 meses, 6 meses ou 1 ano, permitindo a exclusão em lote por categoria.
*   🔄 **Persistência de Expiração**: Mesmo que o programa seja fechado, fotos temporárias vencidas serão detectadas e movidas para a lixeira na próxima inicialização.

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3**: Linguagem base do sistema.
*   **JSON**: Armazenamento e persistência dos dados.
*   **Threading**: Utilizado para temporizadores em tempo real.
*   **Datetime**: Manipulação e cálculo de datas de criação e expiração.
*   **OS**: Integração com o sistema operacional para limpeza de terminal.

---

## 📁 Estrutura do Projeto

```bash
📦 Sprint-2--python
 ┣ 📜 menu.py          # Arquivo principal do sistema
 ┣ 📜 galeria.json     # Banco de dados em formato JSON
 ┗ 📜 README.md        # Documentação do projeto
```

---

## 📄 Estrutura do JSON

O arquivo `galeria.json` organiza as fotos em dois grupos principais: `fotos` (galeria ativa) e `lixeira`.

### Exemplo de Registro:
```json
{
    "foto": "notebook_estudos.jpg",
    "descricao": "Meu computador para a faculdade",
    "data": "15-05-2026 14:00",
    "is_temporaria": true,
    "tempo_vida": 86400,
    "expira_em": "16-05-2026 14:00",
    "categoria": "tecnologia"
}
```

---

## ▶️ Como Executar

1. **Acesse a pasta do projeto**:
   ```bash
   cd Sprint-2--python
   ```

2. **Execute o sistema**:
   ```bash
   python menu.py
   ```

---

## 📋 Menu Principal

```text
1 - Ver galeria
2 - Procurar foto
3 - Adicionar foto
4 - Excluir foto
5 - Foto temporária
6 - Ver fotos antigas
7 - Ver Lixeira
0 - Sair
```

---

## 🧠 Categorias e Palavras-Chave

O sistema utiliza listas pré-definidas para classificar suas fotos automaticamente. Algumas palavras monitoradas:
*   **Animais**: cachorro, gato, leão, urso, peixe...
*   **Natureza**: floresta, rio, mar, árvore, sol...
*   **Estudos**: livro, caderno, escola, faculdade, curso...
*   **Comida**: pizza, hambúrguer, café, chocolate...
*   **Tecnologia**: computador, código, celular, python...

---

## ⏳ Gestão de Tempo

### Fotos Temporárias
Ao adicionar uma foto temporária, você pode escolher entre:
*   15 segundos (para testes)
*   1 dia
*   1 semana
*   1 mês
*   1 ano

### Fotos Antigas
O sistema permite a **Exclusão em Lote**. Você pode optar por mover para a lixeira todas as fotos de uma categoria específica que tenham mais de **1 ano** de armazenamento.

---

## ⚠️ Robustez e Segurança

*   **Validação de Entrada**: Tratamento para evitar que letras sejam digitadas em campos numéricos.
*   **Prevenção de Duplicatas**: Não permite adicionar fotos com o mesmo nome.
*   **Integridade de Dados**: Se o arquivo JSON for deletado ou corrompido, o sistema cria uma nova base de dados automaticamente.
*   **Loop Seguro**: Operações em listas são feitas em cópias para evitar erros de iteração durante exclusões.

---

Desenvolvido para a **Sprint 2** - Computational Thinking with Python. 🚀
