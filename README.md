# Sistema distribuidos e computação paralela  - API REST/RESTful
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
*	As bibliotecas flask, flask-restful e pandas. Para isso, abra o terminal e digite 
*	```sh pip install flask flask-restful pandas openpyxl xlwt``` 
para instalar as bibliotecas respectivamente.

Abra o código com o VSCode e vá para o arquivo app.py e o execute. Um terminal deve abrir, informando que está tudo ok e mostrando o ip da sua máquina assim como a porta que a API está rodando.

## Etapa 2 - Mandando um "request"

### Requisitos
*	Postman

A primeira coisa que precisa ser feita para conseguir uma resposta da API é uma maneira de mandar um “request” para ela, seja com outra API ou com algum programa externo. Para essa demonstração utilizaremos um programa chamado de “Postman”.

Abra o postman e você deve ver uma tela parecida com essa

![postman](https://github.com/MMaues/api_excel/blob/main/img/postman1.png?raw=true)

Altere GET para POST e insira a seguinte URL ```http://{{ip da sua máquina:porta}}/v1/api/modificadorexcel``` para ficar da seguinte forma

![postman2](https://github.com/MMaues/api_excel/blob/main/img/postman2.png?raw=true)

Escolha a opção "Body" -> "form-data" e altere o tipo do campo para "file". Nomeie como excel_notas e insira o arquivo das notas de excel presentes neste GitHub.

Se estiver tudo certo, seu postman deve parecer com isso

![postman3](https://github.com/MMaues/api_excel/blob/main/img/postman3.png?raw=true)

Agora basta apertar em "send" e esperar a resposta da API

Quando a API responder, você deve ver algo parecido com isso. A API retorna os bytes do arquivo, por isso a resposta pode parecer um pouco estranha.

![postman4](https://github.com/MMaues/api_excel/blob/main/img/postman4.png?raw=true)

Agora é só apertar em "save response", "save to file" e escolher o local onde salvar. 


