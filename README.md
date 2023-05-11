## yFinanceBot
- Este projeto é um bot para fins educacionais que utiliza a biblioteca yfinance para coletar informações sobre ações da bolsa de valores. O bot foi criado para praticar conceitos de programação e finanças, e pode ser útil para investidores que desejam automatizar o processo de coleta de dados.

## Estrutura do diretório
```
  yFinanceBot
  |___ Artefatos
        |___ Modelagens
        |___ Requisitos
        |___ Scripts
  |___ docs
  |___ tests
  |___ venv
  |___ requirements.txt
  |___ README.md
  |___ controller.py
  |___ main.py
  |___ model.py
  |___ view.py

```	

- Artefatos
  Pasta onde serão salvos os artefatos do projeto, incluindo:

  - /Modelagens: imagens de modelagens de casos de uso e diagramas de classe;
  - /Requisitos: arquivos de texto contento os requisitos e regras de negocio;
  - /Scripts: scripts base e ideias iniciais para modelagens futuras.

- /docs: Pasta com documentação do projeto, incluindo:

  - Documento de visão: Descreve o propósito do projeto, seus objetivos, público-alvo, escopo e funcionalidades.
  - Modelo de casos de uso: Representa as interações do usuário com o sistema e os resultados esperados.
  - Modelo de classes: Apresenta as classes do sistema, seus atributos e métodos.

- /tests: Pasta com arquivos de testes do programa.

- /venv: Pasta onde está o ambiente virtual Python (venv) com as dependências do projeto.

- requirements.txt: Arquivo que lista as dependências do projeto.

- Readme.md: Arquivo que contém informações sobre o projeto e sua estrutura.

_______________________________________________________________________________
## Instalação

# Para executar o programa, é necessário ter o Python 3.6 ou superior instalado no seu computador. Em seguida, siga as instruções abaixo:

- Faça o download ou clone o repositório para o seu computador.
  ```
  git clone git@github.com:Shepardy22/yFinanceBot.git
  ```
- Abra o terminal na pasta raiz do projeto.
- Crie e ative o ambiente virtual Python (venv):

  ```
  python -m venv venv
  ```
  - (Linux/Mac)
  ```
  source venv/bin/activate 
  ```
  - (Windows)
  ```
  venv\Scripts\activate 
  ```

# Instale as dependências do projeto:
```	
pip install -r requirements.txt
```


# Execute o programa:

  python 
  ```
    python main.py
  ```

# Contribuição
 - Este projeto é de código aberto e as contribuições são bem-vindas! Sinta-se à vontade para fazer um fork e enviar pull requests para melhorar o código e a documentação.

# Licença
- Este projeto está sob a licença MIT. Leia o arquivo LICENSE para mais informações.