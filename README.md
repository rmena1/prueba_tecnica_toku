# Pelea de Superheroes

Este proyecto es la solución a la prueba técnica de ingreso a Toku.

El programa debe ser ejecutado con el siguiente comando:

```shell
python main.py
```

Al correr el programa, este creará dos equipos de cinco Superhéroes al azar y calculará todos sus parámetros. 
Una vez creados, se presentarán los dos equipos con sus respectivos Superhéroes y los principales parámetros de estos.

Luego, comenzará la pelea.
Para realizar la pelea, cada equipo atacará por turnos, y en cada turno se eligirá uno de los Superhéroes vivos del equipo atacante para que ataque a un Superhéroe al azar del equipo contrario.
El tipo de ataque con el que cada Superhéroe arremetirá a su contrincante también será elegido de forma aleatoria.
De esta forma, los equipos se atacarán por turnos y ganará el equipo que logre derrotar a todos los miembros del equipo contrario.

## Supuestos

1. Se supuso que los Superhéroes que no tienen disponible algún parámetro necesario en la API de superhéroes no podrá ser utilizado. (Por ejemplo, un superhéroe con atributo combat = 'null')

2. Se supuso que los Superhéroes con alignment distinto a 'good' o 'bad' no pertenecía a ninguno de estos bandos, es decir, se verán afectados negativamente por el filiation_coefficient.

3. Se supuso que actual_stamina es un parámetro único. En el enunciado se menciona que para cada atributo hay un parámetro actual_stamina y luego se incluye este en las fórmulas como atributo único, lo cual no me quedó claro.

4. Se supuso que el manejo de la pelea y las reglas de esta quedaban a libre elección ya que no se mencionaban en el enunciado.
