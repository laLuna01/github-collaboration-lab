# Guia de Contribuição

Obrigado pelo interesse em contribuir com o **GitHub Collaboration Lab**!

Este repositório foi criado como um ambiente de estudos para praticar colaboração e gerenciamento de projetos utilizando recursos do GitHub.

Contribuições podem incluir novos exercícios, melhorias em soluções existentes, correções, documentação ou implementações em outras linguagens.

## Como contribuir

O fluxo de contribuição utilizado neste projeto é:

1. verificar as Issues existentes;
2. escolher uma tarefa ou propor uma nova melhoria;
3. criar uma branch para realizar a alteração;
4. implementar a mudança;
5. realizar commits claros e objetivos;
6. abrir um Pull Request;
7. aguardar a revisão;
8. realizar ajustes, caso sejam solicitados;
9. realizar o merge após a aprovação.

## Issues

Antes de iniciar uma alteração, verifique se já existe uma Issue relacionada.

As Issues podem ser utilizadas para:

- propor novos exercícios;
- relatar problemas;
- sugerir melhorias;
- solicitar implementações em outras linguagens;
- propor melhorias na documentação.

Caso ainda não exista uma Issue relacionada à contribuição, crie uma antes de iniciar o desenvolvimento.

## Branches

As alterações devem ser desenvolvidas em uma branch separada da `main`.

Utilize nomes descritivos para facilitar a identificação da alteração.

Exemplos:

```text
feature/python-fizzbuzz
feature/javascript-palindrome
fix/fibonacci-validation
docs/improve-python-readme
```

Alguns prefixos sugeridos:

| Prefixo | Utilização |
| --- | --- |
| `feature/` | Novo exercício ou funcionalidade |
| `fix/` | Correção de problema |
| `docs/` | Alteração de documentação |
| `refactor/` | Melhoria interna sem alterar o comportamento |

## Commits

Procure utilizar mensagens de commit curtas e descritivas.

Exemplos:

```text
feat: add FizzBuzz exercise
fix: handle empty palindrome input
docs: improve contribution guide
refactor: simplify Fibonacci implementation
```

Cada commit deve representar uma alteração lógica sempre que possível.

## Pull Requests

Ao finalizar uma alteração, abra um Pull Request para a branch `main`.

O Pull Request deve explicar:

- o que foi alterado;
- por que a alteração foi realizada;
- qual Issue está relacionada;
- como a alteração pode ser testada, quando aplicável.

Quando o Pull Request resolver uma Issue, ela poderá ser referenciada na descrição utilizando:

```text
Closes #numero-da-issue
```

Exemplo:

```text
Closes #1
```

Dessa forma, a Issue relacionada poderá ser encerrada quando o Pull Request for integrado.

## Exercícios

Os exercícios estão organizados dentro do diretório `exercises/`, separados por linguagem:

```text
exercises/
├── python/
├── javascript/
└── java/
```

Python será utilizado para as primeiras implementações.

Implementações equivalentes em JavaScript e Java poderão ser adicionadas posteriormente através de contribuições.

## Boas práticas

Ao contribuir:

- mantenha o código simples e legível;
- utilize nomes claros para variáveis e funções;
- evite alterações que não estejam relacionadas à Issue escolhida;
- documente comportamentos que possam não ser óbvios;
- mantenha o escopo do Pull Request pequeno sempre que possível;
- respeite a estrutura existente do projeto.

## Sugestões de contribuição

Algumas formas de contribuir com este projeto são:

- adicionar um novo exercício de lógica;
- implementar um exercício existente em outra linguagem;
- melhorar uma solução;
- tratar casos especiais de entrada;
- melhorar a documentação;
- corrigir erros encontrados nos exercícios;
- propor novas ideias através das Issues.

---

Este guia poderá evoluir conforme novas formas de colaboração forem utilizadas no projeto.
