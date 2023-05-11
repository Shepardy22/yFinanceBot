import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

# lista de ativos disponíveis
ativos = ["AAPL", "GOOGL", "MSFT", "BTC-USD"]
periodos = ["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]

# janela gráfica
janela = Tk()
janela.title("MT5")

# frame superior para selecionar o ativo e o período
frame_superior = Frame(janela)
frame_superior.pack(side=TOP)

# lista dropbox para selecionar o ativo
ativo_selecionado = StringVar(frame_superior)
ativo_selecionado.set(ativos[0])
dropbox_ativos = OptionMenu(frame_superior, ativo_selecionado, *ativos)
dropbox_ativos.pack(side=LEFT)

# lista dropbox para selecionar o período
periodo_selecionado = StringVar(frame_superior)
periodo_selecionado.set(periodos[0])
dropbox_periodos = OptionMenu(frame_superior, periodo_selecionado, *periodos)
dropbox_periodos.pack(side=LEFT)

# botão "Buscar Dados"
def buscar_dados():
    ativo_ticker = yf.Ticker(ativo_selecionado.get())
    ativo_data = ativo_ticker.history(period=periodo_selecionado.get())
    plt.clf()
    plt.plot(ativo_data.index, ativo_data['Close'])
    plt.title(f"Gráfico do Preço do {ativo_selecionado.get()} ({periodo_selecionado.get()})")
    plt.xlabel("Data")
    plt.ylabel("Preço (USD)")
    canvas.draw()

botao_busca = Button(frame_superior, text="Buscar Dados", command=buscar_dados)
botao_busca.pack(side=LEFT)

# Crie o canvas para exibir o gráfico
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)

# Exiba a janela para o usuário
janela.mainloop()
