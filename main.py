"""
Esta aplicación fue realizada en mis comienzos con python. La idea es practicar el lenguaje, la lógica, e iniciar mi primer proyecto con python.

- Nombre del juego: Piedra, papel, o tijera
- Cantidad jugadores: 2 (Usuario vs Máquina)
- Cantidad elementos: 3
- Elementos:
    - piedra
    - papel
    - tijera
- Reglas:
    - piedra le gana a tijera, pero pierde con papel
    - tijera le gana a papel, pero pierde con piedra
    - papel le gana a piedra, pero pierde con tijera
    - se juega al mejor de 3. Quien gane más rondas en un total de 3, gana el juego
- Conceptos utilizados:
    - librerias
    - arrays
    - diccionarios y acceso a sus claves y valores
    - objetos y métodos
    - funciones, con y sin argumentos
    - iteradores while y for
    - try/except
    - condicionales if/elif/else
    - variables
    - string interpolation
"""
import random

choices_pc = ['piedra','papel','tijera']
choices_user = {
    'piedra': {
        'papel': 'perdiste',
        'tijera': 'ganaste'
    },
    'papel': {
        'tijera': 'perdiste',
        'piedra': 'ganaste'
    },
    'tijera': {
        'piedra': 'perdiste',
        'papel': 'ganaste'
    }
}
n_rounds = 4 # 3 rounds for the 'for' iterator

# Clase constructora para cada usuario
class User:
    def __init__(self):
        self.nombre = None
        self.puntaje = 0
    
    def welcome(self):
        print(f'Welcome to the game, {(self.nombre).title()}.')
    
    def add_points(self):
        self.puntaje += 1
    
    def username_set(self):
        self.nombre = input(f'Introduzca su nombre de usuario: ')

# Definir funciones
def play_rps(user,pc):
    return choices_user[user][pc]

def assign_score():
    result = play_rps(user_ans,pc_ans)
    print(f'Elegiste {user_ans}... {result} contra {pc_ans}.')
    if result == 'ganaste':
        username.add_points()
    else:
        pc.add_points()
    print(f'Ronda {n} terminada.')

def pc_pick():
    global pc_ans
    pc_ans = random.choice(choices_pc) # PC picks a random element from the pc_response array

def user_pick():
    global user_ans
    user_ans = input('Piedra, papel, o tijera? ').lower().strip()

def final_results():
    if username.puntaje < pc.puntaje:
        print(f'¡Ganó {pc.nombre}! El partido salió {pc.puntaje} a {username.puntaje}.')
    elif username.puntaje > pc.puntaje:
        print(f'¡Felicidades {(username.nombre).title()}, ganaste el juego.! El partido salió {username.puntaje} a {pc.puntaje}.')
    else:
        print(f'¡Es un empate! El partido salió {pc.puntaje} a {username.puntaje}.')

# Instanciar valores de la PC
pc = User()
pc.nombre = 'PC'

# Pedir nombre de usuario del jugador
username = User()
while username.nombre == None or username.nombre == '':
    username.username_set()
username.welcome()

# Lógica del juego
for n in range(1, n_rounds):
    while True:
        try:
            pc_pick()
            print(pc_ans) # quitar esta línea cuando sea necesario... es solo de prueba
            user_pick()
            if user_ans != pc_ans:
                assign_score()
                break
            else:
                while user_ans == pc_ans:
                    pc_pick()
                    user_pick()
                assign_score()
                break
        except KeyError:
            print('Datos inválidos, Intente nuevamente...')

# Mostrar resultados finales
final_results()