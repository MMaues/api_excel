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
*	As bibliotecas flask, flask-restful e pandas. Para isso, abra o terminal e digite ```pip install flask flask-restful pandas```, para instalar as bibliotecas respectivamente.

Abra o código com o VSCode e vá para o arquivo app.py e o execute. Um terminal deve abrir, informando que está tudo ok e mostrando o ip da sua máquina assim como a porta que a API está rodando.

## Mandando um "request"

### Requisitos
*	Postman

A primeira coisa que precisa ser feita para conseguir uma resposta da API é uma maneira de mandar um “request” para ela, seja com outra API ou com algum programa externo. Para essa demonstração utilizaremos um programa chamado de “Postman”.

Abra o postman e você deve ver uma tela parecida com essa

![image](https://user-images.githubusercontent.com/49196652/201551964-3cdeaa58-f0b5-46b3-a856-e3ef59384411.png)

Altere GET para POST e insira a seguinte URL ```http://{{ip da sua máquina:porta}}/api/modificadorexcel``` para ficar da seguinte forma

![image](https://user-images.githubusercontent.com/49196652/201552277-e48c1cba-b61b-4645-a1e4-574dc61b6fbd.png)

Escolha a opção "Body" -> "form-data" e altere o tipo do campo para "file". Nomeie como excel_notas e insira o arquivo das notas de excel presentes neste GitHub.

Se estiver tudo certo, seu postman deve parecer com isso

![image](https://user-images.githubusercontent.com/49196652/201552644-605c3538-c449-4542-a200-7a03e8156c5b.png)

Agora basta apertar em "send" e esperar a resposta da API

Quando a API responder, você deve ver algo parecido com isso

![image](https://user-images.githubusercontent.com/49196652/201553087-953bf074-0136-4679-8bf2-8cfbc9b12f81.png)

Basta apertar em "save response", "save to file" e escolher o local onde salvar. 

Agora basta abrir o arquivo para perceber que ele está organizado por professor e aluno.


