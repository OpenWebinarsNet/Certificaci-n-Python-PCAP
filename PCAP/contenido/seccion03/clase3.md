# Nuestro primer módulo (2ª parte)
## Paso 6: Detección del contexto de ejecución

La variable `__name__` se puede usar para determinar si el archivo fue ejecutado directamente o importado. Al modificar `module.py` de la siguiente forma:

```
if __name__ == "__main__":
    print("Yo prefiero ser un módulo")
else:
    print("Me gusta ser un módulo")
```

* Si ejecutas `module.py` directamente, verás: `Yo prefiero ser un módulo.`
* Si ejecutas `programa1.py`, verás: `Me gusta ser un módulo.`

Este enfoque es útil para realizar pruebas dentro del módulo, que solo se ejecutan cuando el archivo se ejecuta directamente y no cuando se importa.

## Paso 7: Agregar un contador al módulo

En este paso, se introduce una variable global `contador` en el módulo para contar cuántas veces se invocan las funciones:

```
contador = 0

if __name__ == "__main__":
    print("Yo prefiero ser un módulo")
else:
    print("Me gusta ser un módulo")
```

Esta variable se inicializa en 0 cuando el módulo es importado.

## Paso 8: Acceso a variables del módulo

El archivo `main.py` se modifica para acceder a la variable `contador`:

```
import module
print(module.contador)
```

Este código es válido, pero plantea una cuestión sobre la privacidad de las variables. En Python, no existe un mecanismo para ocultar variables a los usuarios del módulo. Sin embargo, es una convención anteponer un guión bajo (`_`) o dos (`__`) al nombre de las variables para indicar que son "privadas". Aunque esto es solo un acuerdo, los usuarios del módulo pueden respetarlo o no.

## Paso 9: Añadir funciones al módulo

El módulo se actualiza para incluir dos funciones que calculan la suma y el producto de los elementos de una lista, además de un contador privado:

```
#!/usr/bin/env python3

""" module.py - Un ejemplo de un módulo en Python """

__contador = 0


def suma(lista):
    global __contador
    __contador += 1
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    return acumulador


def producto(lista):
    global __contador
    __contador += 1
    acumulador = 1
    for elemento in lista:
        acumulador *= elemento
    return acumulador


if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    mi_lista = [i+1 for i in range(5)]
    print(suma(mi_lista) == 15)
    print(producto(mi_lista) == 120)
```

* La línea `#!/usr/bin/env python3` indica al sistema operativo qué programa debe usar para ejecutar el archivo (importante en sistemas Linux).
* El doc-string (`""" module.py - Un ejemplo de un módulo en Python """`) proporciona una breve descripción del módulo.
* Las funciones `suma()` y `producto()` están disponibles para ser importadas y cuentan cuántas veces son llamadas mediante la variable `__contador`.
* La variable `__name__` se usa para ejecutar pruebas si el archivo es ejecutado directamente.

## Paso 10: Usar el módulo

Finalmente, el módulo puede usarse desde el archivo `programa1.py` de la siguiente manera:

```
from module import suma, producto

ceros = [0 for i in range(5)]
unos = [1 for i in range(5)]
print(suma(ceros))  # Salida: 0
print(producto(unos))   # Salida: 1
```

Este código importa las funciones del módulo y las utiliza para calcular la suma y el producto de los elementos en las listas `ceros` y `unos`.

## Paso 11: Cómo Python busca los módulos

En este paso, el escenario cambia y el archivo principal (`programa1.py`) se encuentra en una carpeta diferente a la del módulo. El ejemplo asume el siguiente entorno Linux:

* `programa1.py` está en: `~/python/programas`
* El módulo está en: `~/python/modulos`

Python busca los módulos en las carpetas especificadas en una lista llamada `sys.path`. Para verificar esta lista, se puede usar el siguiente código:

```
import sys

for p in sys.path:
    print(p)
```

Este código imprime las rutas que Python examina al buscar módulos. El primer elemento es la carpeta desde donde se ejecuta el script, seguida de varias otras rutas predeterminadas (como el directorio de instalación de Python y las bibliotecas de terceros). También puede incluir archivos `.zip`, ya que Python puede tratarlos como si fueran carpetas.

Para que Python encuentre el módulo en un directorio diferente, puedes modificar la lista `sys.path` agregando la carpeta correspondiente.

## Paso 12: Añadir una ruta a `sys.path`

Para que Python pueda encontrar el módulo en una carpeta diferente, se puede agregar su ruta, lo vemos en el archivo `programa2.py`:

```
from sys import path

path.append('../modulos')  # Añade la carpeta 'modulos' a sys.path

import module

ceros = [0 for i in range(5)]
unos = [1 for i in range(5)]
print(module.suma(ceros))   # Salida: 0
print(module.producto(unos))    # Salida: 1
```

* **Rutas relativas**: En el ejemplo, se usa una ruta relativa (`../modulos`), lo que significa que Python buscará la carpeta `modulos` ubicada un nivel por encima del directorio actual. Esta solución funciona si `programa2.py` se ejecuta desde la carpeta adecuada.
- **Rutas absolutas**: Si prefieres asegurarte de que Python siempre encuentra el módulo, puedes usar una ruta absoluta:  
  ```
  path.append('~/python/modulos')
  ```
- **Método `append()`**: Añade la nueva ruta al final de la lista `sys.path`. Si prefieres que la nueva ruta sea la primera en ser buscada, puedes usar `insert()` en lugar de `append()`.

Este método asegura que Python pueda importar módulos desde cualquier ubicación en el sistema, según las rutas agregadas a `sys.path`.

