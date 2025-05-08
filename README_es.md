# Tropel Musical Simulation

[Read in English](./README.md)

## Autores

- Kevin Sebastián Cifuentes López
- Mariana Lopera Correa
- Emanuel García Ríos

## Descripción

Tropel Musical es una simulación física interactiva que utiliza Pygame y Pymunk para modelar un sistema de dominós, rampas y bolas. El objetivo es proporcionar una experiencia visual y educativa sobre cómo funcionan las interacciones físicas en un entorno simulado.

---

## Cómo Ejecutar el Proyecto

### Clonación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/tropel-musical.git
   ```

   **Nota:** Si deseas realizar cambios, por favor haz un fork del repositorio y trabaja en tu propio fork.

### Instalación de Dependencias

Este proyecto utiliza `poetry` para la gestión de dependencias. Si no tienes `poetry` instalado, sigue las instrucciones en la [documentación oficial de Poetry](https://python-poetry.org/docs/).

1. Instala `poetry` (si no lo tienes):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd tropel-musical
   ```

3. Instala las dependencias:

   ```bash
   poetry install --no-root
   ```

### Cómo Correr la Interfaz de Usuario

1. Activa el ambiente virtual de `poetry`:

   **Nota:** ve a la página oficial de Poetry para verificar como se activa el ambiente virtual, es importante que lo actives para que puedas ejecutar con normalidad el proyecto dentro de tu ambiente virtual usando el interprete del ambiente. [Activación del ambiente](https://python-poetry.org/docs/managing-environments/#bash-csh-zsh)

   ```bash
   eval $(poetry env activate)
   ```

2. Ejecuta el archivo principal para iniciar la simulación:

   ```bash
   python src/view/gui/tropel_musical_gui.py
   ```

---

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```bash
tropel-musical/
├── README.md
├── poetry.lock
├── pyproject.toml
├── src/
│   ├── model/
│   │   └── tropel_musical_model.py
│   ├── view/
│   │   └── gui/
│   │       └── tropel_musical_gui.py
```

- **README.md**: Documentación del proyecto.
- **poetry.lock** y **pyproject.toml**: Archivos de configuración de `poetry` para la gestión de dependencias.
- **src/**: Carpeta principal del código fuente.
  - **model/**: Contiene la lógica del modelo físico.
  - **view/gui/**: Contiene la interfaz gráfica de usuario.

---

## Explicación del Código

### `tropel_musical_model.py`

Este archivo contiene las funciones principales para crear los elementos físicos de la simulación:

- **`create_boundaries`**: Define los límites del espacio físico.
- **`create_ball`**: Crea una bola con propiedades físicas específicas.
- **`create_table`**: Genera una mesa estática en el espacio.
- **`create_ramps`**: Crea una serie de rampas alternadas.
- **`create_domino`**: Genera un dominó con propiedades físicas.

### `tropel_musical_gui.py`

Este archivo contiene la lógica para la interfaz gráfica y el bucle principal del programa:

- **`draw`**: Dibuja los elementos del espacio físico en la ventana de Pygame.
- **`ball_hits_domino`**: Maneja las colisiones entre la bola y los dominós.
- **`create_dominoes`**: Crea una fila de dominós en el espacio.
- **`run`**: Ejecuta el bucle principal, manejando eventos y actualizando la simulación.

Con esta estructura, el proyecto combina la lógica física con una interfaz gráfica interactiva para simular un sistema dinámico de objetos.

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](./LICENSE).
