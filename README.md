# Descrição
O projeto Comunicação Global tem como objetivo principal tornar a comunicação mais inclusiva e eficiente entre pessoas surdas e pessoas com acuidade auditiva. Para isso, desenvolvemos um sistema inovador que traduz a Língua Brasileira de Sinais (Libras) para o idioma português através do reconhecimento da língua de sinais em tempo real por uma Inteligência Artificial.
A linguagem de sinais é uma forma fundamental de comunicação para a comunidade surda, e nosso projeto visa quebrar as barreiras linguísticas ao permitir que pessoas com acuidade auditiva possam compreender os sinais e se comunicar de forma mais efetiva.


# Requisitos 
Python 3.11.3 - https://www.python.org/downloads/
Conda - https://conda.io/projects/conda/en/latest/user-guide/install/index.html
Webcam


# Visão geral de uso
O programa utiliza a webcam do usuário para identificar os sinais em Libras em tempo real e, em seguida, traduz as letras e/ou palavras para o idioma português. A interface é intuitiva e amigável, permitindo uma experiência fácil e acessível para todos os usuários.
Para começar, basta iniciar o programa e posicionar-se em frente à webcam. Em seguida, o sistema identificará os sinais realizados e exibirá a tradução correspondente na tela. Assim, pessoas com acuidade auditiva poderão entender a mensagem transmitida em Libras de forma imediata.

Para acessar o software é necessário fazer o download do repositório na máquina do usuário e executar o arquivo teste.html. Para utilizar o programa necessitá-se usar navegador web. Quando aberto, centralizar o sinal dentro dos limites do frame e acionar o botão para capturar a imagem, para então poder ser traduzida pela IA para a língua de sinais. 


# Tecnologias Utilizadas       
O projeto Comunicação Social utiliza as seguintes tecnologias:
Backend: Python - Utilizamos o poderoso ecossistema de desenvolvimento em Python para o desenvolvimento do backend. Através dele, implementamos os algoritmos de reconhecimento e tradução da Língua Brasileira de Sinais através do treinamento de uma IA.
Frontend: HTML, CSS, JavaScript - Para a criação do frontend, utilizamos as linguagens de marcação HTML, folhas de estilo CSS para a estilização visual e o JavaScript para a interatividade com o usuário. Essas tecnologias combinadas possibilitam uma experiência fluída e responsiva para os usuários.


Agradecemos o interesse no projeto Comunicação Universal. Estamos empenhados em promover uma comunicação inclusiva e eficiente, ajudando a quebrar barreiras e construir um mundo mais acessível para todos. Sinta-se à vontade para colaborar, fornecer feedback ou tirar dúvidas. Juntos, podemos fazer a diferença!

# Implementações
## Python

## HTML
FOi implementada uma função em JavaScript que lia a webcam e covertia a imagem para base64 e enviava para a API. Como resposta da API, é informada a letra correspondente ao sinal.
