# Sistema distribuidos e computação gráfica - API REST/RESTful
## Alunos:
* João Francisco Ramacciotti Sieiro
* José Augusto Barros Minhoto
* Marcelo Maués Botelho de Souza
* Vinicius Prado Vasconcelos

## Descrição do projeto
Esta POC tem como finalidade, separar um arquivo Excel que contenha notas, nomes de alunos e professores. A princípio teremos as células em ordens aleatórias, assim, utilizaremos nosso API para ordenar e separar em arquivos diferentes baseado no nome do professor. 


# Passo a passo

## Etapa 1 - Configuração de projeto

### Requisitos
*	Visual Studio Code
*	Python 3 ou superior
*	As bibliotecas flask, flask-restful e pandas. Para isso, abra o terminal e digite ```pip install flask```, ```pip install flask-restful``` e ```pip install pandas```, para instalar as bibliotecas.

Abra o código com o VSCode e vá para o arquivo app.py e o execute. Um terminal deve abrir, informando que está tudo ok e mostrando o ip da sua máquina.

## Mandando um "request"

A primeira coisa que precisa ser feita para conseguir uma resposta da API é uma maneira de mandar um “request” para ela, seja com outra API ou com algum programa externo. Para essa demonstração utilizaremos um programa chamado de “Postman”.
