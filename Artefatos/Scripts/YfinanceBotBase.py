
#/////////////////Arquivo Main.py/////////////////////

from controller import Controller

if __name__ == "__main__":
    controller = Controller()
    controller.start()

#/////////////////Arquivo Model.py/////////////////////

import yfinance as yf

class Model:
    def __init__(self):
        self.ativos = ["AAPL", "GOOGL", "MSFT", "BTC-USD"]
        self.periodos = ["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]
        
    def buscar_dados(self, ativo, periodo):
        ativo_ticker = yf.Ticker(ativo)
        ativo_data = ativo_ticker.history(period=periodo)
        return ativo_data['Close'], ativo_data.index


#/////////////////Arquivo View.py/////////////////////

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class View:
    def __init__(self, controller):
        self.controller = controller
        
        self.root = tk.Tk()
        self.root.title("MT5")
        
        # Frame superior para selecionar o ativo e o período
        self.superior_frame = tk.Frame(self.root)
        self.superior_frame.pack(side=tk.TOP)
        
        # Lista dropbox para selecionar o ativo
        self.ativo_selecionado = tk.StringVar(self.superior_frame)
        self.ativo_selecionado.set(self.controller.ativos[0])
        self.dropbox_ativos = ttk.Combobox(self.superior_frame, textvariable=self.ativo_selecionado, values=self.controller.ativos)
        self.dropbox_ativos.pack(side=tk.LEFT)
        
        # Lista dropbox para selecionar o período
        self.periodo_selecionado = tk.StringVar(self.superior_frame)
        self.periodo_selecionado.set(self.controller.periodos[0])
        self.dropbox_periodos = ttk.Combobox(self.superior_frame, textvariable=self.periodo_selecionado, values=self.controller.periodos)
        self.dropbox_periodos.pack(side=tk.LEFT)
        
        # Botão "Buscar Dados"
        self.botao_busca = tk.Button(self.superior_frame, text="Buscar Dados", command=self.buscar_dados)
        self.botao_busca.pack(side=tk.LEFT)
        
        # Crie o canvas para exibir o gráfico
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        
        # Exiba a janela para o usuário
        self.root.mainloop()

    def buscar_dados(self):
        ativo = self.ativo_selecionado.get()
        periodo = self.periodo_selecionado.get()
        close, index = self.controller.model.buscar_dados(ativo, periodo)
        self.plotar_grafico(close, index)

    def plotar_grafico(self, close, index):
        self.ax.clear()
        self.ax.plot(index, close)
        self.ax.set_title(f"Gráfico do Preço do {self.ativo_selecionado.get()} ({self.periodo_selecionado.get()})")
        self.ax.set_xlabel("Data")
        self.ax.set_ylabel("Preço")
        self.fig.autofmt_xdate()
        self.canvas.draw()

#/////////////////Arquivo Controller.py/////////////////////

from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    @property
    def ativos(self):
        return self.model.ativos

    @property
    def periodos(self):
        return self.model.periodos