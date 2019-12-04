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

    for n in lines:
        response = requests.get(f'{api_url}?n={n}')
        json_data = json.loads(response.text[9:])
        result = 'error' if json_data['error'] else int(json_data['premio'])
        print(f'El número {n:05} tiene un premio de: {result}')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
    