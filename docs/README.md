# Modelagem de Classes
Este código apresenta uma implementação do padrão de arquitetura MVC (Model-View-Controller), onde cada um desses componentes é representado por uma classe específica. A seguir, é apresentada a modelagem de cada classe, com seus respectivos atributos e métodos.

## Classe Model
A classe Model representa o modelo de dados da aplicação. É responsável por buscar e armazenar os dados dos ativos financeiros escolhidos pelo usuário.

### Atributos:

`ativos`: lista de strings com os nomes dos ativos financeiros disponíveis.  
`periodos`: lista de strings com os períodos disponíveis para a busca dos dados.  

### Métodos:

`buscar_dados(ativo, periodo)`: recebe como parâmetro o nome do ativo financeiro e o período de busca dos dados. Utiliza a biblioteca yfinance para buscar os dados do ativo financeiro escolhido no período escolhido. Retorna duas listas de floats, uma contendo os preços de fechamento do ativo financeiro e outra contendo as datas correspondentes a cada preço.  


## Classe View
A classe View representa a interface gráfica da aplicação. É responsável por exibir as informações para o usuário e capturar suas ações.

### Atributos:

`controller`: referência ao objeto Controller da aplicação.  
`root`: objeto Tk do tkinter que representa a janela principal da aplicação.  
`superior_frame`: objeto Frame do tkinter que contém os widgets para a seleção do ativo e período de busca dos dados.  
`ativo_selecionado`: objeto StringVar do tkinter que armazena o nome do ativo financeiro selecionado pelo usuário.  
`dropbox_ativos`: objeto Combobox do tkinter que exibe a lista de ativos financeiros disponíveis para seleção.  
`periodo_selecionado`: objeto StringVar do tkinter que armazena o período selecionado pelo usuário.  
`dropbox_periodos`: objeto Combobox do tkinter que exibe a lista de períodos disponíveis para seleção.  
`botao_busca`: objeto Button do tkinter que aciona a busca dos dados do ativo financeiro selecionado pelo usuário.  
`fig`: objeto Figure do matplotlib que representa o gráfico a ser exibido na interface gráfica.  
`ax`: objeto Axes do matplotlib que representa os eixos do gráfico.  
`canvas`: objeto FigureCanvasTkAgg do matplotlib que representa a área do tkinter onde o gráfico é exibido.  


### Métodos:

`buscar_dados()`: captura os valores selecionados pelo usuário nos widgets da interface gráfica e chama o método buscar_dados do objeto Controller correspondente para buscar os dados do ativo financeiro selecionado. Chama o método plotar_grafico para exibir o gráfico correspondente na interface gráfica.  

`plotar_grafico(close, index)`: recebe como parâmetros as listas de preços de fechamento e datas do ativo financeiro selecionado. Utiliza o objeto Axes do matplotlib para plotar o gráfico correspondente na interface gráfica.  


## Classe Controller
A classe Controller representa o controlador da aplicação. É responsável por intermediar a comunicação entre a interface gráfica e o modelo de dados.

### Atributos:

`model`: referência ao objeto Model da aplicação.  
`view`: referência ao objeto View da aplicação.  


### Métodos:

`ativos()`: retorna a lista de ativos finance  
`periodos()`: retorna a lista de períodos disponíveis para busca dos dados.  


## Resumo

Classe | Atributos | Métodos | Descrição
------ | --------- | ------- | --------
Model | ativos (lista), periodos (lista) | buscar_dados(ativo, periodo) | Classe responsável por buscar os dados dos ativos selecionados no Yahoo Finance e retornar os preços de fechamento e os índices de tempo correspondentes.
View | controller, root, superior_frame, ativo_selecionado, dropbox_ativos, periodo_selecionado, dropbox_periodos, botao_busca, fig, ax, canvas | __init__(), buscar_dados(), plotar_grafico() | Classe responsável por criar a interface gráfica com o usuário, exibir o gráfico e receber as entradas do usuário.
Controller | model, view | __init__() | Classe responsável por instanciar o Model e a View e iniciar o programa.
