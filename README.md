# ANALIZADOR SINTÁCTICO

El código que has proporcionado es un programa en Python que implementa un analizador sintáctico utilizando la biblioteca PLY (Python Lex-Yacc). El analizador sintáctico se define utilizando reglas de gramática en la notación de la sintaxis de las producciones (BNF).

El propósito de este analizador sintáctico es reconocer la estructura gramatical de un lenguaje de programación similar a PHP de manera jerárquica. Las reglas de gramática definidas en el código describen la estructura sintáctica del lenguaje. Cada regla de gramática se define con la función `p_<nombre>` que especifica cómo se deben combinar los tokens léxicos para formar una construcción gramatical válida.

La función `p_program` es la regla inicial de la gramática y define la estructura de un programa en este lenguaje. El analizador sintáctico lee el archivo de entrada especificado (por defecto es 'test.php'), lee su contenido y llama a `parser.parse()` para analizar el programa utilizando las reglas de gramática definidas. Si el análisis sintáctico tiene éxito, se imprime el mensaje "El analizador sintáctico ha reconocido correctamente todo".

En resumen, este código implementa un analizador sintáctico para un lenguaje de programación similar a PHP utilizando la biblioteca PLY en Python. El analizador sintáctico verifica si la estructura del programa cumple con las reglas de gramática especificadas.

```PY
import ply.yacc as yacc
from miniphp_lex import tokens
import miniphp_lex
import sys

VERBOSE = 1

# Definición de las reglas de gramática

def p_program(p):
    'program : OPENPHP declaration_list CLOSEPHP'
    pass

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration
    '''
    pass

def p_declaration(p):
    '''declaration : var_declaration
                    | fun_declaration
                    | statement_list
                    | header_declaration
    '''
    pass

# ... (resto de las reglas de gramática)

def p_error(p):
    if VERBOSE:
        if p is not None:
            print("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL TOKEN  " + str(p.value))
        else:
            print("ERROR SINTACTICO EN LA LINEA: " + str(miniphp_lex.lexer.lineno))
    else:
        raise Exception('syntax', 'error')

# Creación del analizador sintáctico

parser = yacc.yacc()

if __name__ == '__main__':

    # Lectura del archivo de entrada
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'test.php'

    f = open(file, 'r')
    data = f.read()

    # Análisis sintáctico del programa
    parser.parse(data, tracking=True)

    print("El analizador sintáctico ha reconocido correctamente todo")
```

## Descripcion

El código proporcionado es un analizador sintáctico implementado utilizando la biblioteca PLY en Python. El analizador sintáctico se utiliza para analizar programas en un lenguaje similar a PHP y verificar su estructura gramatical.

La variable `VERBOSE` se establece en 1 para mostrar mensajes de error detallados durante el análisis sintáctico. Si se encuentra un error sintáctico, se muestra un mensaje indicando la línea y el token inesperado.

A continuación, se definen las reglas de gramática utilizando la notación de la sintaxis de las producciones (BNF). Cada regla de gramática se define como una función que especifica cómo se deben combinar los tokens léxicos para formar una construcción gramatical válida.

Después de definir las reglas de gramática, se define una función `p_error` que se llama cuando se encuentra un error sintáctico. Si la variable `VERBOSE` es verdadera, se muestra un mensaje de error detallado indicando la línea y el token inesperado. De lo contrario, se lanza una excepción.

Luego, se crea el analizador sintáctico utilizando `yacc.yacc()`, que toma las reglas de gramática definidas.

En el bloque `if __name__ == '__main__':`, el programa verifica si se ha proporcionado un archivo de entrada como argumento de línea de comandos. Si se proporciona un archivo, se lee su contenido. De lo contrario, se asume que el archivo de entrada es "test.php". A continuación, se llama a `parser.parse()` para analizar el programa utilizando el analizador sintáctico creado. Si el análisis sintáctico tiene éxito, se imprime el mensaje "El analizador sintáctico ha reconocido correctamente todo".

## Uso

Para ejecutar el analizador sintáctico, sigue los siguientes pasos:

1. Asegúrate de tener instalada la biblioteca PLY en tu entorno de Python. Puedes instalarla utilizando pip:

```sh
pip install ply
```
2. Guarda el código proporcionado en un archivo Python, por ejemplo, `miniphp_parser.py`.

3. Asegúrate de tener un archivo de programa en un lenguaje similar a PHP que deseas analizar sintácticamente. Puedes crear un archivo llamado `test.php` y escribir tu código en él.

4. Abre una terminal y navega hasta la ubicación del archivo `miniphp_parser.py` y el archivo de programa `test.php`.

5. Ejecuta el analizador sintáctico utilizando el comando `python` seguido del nombre del archivo `miniphp_parser.py` y el nombre del archivo de programa `test.php`:
```sh
python miniphp_parser.py test.php
```
Si el archivo de programa no se encuentra en el mismo directorio que el archivo miniphp_parser.py, asegúrate de proporcionar la ruta completa del archivo.
6. Si el análisis sintáctico tiene éxito, se imprime el mensaje "El analizador sintáctico ha reconocido correctamente todo". De lo contrario, se muestra un mensaje de error indicando la línea y el token inesperado.
