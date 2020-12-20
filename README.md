                            ####################################################################
                            ####################################################################
                            ###                       JUEGO DE LA VIDA                       ###
                            ####################################################################
                            ####################################################################
                                                                         By : MiguelE Calambas M


Para ejecutar:                      
                python life_game.py [regla] [tiempo (segundos)] [lattice] 

                regla       :     Número entre 0 y 255
                tiempo      :     Duración en segundos que durara el juego
                lattice     :     Número mayor a 0, representa el tamaño de cada fila, el tamaño de las columnas será computado.

Una vez iniciado el juego usted podrá:

    Cambiar el estado de un elemento haciendo uso de su mouse, utilizando el botón izquierdo para pasarlo a vivo (1) y el botón 
        derecho para pasarlo  a estado muerto (0). Por defecto se pone en estado vivo al elemento del centro de la primera fila, 
        pero usted puede cambiar su estado antes de empezar la ejecución o durante esta.

    Tenga en cuenta que para actualizar el estado de un elemento se tiene en cuenta el estado de sus vecinos en la fila anterior 
        por lo cual se debe verificar que elementos se modifican durante la ejecución para poder apreciar los cambios. 

    Para iniciar o pausar la ejecución, pulse la tecla "espacio". El tiempo en el que la ejecución esté pausada no se 
        contabiliza en el tiempo total de ejecución.

    Para reiniciar la ejecución pulse la tecla "Escape". También se reinicia el tiempo de ejecución. 

    Para aumentar o disminuir la velocidad de la ejecución, use  las teclas "Flecha arriba" o "Flecha abajo", respectivamente. 