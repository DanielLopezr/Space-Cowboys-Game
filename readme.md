# Space Cowboys Duels Game (Español): pygame version: 1.9.6 runs correctly in ubuntu 20.04

El juego cuenta con tres niveles, cada uno con su propio enemigo.
El objetivo del juego es derrotar a los tres alienígenas para ganar.

La jugabilidad del juego se centra en que en cada duelo, no solamente se necesita pericia y reflejos, si no que para disparar, una letra del teclado es seleccionada aleatoriamente. Entonces, hay que identificar la letra antes de que el alien dispare. Si la letra ingresada es equivocada, entonces el jugador también pierde.

El tiempo para realizar esta tarea, varía en cada nivel.  Siendo así:
* Nivel 1: 2 segundos
* Nivel 2: 1.5 segundos
* Nivel 3: 0.5 segundos

El juego cuenta con una pantalla de inicio, la cual muestra el titulo del juego y cuando se presiona espacio se comienzan los duelos.

Cada duelo tiene una cuenta atrás de tres segundos antes de mostrar la letra para disparar. Solamente queda probar el juego y disfrutar!

Para el diseño, se utilizaron vaqueros y enemigos genericos. Con inteligencia artificial, se modificaron estas imágenes para obtener villanos variados que nuestro heroe pueda enfrentar.  En cuestión de paisajes,  también se generaron con el modelo de inteligencia artificial Stable DIffusion. Para el apartado de sonido, se descargaron sonidos opensource. Los cuales suenan al disparar, ganar o perder.

En cuestión de código, se usaron funciones simples para programar los diferentes paisajes. La función clave es *show_game_screen()* la cual actualiza la posición de los personajes y sobreescribe los mensajes de conteo, balas, etc.

La logica es separada en 3 niveles en la función main, aunque se pudo realizar una clase para el juego, con los parámetros de cada nivel. Por cuestiones de tiempo se dejó lo más simple posible. Pero básicamente, la lógica consiste de dos loops. Uno para evaluar si el jugador presionó la tecla correcta o no y  para hacer el movimiento de la bala. Y otro para recorrer las balas disparadas, el jugador o el alien pueden disparar más de una bala (por eso ese efecto de que el alien dispara muchas veces).

Comentarios en inglés y en español se hicieron en el codigo, a veces por descuido y otras veces por costumbre.

Gracias por la oportunidad, espero que el juego les guste.
Autor: Daniel Felipe López Rubiano, Bogota DC, Colombia.

# Space Cowboys Duels Game (English): pygame version: 1.9.6 runs correctly in ubuntu 20.04

The game has three levels, each with its own enemy.
The object of the game is to defeat all three aliens to win.

The gameplay of the game focuses on the fact that in each duel, not only skill and reflexes are needed, but to shoot, a letter on the keyboard is randomly selected. So, you have to identify the letter before the alien shoots. If the entered letter is wrong, then the player also loses.

The time to perform this task varies at each level. Being so:
* Level 1: 2 seconds
* Level 2: 1.5 seconds
* Level 3: 0.5 seconds

The game has a start screen, which shows the title of the game and when you press space the duels begin.

Each duel has a three second countdown before showing the letter to shoot. It only remains to try the game and enjoy!

For the design, generic cowboys and enemies were used. With artificial intelligence, these images were modified to obtain various villains that our hero can face. In terms of landscapes, they were also generated with the Stable DIffusion artificial intelligence model. For the sound section, opensource sounds were downloaded. Which sound when shooting, winning or losing.

In a matter of code, simple functions were used to program the different landscapes. The key function is *show_game_screen()* which updates the position of the characters and overrides the count messages, bullets, etc.

The logic is separated into 3 levels in the main function, although it was possible to create a class for the game, with the parameters of each level. Due to time constraints, it was kept as simple as possible. But basically, the logic consists of two loops. One to evaluate if the player pressed the correct key or not and to make the movement of the bullet. And another to go through the bullets fired, the player or the alien can shoot more than one bullet (hence that effect that the alien shoots many times).

Comments in English and Spanish were made in the code, sometimes out of carelessness and other times out of habit.

Thanks for the opportunity, I hope you like the game.
Author: Daniel Felipe López Rubiano, Bogota DC, Colombia.
