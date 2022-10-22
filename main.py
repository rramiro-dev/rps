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
    - las tiradas pueden ser infinitas hasta que uno de los 2 jugadores abandone la partida
    - si un usuario pierde 3 veces, su oponente gana, y se debe reiniciar o finalizar el juego
"""
import random

answers_pc = ['piedra','papel','tijera']

answers = {
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

pc_ans = random.choice(answers_pc)

def play_rps(user,pc):
    return answers[user][pc]

while True:
    try:
        user_ans = input('Piedra, papel, o tijera? ').lower().strip()

        if user_ans != pc_ans:
            print(f'Elegiste {user_ans}... {play_rps(user_ans,pc_ans)} contra {pc_ans}.')
            break
        else:
            while user_ans == pc_ans:
                user_ans = input('Piedra, papel, o tijera? ').lower().strip()
            print(f'Elegiste {user_ans}... {play_rps(user_ans,pc_ans)} contra {pc_ans}.')
            break
    except KeyError:
        print('Datos inválidos, Intente nuevamente...')