# Herencia de clases en Python

En el ámbito de la programación orientada a objetos, la herencia se refiere a la capacidad de una clase, conocida como **subclase**, para adquirir atributos y métodos de otra clase existente, denominada **superclase**. Esto permite **crear una nueva clase basada en una clase predefinida**, reutilizando su funcionalidad y, si es necesario, añadiendo nuevas características.

La herencia no solo promueve la reutilización del código, sino que también facilita la creación de jerarquías de clases más especializadas, donde las subclases pueden extender o modificar el comportamiento de sus superclases.

## La Relación entre superclases y subclases

Un aspecto crucial de la herencia es la relación entre las superclases y sus subclases. Esta relación es transitiva, lo que significa que si una clase B es una subclase de A, y C es una subclase de B, entonces C también es considerada una subclase de A. Esta característica permite construir jerarquías complejas de clases.

Consideremos un ejemplo simple de herencia en Python:

```
class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass
```

En este caso, las clases están vacías, pero ilustran la relación jerárquica:

* `Vehiculo` es la superclase de `VehiculoTerrestre` y `VehiculoOruga`.
* `VehiculoTerrestre` es una subclase de `Vehiculo` y, a su vez, la superclase de `VehiculoOruga`.
* `VehiculoOruga` es una subclase tanto de `Vehiculo` como de `VehiculoTerrestre`.

Un interrogante natural que surge es: ¿sabe Python cómo gestionar estas relaciones de herencia? La respuesta es sí. Python ofrece mecanismos que permiten a los programadores indagar sobre la estructura de clases y sus relaciones, facilitando la comprensión y el uso de la herencia en sus aplicaciones.

