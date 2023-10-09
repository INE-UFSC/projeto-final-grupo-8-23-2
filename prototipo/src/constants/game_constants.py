from app import App


# Instancia de App para extrair as informações da tela
app_obj = App()

# Constantes da tela
screen = app_obj.get_screen()
screen_width = app_obj.get_screen().get_width()
screen_height = app_obj.get_screen().get_height()
fps = 60
