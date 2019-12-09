#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import sys


api_url = 'http://api.elpais.com/ws/LoteriaNavidadPremiados'
# http://api.elpais.com/ws/LoteriaNavidadPremiados?n=33488
# http://api.elpais.com/ws/LoteriaNavidadPremiados?s=1  --> pide status del sorteo

def main():
    """Recibe una lista de números en un fichero, uno en cada línea, y devuelve el premio"""
    
    if len(sys.argv) != 2:
        print('Por favor, introduzca el nombre de fichero con la lista de números.')
        return -1

    input_file = sys.argv[1]

    try:
        with open(input_file) as in_f:
            lines = in_f.readlines()
    except FileNotFoundError:
        print(f'No se encuentra el fichero {input_file}')
        return -2
        
    lines = [int(x.strip()) for x in lines] 

    # Get lottery status
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

    # Get prize for each number
    for n in lines:
        response = requests.get(f'{api_url}?n={n}')
        json_data = json.loads(response.text[response.text.find('{'):])
        result = 'error' if json_data['error'] else int(json_data['premio'])
        print(f'El número {n:05} tiene un premio de: {result}')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
    