from controle.controlador_sistema import ControladorSistema

def main():
    print("Iniciando sistema do Oscar...")
    
    controlador = ControladorSistema()
    controlador.abre_tela()

if __name__ == "__main__":
    main()
