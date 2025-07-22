# Projeto
> Automação para trocar o PPPoE de um roteador TP-LINK

# Rodar no terminal na pasta raiz e ser feliz

> **O venv é opcional, você pode pular para o passo 3. caso não tenha interesse em criar**

1. Crie um venv: 
  - `sudo apt install python3.12-venv`
  - `python -m venv venv`
2. Execute o venv: `source venv/bin/activate`
3. Instale os requisitos: `pip install -r requirements.txt`
4. Baixe o Chromium: 

``` bash 
sudo apt update
sudo apt install -y chromium-browser chromium-chromedriver
```

5. Seja feliz

**Chromium e bibliotecas são obrigatórias para rodar o projeto**

# Exemplo de execução

`python main.py --url http://192.168.2.254 --senha admin@7777 --pppoe 1234andzilla --modelo xx530`

- URL precisa ser `http` ou `https`
- Nenhum argumento pode ser vazio

  ## Flags
  - `--url` (Link para o roteador)
  - `--senha` (Senha do roteador)
  - `--pppoe` (Login PPPoE)
  - `--modelo` (Modelo do roteador)

# To-do 

- [ ] Verifica o modelo do roteador e roda um metodo proprio para aquele modelo
- [x] Tornas args obrigatórios por padrão 
- [x] verificar se não vai mandar infos erradas antes de executar
- [x] Rodar em segundo plano por padrão
- [x] Rodar sem precisar instalar um navegador
- [x] Teste no Linux
- [x] Validar URL e senha do roteador
- [x] Teste no Ubuntu Server
- [x] Log de ações feitas pela automação no terminal
- [x] Pasta de logs
- [ ] Testar compatibilidade com modelos TP-LINK 
  
  ``` bash 
  UI 1
  EX511,C20,EX141,EX220, EX520
  UI 2
  xx530, xx530V2, 
  ```