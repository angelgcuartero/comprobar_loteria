#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

api_url = 'http://api.elpais.com/ws/LoteriaNavidadPremiados'
# http://api.elpais.com/ws/LoteriaNavidadPremiados?n=33488
# http://api.elpais.com/ws/LoteriaNavidadPremiados?s=1  --> pide status del sorteo

def main():
    number_list = [3347, 44212, 48484, 9902, 1]

    for n in number_list:
        response = requests.get('{}?n={}'.format(api_url, n))
        json_data = json.loads(response.text[9:])
        print('El número {:5} tiene un premio de: {:8}'.format(n, int(json_data['premio'])))


if __name__ == '__main__':
    main()
    