# IotTro-Varal_iot_4422
Projeto desenvolvido para a disciplina de Micros II do Curso Técnico de Eletronica da Fundação Liberato

  Esse projeto consiste na aplicação do protocolo de comunicação MQTT. Nosso trabalho consiste em um varal
de roupas que utiliza informações de clima para saber se deve ou não expor as roupas na rua.
  O trabalho utiliza dois microcontroladores. Um deles é utilizado para a aferição do nivel de chuva na 
região onde esta o Varal.O segundo micro é utilizado para receber as informações e controlar um motor 
de passo responsavel pelo movimento do varal. 
  Nossos microcontroladores não tem acesso nativo a internet para podermos utilizar o protocolo MQTT. Para 
conseguirmos utilizar tal tecnologia foi necessario fazer uma comunicação serial com um computador, utilizando
um aplicação escrita em python e, a partir dessa aplicação, enviar os dados entre os microcontroladores usando o MQTT.
Para obtermos informaçoes mais gerais do clima na cidade, utilizamos uma aplicaçao desenvolvida em NODERED usando o node
OPENWEATHERMAP que nos dá diversas informações do clima.
  
