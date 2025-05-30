# Introducción a las cadenas de caracteres

Las cadenas de caracteres (`str`): Me permiten guardar secuencias de caracteres. Las cadenas de caracteres son inmutables, lo que significa que una vez creadas no se pueden modificar.

## Definición de cadenas

Podemos definir una cadena de caracteres de distintas formas:

```
cad0 = ""
cad1 = "Hola"
cad2 = '¿Qué tal?'
cad3 = '''Hola,
		que tal?'''
```

Un **carácter de escape**, indicado con una barra invertida permite escapar un carácter o introducir caracteres especiales:

* `\n`: Nueva línea.
* `\t`: Tabulador
* `cad4 = 'I\'m'`


## Operaciones básicas con cadenas de caracteres

Algunas de las operaciones que puedo realizar con las cadenas de caracteres son:

* Concatenación: `+`:  El operador + me permite unir datos de tipos secuenciales, en este caso dos cadenas de caracteres.

    ```
    "hola " + "que tal"
    'hola que tal'
    ```

    El operador `+` es empleado en dos o más cadenas y produce una nueva cadena que contiene todos los caracteres de sus argumentos (nota: el orden es relevante aquí, en contraste con su versión numérica, la cual es **conmutativa**).

* Repetición: `*`:  El operador * me permite repetir un dato de un tipo secuencial, en este caso de cadenas de caracteres.

    ```
    "abc" * 3
    'abcabcabc'
    ```

    El operador `*` necesita una cadena y un número como argumentos; en este caso, el orden no importa: puedes poner el número antes de la cadena, o viceversa, el resultado será el mismo: una nueva cadena creada por la enésima replicación de la cadena del argumento.

    La capacidad de usar el mismo operador en tipos de datos completamente diferentes (como números o cadenas) se llama **overloading - sobrecarga** (debido a que el operador está sobrecargado con diferentes tareas).

* Indexación: Puedo obtener el dato de una secuencia indicando la posición en la secuencia. En este caso puedo obtener el carácter de la cadena indicando la posición (**empezando por la posición 0**).

    ```
    cadena = "josé"

    cadena[0]
    'j'

    cadena[3]
    'é'
    ```

* Recorrido de cadenas

    Podemos usar la indiexación para hacer un recorrido:

    ```
    cadena = 'Python3 es bonito'

    for indice in range(len(cadena)):
        print(cadena[indice], end=' ')

    print()
    ```

    O utilizar la propiedad del bucle `for` para recorrer secuencias:

    ```
    cadena = 'Python3 es bonito'

    for caracter in cadena:
        print(caracter, end=' ')

    print()
    ```

* Rebanadas: Al igual que en las listas, podemos usar las rebanadas para crear nuevas cadenas:

    ```
    alpha = "abdefg"

    print(alpha[1:3])
    print(alpha[3:])
    print(alpha[:3])
    print(alpha[3:-2])
    print(alpha[-3:4])
    print(alpha[::2])
    print(alpha[1::2])
    ```

* Operadores de pertenencia: Al igual que las listas podemos usar los operadores de pertenencia. El operador `in` comprueba si el argumento izquierdo (una cadena) se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).

    ```
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    print("f" in alfabeto)
    print("F" in alfabeto)
    print("1" in alfabeto)
    print("ghi" in alfabeto)
    print("Xyz" in alfabeto)
    ```

    Vamos un ejemplo con el operador `not in`:

    ```
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    print("f" not in alfabeto)
    print("F" not in alfabeto)
    print("1" not in alfabeto)
    print("ghi" not in alfabeto)
    print("Xyz" not in alfabeto)
    ```



