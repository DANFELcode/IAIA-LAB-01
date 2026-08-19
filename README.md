# Laboratorio 01 — Búsqueda en espacio de soluciones (IAIA 2026-2)

**Grupo:** Azul
**Curso:** Inteligencia Artificial (IAIA) — Escuela Colombiana de Ingeniería
**Integrantes:** _(completar nombres del equipo)_

## Descripción

Este laboratorio implementa un modelo genérico de búsqueda sin adversario en
espacio de soluciones (`Node`, `Frontier`, `Problem`) y los algoritmos
**Best-First Search** y **A\***. Con esa base se resuelve el problema del
**granjero, el lobo, la oveja y la lechuga**: cruzar un río sin que ninguna
compra se coma a otra, usando A\* para encontrar la secuencia de cruces
óptima.

## Estructura del repositorio

```
├── Algoritmos/
│   ├── 2_1_1_modelar_estructura_datos.py   # Node y Frontier del espacio de búsqueda
│   ├── 2_1_2_modelar_problema.py           # Clase Problem genérica
│   ├── 2_2.py                              # expand, best_first_search, A* y prueba con grafo de ejemplo
│   └── 3_1_2_problema_granjero.py          # Modelado y solución del problema del granjero
├── Recursos/
│   └── Grafo.png                           # Grafo de ejemplo usado para probar Best-First Search
├── L01-IAIA-2026-2.pdf                     # Enunciado del laboratorio
├── Lab01-Azul.ipynb                        # Notebook con el desarrollo completo y explicaciones
└── README.md
```

## Cómo ejecutar

El desarrollo completo, con explicaciones y resultados, está en
`Lab01-Azul.ipynb`. Para reproducirlo:

1. Abrir el notebook con Jupyter.
2. Ejecutar las celdas en orden — cada sección corresponde a un punto del
   enunciado (`2.1.1`, `2.1.2`, `2.2.1`, `2.2.2`, `2.2.3`, `3.1`).

Los scripts en `Algoritmos/` contienen el mismo código de forma modular,
por si se prefiere ejecutarlos o importarlos por separado.

## Componentes implementados

### Modelo genérico

- **`Node`**: estado, nodo padre, acción, costo del camino y representación.
- **`Frontier`**: cola de prioridad (basada en `heapq`) parametrizada por una
  `evaluation_function`, con `is_empty`, `pop`, `top` y `add`.
- **`Problem`**: interfaz genérica con `initial`, `goals`, `is_goal`,
  `result_actions`, `action_cost` y `heuristic`.

### Algoritmos de búsqueda

- **Best-First Search**: expande siempre el nodo de menor valor según la
  `evaluation_function` recibida — es la base genérica de la que se derivan
  UCS, Greedy y A\*.
- **A\***: se obtiene pasándole a `best_first_search` la función de
  evaluación `f(n) = g(n) + h(n)`, es decir, costo acumulado del nodo más la
  heurística del estado (`node.cost + problem.heuristic(node.state)`), sin
  modificar el algoritmo genérico.

### Problema del granjero

- **Estado**: tupla `(granjero, lechuga, oveja, lobo)`, donde cada posición
  vale `0` (orilla de partida) o `1` (orilla destino).
- **Estado inicial**: `(0,0,0,0)` — **meta**: `(1,1,1,1)`.
- **Restricciones**: un estado es inválido si oveja y lobo, u oveja y
  lechuga, quedan en la misma orilla sin el granjero.
- **`result_actions`**: genera los estados a los que el granjero puede
  cruzar (solo o llevando una compra que esté en su misma orilla) y filtra
  los inválidos.
- **`action_cost`**: cada cruce cuesta `1`.
- **`heuristic`**: cantidad de elementos que aún están en la orilla de
  partida (admisible, nunca sobreestima los cruces restantes).

## Resultado

La búsqueda A\* encuentra la solución óptima en 7 cruces:

```
(0,0,0,0) -> (1,0,1,0) -> (0,0,1,0) -> (1,1,1,0) -> (0,1,0,0) -> (1,1,0,1) -> (0,1,0,1) -> (1,1,1,1)
```

Es decir: el granjero cruza con la oveja, vuelve solo, cruza con la
lechuga, vuelve con la oveja, cruza con el lobo, vuelve solo y finalmente
cruza con la oveja — dejando las tres compras intactas del otro lado.

## Referencias

[1] S. Russell and P. Norvig. *Artificial Intelligence: A Modern Approach*,
Global Edition. Pearson Education, 2021.
