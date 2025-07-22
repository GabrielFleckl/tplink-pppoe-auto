
from utils.logger import configura_logger
from utils.driver import configurar_driver
from utils.validators import validar_argumento
from routers.tp_link_xx530 import executar_tp_link_xx530

import argparse

if __name__ == "__main__":
    configura_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("--modelo", required=True, choices=["xx530"], help="Modelo do roteador TP-Link")
    parser.add_argument("--url", required=True, type=validar_argumento, help="URL do roteador")
    parser.add_argument("--senha", required=True, type=validar_argumento, help="Senha do roteador")
    parser.add_argument("--pppoe", required=True, type=validar_argumento, help="Login PPPoE")
    args = parser.parse_args()

    if args.modelo == "xx530":
        executar_tp_link_xx530(args.url, args.senha, args.pppoe)
