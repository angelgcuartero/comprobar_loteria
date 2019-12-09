# Comprobar Lotería
Programa para comprobar una lista de números de la lotería nacional usando el API de El País, para ahorrar tiempo revisando los resultados.

Como ejemplo, incluye una lista de números para comprobar el uso.

Para más información sobre dicho API, por favor, visite [su página de documentación](https://servicios.elpais.com/sorteos/loteria-navidad/api/ "API de El País").

# Descargo de responsabilidad: 
> La **única lista oficial** contra la que hay que comprobar los resultados del sorteo de navidad es la que publica el Organismo Nacional de Loterías y Apuestas del Estado. El uso de este programa no implica la veracidad de los resultados. Haz un uso responsable del programa y de los resultados obtenidos.

## Preparación
1. Crear un entorno virtual para Python. La versión requerida es 3.5 ó posterior. Si necesitas información sobre esto, puedes pulsar [aquí](https://www.google.com/search?hl=es&q=entorno%20virtual%20python).
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
