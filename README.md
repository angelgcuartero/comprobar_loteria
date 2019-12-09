# Comprobar Lotería
Programa para comprobar una lista de números de la lotería nacional usando el API de El País.

Para más información sobre dicho API, por favor, visite [su página de documentación](https://servicios.elpais.com/sorteos/loteria-navidad/api/ "API de El País").

## Preparación
1. Crear un entorno virtual para Python. La versión requerida es 3.5 ó posterior.
2. Instalar en el mismo las dependencias:
    ```shell
    $> pip install -r requirements.txt
    ```

## Uso
1. Crear un fichero con la lista de números que se quieren comprobar, introduciendo solamente un número por línea. Se adjunta un fichero de ejemplo llamado ```numeros.txt``` para verificar.
2. Ejecutar el programa python:
    ```shell
    $> comprobar_lotería.py <numeros.txt>
    ```
