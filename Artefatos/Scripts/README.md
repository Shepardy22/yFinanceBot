

Codigo Base:

import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import *

# Defina uma lista de ativos disponíveis
ativos = ["AAPL", "GOOGL", "MSFT", "BTC-USD"]
periodos = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]

# Crie a janela gráfica
janela = Tk()
janela.title("MT5")

# Crie o frame superior para selecionar o ativo e o período
frame_superior = Frame(janela)
frame_superior.pack(side=TOP)

# Crie a lista dropbox para selecionar o ativo
ativo_selecionado = StringVar(frame_superior)
ativo_selecionado.set(ativos[0])
dropbox_ativos = OptionMenu(frame_superior, ativo_selecionado, *ativos)
dropbox_ativos.pack(side=LEFT)

# Crie a lista dropbox para selecionar o período
periodo_selecionado = StringVar(frame_superior)
periodo_selecionado.set(periodos[0])
dropbox_periodos = OptionMenu(frame_superior, periodo_selecionado, *periodos)
dropbox_periodos.pack(side=LEFT)

# Crie o botão "Buscar Dados"
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



_____________________________________________________________________________________________________
refatore somente os arquivos necessarios para solucionar o erro:

Exception in Tkinter callback
Traceback (most recent call last):
  File "pandas\_libs\tslibs\parsing.pyx", line 440, in pandas._libs.tslibs.parsing.parse_datetime_string_with_reso
  File "pandas\_libs\tslibs\parsing.pyx", line 649, in pandas._libs.tslibs.parsing.dateutil_parse
ValueError: Unknown datetime string format, unable to parse: close

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python311\Lib\site-packages\pandas\core\indexes\datetimes.py", line 704, in get_loc
    parsed, reso = self._parse_with_reso(key)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\site-packages\pandas\core\indexes\datetimelike.py", line 230, in _parse_with_reso
    parsed, reso_str = parsing.parse_time_string(label, freq)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pandas\_libs\tslibs\parsing.pyx", line 367, in pandas._libs.tslibs.parsing.parse_time_string
  File "pandas\_libs\tslibs\parsing.pyx", line 445, in pandas._libs.tslibs.parsing.parse_datetime_string_with_reso
pandas._libs.tslibs.parsing.DateParseError: Unknown datetime string format, unable to parse: close

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Python311\Lib\tkinter\__init__.py", line 1948, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "c:\Users\Yuri\Documents\workspace\yFinanceBot\Artefatos\Scripts\view.py", line 35, in <lambda>
    self.botao_busca = Button(self.frame_superior, text="Buscar Dados", command=lambda: self.controller.buscar_dados_controller(self.ativo_selecionado.get(), self.periodo_selecionado.get()))
                                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\Yuri\Documents\workspace\yFinanceBot\Artefatos\Scripts\controller.py", line 11, in buscar_dados_controller
    self.view.exibir_grafico(dados["Close"], ativo, periodo)
  File "c:\Users\Yuri\Documents\workspace\yFinanceBot\Artefatos\Scripts\view.py", line 45, in exibir_grafico
    self.ax.plot(pd.to_datetime(grafico_data.index), grafico_data['close'])
                                                     ~~~~~~~~~~~~^^^^^^^^^
  File "C:\Python311\Lib\site-packages\pandas\core\series.py", line 981, in __getitem__
    return self._get_value(key)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\site-packages\pandas\core\series.py", line 1089, in _get_value
    loc = self.index.get_loc(label)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\site-packages\pandas\core\indexes\datetimes.py", line 706, in get_loc
    raise KeyError(key) from err
KeyError: 'close'

#Arquivo Controller.py:

Criar uma classe Controller que será responsável por intermediar as ações do usuário na interface gráfica e as funções da classe Model e View;
Na classe Controller, instanciar as classes Model e View;
Criar um método buscar_dados_controller que chama a função buscar_dados_model da classe Model e passa os parâmetros necessários;
Criar um método exibir_grafico_controller que chama o método exibir_grafico da classe View e passa os dados do gráfico.

    -CODIGO DO ARQUIVO controller.py:

```python

from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
    def buscar_dados_controller(self, ativo, periodo):
        dados = self.model.buscar_dados_model(ativo, periodo)
        self.view.exibir_grafico(dados["Close"], ativo, periodo)

```





______________________________________________________________________________


#Arquivo View.py:

Criar uma classe View que será responsável por exibir a interface gráfica para o usuário;
Mover o código referente à criação da interface gráfica (janela, frames, botões, etc.) para dentro da classe View;
Criar um método exibir_grafico que recebe os dados do gráfico e plota o gráfico em uma área designada na interface gráfica.

    -CODIGO DO ARQUIVO view.py:

```python

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import pandas as pd

class View:
    def __init__(self, controller):
        self.controller = controller
        
        # Defina uma lista de ativos disponíveis
        self.ativos = ["AAPL", "GOOGL", "MSFT", "BTC-USD"]
        self.periodos = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]
        
        # Crie a janela gráfica
        self.janela = Tk()
        self.janela.title("MT5")
        
        # Crie o frame superior para selecionar o ativo e o período
        self.frame_superior = Frame(self.janela)
        self.frame_superior.pack(side=TOP)
        
        # Crie a lista dropbox para selecionar o ativo
        self.ativo_selecionado = StringVar(self.frame_superior)
        self.ativo_selecionado.set(self.ativos[0])
        self.dropbox_ativos = OptionMenu(self.frame_superior, self.ativo_selecionado, *self.ativos)
        self.dropbox_ativos.pack(side=LEFT)
        
        # Crie a lista dropbox para selecionar o período
        self.periodo_selecionado = StringVar(self.frame_superior)
        self.periodo_selecionado.set(self.periodos[0])
        self.dropbox_periodos = OptionMenu(self.frame_superior, self.periodo_selecionado, *self.periodos)
        self.dropbox_periodos.pack(side=LEFT)
        
        # Crie o botão "Buscar Dados"
        self.botao_busca = Button(self.frame_superior, text="Buscar Dados", command=lambda: self.controller.buscar_dados_controller(self.ativo_selecionado.get(), self.periodo_selecionado.get()))
        self.botao_busca.pack(side=LEFT)
        
        # Crie o canvas para exibir o gráfico
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.janela)
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)
        
    def exibir_grafico(self, grafico_data, ativo, periodo):
        self.ax.clear()
        self.ax.plot(pd.to_datetime(grafico_data.index), grafico_data['close'])
        self.ax.set_title(f"Gráfico do Preço do {ativo} ({periodo})")
        self.ax.set_xlabel("Data")
        self.ax.set_ylabel("Preço (USD)")
        self.canvas.draw()
        
    def iniciar(self):
        self.janela.mainloop()


```



______________________________________________________________________________


#Arquivo Model.py:

Criar uma classe Model que será responsável por manipular os dados;
Mover a função buscar_dados para dentro da classe Model, renomeando-a para buscar_dados_model;
Na classe Model, criar um método get_grafico_data que retorna os dados do gráfico em formato apropriado.

    -CODIGO DO ARQUIVO model.py:

```python

import yfinance as yf

class Model:

    ativos = ["AAPL", "GOOGL", "MSFT", "BTC-USD"]
    periodos = ["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]

    def buscar_dados_model(self, ativo, periodo):
        ativo_ticker = yf.Ticker(ativo)
        ativo_data = ativo_ticker.history(period=periodo)
        return ativo_data
    
    def get_grafico_data(self, ativo_data):
        return {'index': ativo_data.index, 'close': ativo_data['Close']}
```

______________________________________________________________________________

#Arquivo main.py:

Na função buscar_dados, instanciar a classe Controller;
Substituir a chamada da função buscar_dados pela chamada do método buscar_dados_controller da classe Controller;
Adicionar a chamada do método exibir_grafico_controller após a chamada do método buscar_dados_controller.
O resultado final deve ser um código organizado em três arquivos distintos, onde cada arquivo possui responsabilidades específicas dentro do padrão MVC.

    -CODIGO DO ARQUIVO main.py:

```python

from controller import Controller

def main():
    controller = Controller()
    controller.view.iniciar()

if __name__ == "__main__":
    main()

```

