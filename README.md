# Rodar no terminal na pasta raiz e ser feliz

1. Crie um venv: `python -m venv venv`
2. Instale os requisitos: `pip install -r requirements.txt`

# Exemplo de execução

`python main.py --url http://192.168.2.254 --senha senha@roteador --pppoe 1234andzilla`

# To-do 

- [x] Tornas args obrigatórios por padrão 
- [x] verificar se não vai mandar infos erradas antes de executar
- [x] Rodar em segundo plano por padrão
- [x] Rodar sem precisar instalar um navegador
- [ ] Teste no Linux
- [ ] Validar URL e senha do roteador
