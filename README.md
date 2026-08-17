# Gerenciador de Estudos

Um projeto desenvolvido em **Python** para ajudar a organizar os estudos e acompanhar o progresso em diferentes matérias.

A ideia surgiu como uma forma de praticar Python e, ao mesmo tempo, criar algo que eu pudesse usar no dia a dia.

## Funcionalidades

- Adicionar e remover matérias
- Definir uma meta semanal de horas para cada matéria
- Adicionar e remover conteúdos
- Alterar o status dos conteúdos
  - Em andamento
  - Concluído
- Adicionar anotações aos conteúdos
- Registrar horas de estudo
- Visualizar o progresso das matérias
- Visualizar o progresso por horas estudadas
- Visualizar o progresso por conteúdos concluídos
- Calcular o progresso total
- Salvar os dados automaticamente em um arquivo JSON
- Carregar os dados salvos ao iniciar o programa
- Validação das entradas do usuário

## Tecnologias utilizadas

- **Python**
- **JSON** para salvar os dados
- **Git/GitHub** para versionamento do projeto

## O que pratiquei

Durante o desenvolvimento, pratiquei vários conceitos de Python que venho estudando, como:

- Programação Orientada a Objetos (POO)
- Classes e objetos
- Funções e métodos
- Listas e dicionários
- Estruturas condicionais e de repetição
- Tratamento de exceções
- Manipulação de arquivos
- Uso de JSON
- Modularização
- Validação de entradas
- Refatoração de código

### Classes

**`Conteudo`**

Responsável pelos conteúdos cadastrados dentro de cada matéria.

Cada conteúdo possui:

- Nome
- Status
- Anotações

**`Materia`**

Responsável pelas informações de cada matéria, como:

- Nome
- Meta semanal de horas
- Horas estudadas
- Conteúdos
- Progresso

**`GerenciadorEstudos`**

Responsável por adicionar, remover, listar e buscar as matérias do sistema.

## Persistência dos dados

Os dados são armazenados no arquivo `materias.json`.

Quando o programa é iniciado, os dados salvos são carregados automaticamente. Sempre que alguma alteração é feita, os dados são atualizados no arquivo.

Assim, as informações continuam disponíveis mesmo depois que o programa é fechado.

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd gerenciador-estudos
```

### 3. Execute o programa

```bash
python main.py
```

É necessário ter o **Python** instalado para executar o projeto.

## Desenvolvimento

Comecei o projeto de uma forma mais simples e, conforme fui desenvolvendo novas funcionalidades, o código foi crescendo.

Depois fiz uma etapa de **refatoração**, separando melhor as responsabilidades entre classes e funções e removendo alguns trechos de código repetidos.

Também fiz testes depois das alterações para verificar se as funcionalidades continuavam funcionando corretamente.

## Objetivo

Criei este projeto principalmente para **praticar Python e aplicar na prática os conceitos que venho estudando**.

Além de desenvolver as funcionalidades, também usei o projeto para aprender mais sobre organização de código, persistência de dados e refatoração.

## Status

**Concluído — v1.0**