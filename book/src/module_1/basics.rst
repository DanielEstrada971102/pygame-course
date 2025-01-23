Conceptos Básicos de Programación
=================================
El siguiente video es un gran material divulgativo que permite digerir el concepto de programar como
una forma de dar instrucciones a una computadora desde un enfoque historico. Es recomendable que tome
unos minutos para verlo antes de continuar.

.. raw:: html

    <div style="text-align:center">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Ca9Z23iqcwQ" frameborder="0" allowfullscreen></iframe>
    </div>

¿Qué es un **Algoritmo**?
-------------------------
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
El pseudocódigo es una forma de representar algoritmos utilizando un lenguaje similar a la
programación pero sin seguir una sintaxis estricta. Sirve para diseñar soluciones de manera comprensible
antes de codificarlas.

.. rubric:: Ejemplos

1. Calcular la suma de dos números.

.. code-block:: pseudocode
    
    Algoritmo Suma
        Leer valor1, valor2
        sum = valor1 + valor2
        Escribir sum
    FinAlgoritmo


2. Encontrar el número mayor en una lista.

.. code-block:: pseudocode

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
Un diagrama de flujo es una representación gráfica del proceso codificado en pseudocodigo de un algoritmo mediante símbolos estandarizados.

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


.. - Introducción a los algoritmos.
.. - Escritura de pseudocódigo.
.. - Creación de diagramas de flujo.