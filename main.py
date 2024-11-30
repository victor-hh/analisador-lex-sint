from lexer import getLexer
from parser import parser
import sys

def main():
    # if len(sys.argv) < 2:
    #     print("Uso: python main.py <arquivo_de_entrada>")
    #     sys.exit(1)
    
    # with open(sys.argv[1], 'r') as f:
    with open('teste.txt', 'r') as f:
        data = f.read()
    
    # Análise léxica
    # try: 
    #     lexer = getLexer()
    #     lexer.input(data)
    #     for tok in lexer:
    #         print(tok)
    # except Exception as error:
    #     print(error)

    try: 
        parser.parse(data, lexer = getLexer())
        print("Análise sintática concluída -> Nenhum Erro")
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()
