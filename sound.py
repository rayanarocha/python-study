
#O Google criou uma API chamada Google Text-To-Speech, que eles usam para ler um texto e fornecer saída de áudio.
# Esta API é integrada a um módulo Python denominado gtts, que pode converter texto em fala, realizar manipulação 
# de áudio, entre outras coisas, armazenando áudio em um objeto de tamanho de bytes e até mesmo salvar a saída 
# final.

#Usaremos a função gTTS para criar um objeto que irá ler o texto e convertê-lo em um objeto de áudio. 
# Podemos usar muitos parâmetros com esta função. Podemos reduzir a velocidade da saída usando o argumento slow.
# A API do Google suporta diferentes idiomas, e podemos mencionar os idiomas suportados usando o parâmetro lang.

"""
from gtts import gTTS
from playsound import playsound

s = gTTS("Olá, Rayana")
s.save('sound.mp3')
playsound('sound.mp3')
"""

#O pyttsx3 é outro módulo que pode realizar tais conversões e funcionar sem conexão com a 
# internet. Primeiro, criaremos um objeto que faz referência ao pyttsx3.Engine usando o 
# construtor init() deste módulo. Em seguida, a função say() adiciona aqui o texto necessário 
# para ser falado na fila. Em seguida, usamos a função runAndWait() para reproduzir o comando 
# da fila.

import pyttsx3  
s = pyttsx3.init() 
nome = str(input("Digite seu nome: ")) 
data = "Olá,", nome
s.say(data)  
s.runAndWait()