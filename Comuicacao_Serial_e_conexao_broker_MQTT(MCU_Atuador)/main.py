# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:36:43 2020
@project: Meu Treco na Internet
@title: Comunicação com Protocolo MQTT no STM32F446RE utilizando Python
@author: Luís Henrique

"""
import serial                   # importar biblioteca para comunicacao serial
import paho.mqtt.client as mqtt # importar cliente MQTT
import sys

#----------------------------------------------------------------------------#
#DEFINICOES:
#-> MQTT:
Broker = "mqtt.eclipse.org"                      # Host MQTT
PortaBroker = 1883                            
KeepAliveBroker = 60
TopicoSubcribe = "iotTro/VaralIot/SensorChuva" #topico assinado

#-> COMUNICACAO SERIAL 
Porta_Serial ="COM3"      # nome da porta serial que sera usada na comunicação
baud_rate =115200         # baud rate da comuicação serial
usart =0                  # "abreviacao" da struct serial.Serial
#----------------------------------------------------------------------------#
#-------------------------FUNCOES AUXILIARES---------------------------------#
    
#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
        print("[STATUS] Conectado ao Broker. Conexao:"+ str(rc))
        # faz subscribe no topico
        client.subscribe(TopicoSubcribe)
        

#Callback - Mensagem recebida do broker
def on_message(client, userdata, msg):
    Mensagem_Recebida = str(msg.payload)
    #imprime mensagem recebida
    print("[MSG RECEBIDA] Topico:"+msg.topic+" -> Mensagem:"+Mensagem_Recebida)
   

    # converte o valor string de 'mensagem recebida' para o formato byte   
    msg_convertida = bytes(Mensagem_Recebida,'utf-8')
    # escreve o valor convetido na porta serial
    usart.write(msg_convertida)
    print("msg convertida: "+msg_convertida)
   
#----------------------------------------------------------------------------#
#-----------------------PROGRAMA PRINCIPAL-----------------------------------#


try:
    # inicia a comunicação serial
    usart = serial.Serial(Porta_Serial,baud_rate) 
    # imprime o status da porta serial
    print("[!] Status Port: %s" %usart.isOpen())
    # imprime o nome da serial conectada   
    print("[!] Port Name: %s" %usart.name)# 
    
    
    print("[STATUS] iniciando MQTT...")
    #inicia MQTT:
    client = mqtt.Client()      
    client.on_connect = on_connect  #callback da funcao
    client.on_message = on_message  #callback da funcao
 
    client.connect(Broker,PortaBroker,KeepAliveBroker) #config e connect broker
    client.loop_forever() # mantem conexao com o broker


except KeyboardInterrupt:
        print ("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
        usart.close()
        sys.exit(0)   # encerra a aplicacao
#----------------------------------------------------------------------------#