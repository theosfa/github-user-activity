import sys

def gua_entry() -> None:
    from gua.gua import main 
    main(sys.argv[1:])


if __name__=="__main__":
    gua_entry()