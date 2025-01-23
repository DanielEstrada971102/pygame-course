Conceptos Básicos de Programación
=================================
El siguiente video es un gran material divulgativo que permite digerir el concepto de programar como
una forma de dar instrucciones a una computadora desde un enfoque historico. Es recomendable que tome
unos minutos para verlo antes de continuar.

.. raw:: html

    <div style="text-align:center">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Ca9Z23iqcwQ" frameborder="0" allowfullscreen></iframe>
    </div>


Algoritmo
---------
Es una secuencia de **pasos** finitos y ordenados **que permiten resolver un problema o realizar una tarea**. 
Un buen algoritmo debe ser preciso, es decir, cada paso debe estar claramente definido. Adicionalmente, debe 
ser finito para poder llegar a la solución del problema. Este también debe plantearse de la manera más eficiente posible, es decir, 
los pasos deben poder ser realizarse en el menor tiempo.

Cuando se comienza a programar, una de las cosas más importante a desarrollar es la **lógica**, es decir, la capacidad de
pensar de manera estructurada y ordenada, para ser capaces de plantear los minimos pasos necesarios para resolver la tarea. 

Hay que tener en cuenta que la solución a un problema puede tener diferentes algoritmos o métodos que son completamente validos,
la eleccion de uno u otro dependera de la persona que lo desarrolle y de los factores que se quieran priorizar, como la velocidad de procesamiento,
la cantidad de memoria que se utilice, la facilidad de lectura del codigo, la interaccion con el usuario, entre otros.

.. rubric:: Ejemplos

1. **Problema**: Calcular la suma de dos números.
    - **Informacion de entrada**: Dos números enteros.
    - **Resultado o Salida**: La suma de los dos números.

        1. Recibir y guardar los valores ingresados
        2. Sumarlos.
        3. Retornar el resultado de la suma.

2. **Problema**: Preparar un sándwich.
    - **Informacion de entrada**: Tamaño (pisos), lista de ingredientes, etc...
    - **Resultado o Salida**: Un sándwich listo para comer.

        1. Tomar dos rebanadas de pan.
        2. Agregar cada ingrediente de la lista a una rebanada de pan.
        3. Tapar con la otra rebanada de pan.
        4. Repetir los pasos 1-3 según el tamaño del sándwich.
        5. Servir el sándwich.

3. **Problema**: Encontrar el número mayor en una lista.
    - **Informacion de entrada**: Una lista de números.
    - **Resultado o Salida**: El número mayor de la lista.

        1. Tomar una lista de números.
        2. Asignar el primer número como el mayor.
        3. Comparar con cada número en la lista.
        4. Si se encuentra un número mayor, actualizar la variable mayor.
        5. Al finalizar, devolver el número mayor.

Pseudocódigo
------------
.. note::
    Instale **PSeInt** para practicar pseudocódigo. Lo necesitarás de ahora en adelante.

El pseudocódigo es una forma de representar algoritmos utilizando un lenguaje similar a la
programación pero sin seguir una sintaxis estricta. Sirve para diseñar soluciones de manera comprensible
antes de codificarlas.

Para plantear pseudocódigo no hace falta más que lapiz y papel, sin embargo, existen herramientas como
`**PSeInt** <https://pseint.sourceforge.net/slide/pseint.html>`_ que permiten escribir y probar algoritmos 
de manera sencilla y cercano a lo que pasaria en un lenguaje de programación.

Puede descargar el instalador de PSeInt `aqui <https://pseint.sourceforge.net/index.php?page=descargas.php>`_, y puede
revisar la documentación oficial en este `link <https://pseint.sourceforge.net/index.php?page=documentacion.php>`_. Adicionalmente,
puede encontrar diversos tutoriales en youtube como por ejemplo `este <https://www.youtube.com/watch?v=FvibfpSVFBw&list=PLAzlSdU-KYwXllXcUCW-BylQZemcDV798>`_.

.. rubric:: Ejemplos

1. Calcular la suma de dos números.

.. code-block:: pseudocode
    :linenos:

    Algoritmo Suma
        Leer valor1, valor2
        sum = valor1 + valor2
        Escribir sum
    FinAlgoritmo


2. Encontrar el número mayor en una lista.

.. code-block:: pseudocode
    :linenos:

    Algoritmo Suma
        Dimension nums[5]
        // Leer los numeros
        Para i Desde 0 Hasta 4 Con Paso 1 Hacer
            Leer valor
            nums[i] = valor
        FinPara
        
        mayor = nums[0] 
        Para Cada num En nums Hacer
            Si num > mayor Entonces
                mayor = num
            FinSi
        FinPara
        
        Mostrar mayor
        
    FinAlgoritmo


Diagramas de Flujo
------------------
Un diagrama de flujo es una representación gráfica del proceso codificado en pseudocodigo de un algoritmo 
mediante símbolos estandarizados. Esta representacion basta con ser legible y entendible para poder 
representar la secuencia de pasos de un algoritmo, sin embargo, se usan como estandar los simbolos que 
se muestran `acá <https://es.wikipedia.org/wiki/Diagrama_de_flujo>`_.

.. rubric:: Ejemplos

1. Calcular la suma de dos números.

.. raw:: html

    <div style="text-align:center">
        <!-- <img src="../../_static/flow_diagram1_light.png" alt="Descripción de la imagen" widht=100x class="theme-light-image"> -->
        <img src="../../_static/flow_diagram1_dark.png" alt="Descripción de la imagen" width=300x class="theme-dark-image"> 
    </div>

2. Encontrar el número mayor en una lista.

.. raw:: html

    <div style="text-align:center">
        <!-- <img src="../../_static/flow_diagram2_light.png" alt="Descripción de la imagen" widht=100x class="theme-light-image"> -->
        <img src="../../_static/flow_diagram2_dark.png" alt="Descripción de la imagen" width=300x class="theme-dark-image"> 
    </div>

Ejercicios sencillos
--------------------

1. Escribir un algoritmo que solicite el nombre del usuario y lo salude.

.. literalinclude:: ../../../codes/mod-1/basics/ej-basic-1.ps
    :language: pseudocode
    :linenos:

2. Imprimir los números del 1 al 10 utilizando un bucle.

.. literalinclude:: ../../../codes/mod-1/basics/ej-basic-2.ps
    :language: pseudocode
    :linenos:

3. Generar la tabla de multiplicar de un número ingresado por el usuario.

.. literalinclude:: ../../../codes/mod-1/basics/ej-basic-3.ps
    :language: pseudocode
    :linenos:

4. Determinar si un número ingresado es positivo, negativo o cero. Tambien Verificar si un número es par o impar.

.. literalinclude:: ../../../codes/mod-1/basics/ej-basic-4.ps
    :language: pseudocode
    :linenos:
    :caption: Opción 1

.. literalinclude:: ../../../codes/mod-1/basics/ej-basic-4-op2.ps
    :language: pseudocode
    :linenos:
    :caption: Opción 2

5. Calcular el promedio de un conjunto de calificaciones ingresadas.

.. literalinclude:: ../../../codes/mod-1/basics/ej-basic-5.ps
    :language: pseudocode
    :linenos:

6. Calcular el área de un rectángulo ingresando la base y la altura.

.. literalinclude:: ../../../codes/mod-1/basics/ej-basic-6.ps
    :language: pseudocode
    :linenos:

.. important:: En los siguientes ejercicio se puede desplegar la solución, sin embargo, **INTENTE RESOLVERLO** por su cuenta antes de revisarla. 

.. dropdown:: 7. Calcular la suma de los primeros N números naturales.
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-7.ps
        :language: pseudocode
        :linenos:

.. dropdown:: 8. Determinar si un año ingresado es bisiesto.
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-8.ps
        :language: pseudocode
        :linenos:

.. dropdown:: 9. Convertir grados Celsius a Fahrenheit.
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-9.ps
        :language: pseudocode
        :linenos:

.. dropdown:: 10. Calcular el factorial de un número utilizando un bucle. (*)
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-10.ps
        :language: pseudocode
        :linenos:

.. dropdown:: 11. Generar una secuencia de Fibonacci hasta un número dado.
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-11.ps
        :language: pseudocode
        :linenos:

.. dropdown:: 12. Ordenar un arreglo de 5 números ingresados por el usuario de menor a mayor. (*)
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-12.ps
        :language: pseudocode
        :linenos:

.. dropdown:: 13. Buscar un número específico en una lista de valores.
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-13.ps
        :language: pseudocode
        :linenos:

.. dropdown:: 14. Contar la cantidad de números pares en un arreglo de N elementos.
    :chevron: down-up
    :animate: fade-in-slide-down

    .. literalinclude:: ../../../codes/mod-1/basics/ej-basic-14.ps
        :language: pseudocode
        :linenos:

-------------------------

Desafios
--------

1. Escribir un algoritmo que funcione como una **calculadora básica**. El usuario debe ingresar dos números y una operación (suma, resta, multiplicación o división), y el programa debe mostrar el resultado correspondiente.  

2. Diseñar un algoritmo que **convierta** una cantidad de dinero **de una moneda a otra** (por ejemplo, de dólares a euros o pesos). El usuario deberá ingresar la cantidad y seleccionar la moneda de destino.  

3. Implementar un **juego de adivinanza** en el que el programa genera un número aleatorio entre 1 y 100, y el usuario debe adivinarlo. Después de cada intento, el programa debe indicar si el número es mayor o menor que la suposición del usuario.

5. Diseñar un algoritmo que permita al usuario simular las funciones de un **cajero automático**. El usuario podrá consultar su saldo, realizar depósitos, retiros y salir del sistema. El programa debe validar que no se pueda retirar más dinero del que hay disponible.  

6. Diseñar un programa que simule el clásico juego **del ahorcado**. El programa debe seleccionar una palabra secreta y mostrarla como una serie de guiones. El usuario podrá ingresar letras una por una e ir descubriendo la palabra. Si la letra no está en la palabra, se debe descontar una vida. El juego termina cuando el usuario adivina la palabra o se queda sin intentos. Opcional: agregar una lista de palabras para elegir aleatoriamente y mostrar la cantidad de intentos restantes.
