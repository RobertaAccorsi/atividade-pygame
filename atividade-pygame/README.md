# Atividade Pygame – Colisão de Objetos

Atividade desenvolvida utilizando a biblioteca Pygame, com o objetivo de simular o movimento de dois objetos na tela (estilo DVD) e detectar colisões entre eles.

---

## Enunciado da atividade

- Desenvolver dois objetos (rect) que se colidam  
- Utilizar código refatorado de movimento de objetos (simulação DVD)  
- Subir o projeto no GitHub  
- Estruturar e documentar o projeto no README.md  

---

## Objetivo

Implementar dois objetos que se movimentam continuamente na tela, tratando a colisão com as bordas da janela por meio de uma função refatorada e detectando a colisão entre os próprios objetos.

---

## Descrição da solução

O programa exibe dois textos na tela:

- Roberta  
- Accorsi  

Cada texto é representado por um objeto do tipo `Rect`.

Os objetos se movimentam automaticamente pela tela simulando o comportamento do logotipo de DVD.

O sistema possui:

- Tratamento de colisão com as bordas da janela por meio de função refatorada
- Detecção de colisão entre os dois objetos
- Inversão da direção do movimento quando ocorre colisão
- Alteração da cor dos textos ao colidir

---

## Estrutura do projeto