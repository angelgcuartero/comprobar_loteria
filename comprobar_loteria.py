#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import sys
import time


api_url = 'http://api.elpais.com/ws/LoteriaNavidadPremiados'
# api_url + '?n=33488' --> comprueba el número 33488
# api_url + '?s=1'  --> pide status del sorteo

def main():
    """Recibe una lista de números en un fichero, uno en cada línea, y devuelve el premio"""
    
    if len(sys.argv) != 2:
        print('\nPor favor, introduzca el nombre de fichero con la lista de números.')
        print(sys.argv[0] + ' <fichero_con_numeros>\n')
        return 2

    input_file = sys.argv[1]

    try:
        with open(input_file) as in_f:
            lines = in_f.readlines()
    except FileNotFoundError:
        print(f'\nNo se encuentra el fichero {input_file}\n')
        return 1
        
    try:
        lines = [int(x.strip()) for x in lines]
    except ValueError:
        print('\nAsegúrese de que en cada línea sólo haya un número y de que tenga el formato correcto.\n')
        return 1

    # Dar la fecha del sorteo para estos resultados
    response = requests.get(f'{api_url}?t=1')
    json_data = json.loads(response.text[response.text.find('{'):])
    if not json_data['error']:
        ts = time.gmtime(json_data['timestamp'])
        tm_st = time.strftime("%d/%m/%Y", ts)
        print(f'\nLos resultados para este sorteo son de fecha: {tm_st}\n')

    # Dar la situación del sorteo
    status_msg = [
        "El sorteo no ha comenzado aún. Todos los números aparecerán como no premiados.",
        "El sorteo ha empezado. La lista de números premiados se va cargando poco a poco. \nUn número premiado podría llegar a tardar unos minutos en aparecer.",
        "El sorteo ha terminado y la lista de números y premios debería ser la correcta aunque, tomada al oído, no podemos estar seguros de ella.",
        "El sorteo ha terminado y existe una lista oficial en PDF.",
        "El sorteo ha terminado y la lista de números y premios está basada en la oficial. \nDe todas formas, recuerda que la única lista oficial es la que publica la ONLAE y deberías comprobar todos tus números contra ella."
    ]
    response = requests.get(f'{api_url}?s=1')
    json_data = json.loads(response.text[response.text.find('{'):])
    if not json_data['error']:
        print(f'{status_msg[json_data["status"]]}\n')

    # Dar los premios para cada número
    for n in lines:
        response = requests.get(f'{api_url}?n={n}')
        json_data = json.loads(response.text[response.text.find('{'):])
        result = 'error' if json_data['error'] else int(json_data['premio'])
        print(f'El número {n:05} tiene un premio de: {result}')
    
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
    
