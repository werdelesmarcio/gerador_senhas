#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Sistema de Geração de Senhas
Data da última atualização: 23/02/2024
Dewsenvolvido por Werdeles 'gh05tb0y' Soares
"""

import random as rand
import PySimpleGUI as sg

class PassGen:
    #-------------------------------------------------- Layout da aplicação
    def __init__(self):        
        sg.theme('Reddit')
        layout = [[sg.Text('Site/Software:', size=(20,1)), sg.Input(key='site', size=(22,1))],
                  [sg.Text('E-mail/Usuário:', size=(20,1)), sg.Input(key='usuario', size=(22,1))],
                  [sg.Text('Quantidade de caracteres:', size=(20,1)), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(4,1))],
                  [sg.Output(size=(45,5))],[sg.Button('Gerar Senha')],
                  [sg.Text('Desenvolvido por: Werdeles Soares')]]
        
        #Criação da Janela da aplicação
        self.janela = sg.Window('Password Generator - Versão 1.0', layout)

    #-------------------------------------------------- Execução do Evento    
    def Iniciar(self):        
        while True:
            event, valores = self.janela.read()
            #Finalização da aplicação
            if event == sg.WINDOW_CLOSED:
                break

            #Evento do click do botão 'Gerar Senha'
            if event == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
    
    #-------------------------------------------------- Evento de criação de senha randômica
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&*'
        chars = rand.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    
    #-------------------------------------------------- Criação do arquivo de log com as senhas salvas
    def salvar_senha(self, nova_senha, valores):
        with open('log.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n")
        
        print('\nSenha gerada com sucesso.\nArquivo Salvo')

gen = PassGen()
gen.Iniciar()