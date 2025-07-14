# Rodar no terminal na pasta raiz e ser feliz

1. Crie um venv: `python -m venv venv`
2. Instale os requisitos: `pip install -r requirements.txt`
3. Baixe o Chromium portable e deixe as 2 pastas na raiz: `https://drive.google.com/file/d/1o3kI6FXk4VZ_IGJFHQuRsbgOSfochcid/view`

# Exemplo de execução

`python main.py --url http://192.168.2.254 --senha senha@roteador --pppoe 1234andzilla`

# To-do 

- [x] Tornas args obrigatórios por padrão 
- [x] verificar se não vai mandar infos erradas antes de executar
- [x] Rodar em segundo plano por padrão
- [x] Rodar sem precisar instalar um navegador
- [ ] Teste no Linux
- [ ] Validar URL e senha do roteador
