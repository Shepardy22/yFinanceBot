import yfinance as yf

class Model:
    def __init__(self):
        self.ativos = ["AAPL", "GOOGL", "MSFT", "BTC-USD"]
        self.periodos = ["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]
        
    def buscar_dados(self, ativo, periodo):
        ativo_ticker = yf.Ticker(ativo)
        ativo_data = ativo_ticker.history(period=periodo)
        return ativo_data['Close'], ativo_data.index
