# Rodar no terminal na pasta raiz e ser feliz

1. Crie um venv: `python -m venv venv`
2. Instale os requisitos: `pip install -r requirements.txt`
3. Baixe e deixe o Chromium na versão do seus sistema na raiz do projeto: 
   - `https://drive.google.com/file/d/1o3kI6FXk4VZ_IGJFHQuRsbgOSfochcid/view`

# Exemplo de como deve ficar a pasta raiz

``` bash
.
├── chromium_linux/
├── chromium-win/
├── venv/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

# Exemplo de execução

`python main.py --url http://192.168.2.254 --senha admin@7777 --pppoe 1234andzilla`

- URL precisa ser `http` ou `https`
- Nenhum argumento pode ser vazio

  ## Flags
  - `--url` (Link para o roteador)
  - `--senha` (Senha do roteador)
  - `--pppoe` (Login PPPoE)

# To-do 

- [x] Tornas args obrigatórios por padrão 
- [x] verificar se não vai mandar infos erradas antes de executar
- [x] Rodar em segundo plano por padrão
- [x] Rodar sem precisar instalar um navegador
- [x] Teste no Linux
- [x] Validar URL e senha do roteador
