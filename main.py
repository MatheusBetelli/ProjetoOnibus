# main.py

# Importa o seu módulo de menu
from View import menu

# Se você tiver uma função que inicia o menu, chame-a aqui
# Supondo que seu menu.py tenha uma função iniciar(), por exemplo.
if __name__ == "__main__":
    print("Iniciando a aplicação...")
    # Se o seu menu.py executa o código diretamente, 
    # a linha 'from View import menu' já pode ser o suficiente para rodá-lo.
    # O ideal é ter uma função para chamar, como menu.iniciar_menu()