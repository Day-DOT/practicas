print("Hola. Vamos a revisar tu equipo paso a paso.\n")

electricidad = input(
    "¿Tu equipo está conectado a la corriente y recibe energía? (s/n): "
).strip().lower() == "s"

if not electricidad:
    print("\nEntendido. El equipo no está recibiendo energía.")
    print("Revisa el cable de alimentación, el regulador y el tomacorriente.")

    regulador = input(
        "\n¿El regulador o multicontacto está encendido? (s/n): "
    ).strip().lower() == "s"

    if not regulador:
        print("\nEl problema podría estar en el regulador o multicontacto.")
        print("Enciéndelo o prueba conectar el equipo directamente a otro contacto.")

    else:
        print("\nEl regulador está encendido.")
        print("Prueba revisar el cable de alimentación de la computadora.")

else:
    print("\nPerfecto. El equipo está recibiendo energía.")

    enciende = input(
        "¿El equipo enciende al presionar el botón? (s/n): "
    ).strip().lower() == "s"

    if not enciende:
        print("\nEl equipo recibe energía pero no logra encender.")

        luces = input(
            "¿Se enciende alguna luz o se escucha algún ventilador? (s/n): "
        ).strip().lower() == "s"

        if luces:
            print("\nEl equipo recibe energía y presenta señales de vida.")
            print("Podría existir un problema con el botón de encendido, "
                  "la tarjeta madre o algún componente interno.")

        else:
            print("\nEl equipo no presenta ninguna señal de vida.")
            print("Revisa la fuente de poder, el cable y el botón de encendido.")

    else:
        print("\nExcelente. El equipo logra encender.")

        imagen = input(
            "¿Muestra alguna imagen en la pantalla? (s/n): "
        ).strip().lower() == "s"

        if not imagen:
            print("\nEl equipo enciende pero no muestra imagen.")

            monitor = input(
                "¿El monitor está encendido y muestra alguna señal? (s/n): "
            ).strip().lower() == "s"

            if not monitor:
                print("\nEl problema podría estar en el monitor.")
                print("Revisa su cable de alimentación y enciéndelo.")

            else:
                print("\nEl monitor está encendido.")
                print("Revisa el cable HDMI/VGA/DisplayPort.")
                print("También puede ser necesario revisar la memoria RAM "
                      "o la tarjeta gráfica.")

        else:
            print("\nPerfecto. El equipo muestra imagen.")

            sistema = input(
                "¿El sistema operativo inicia correctamente? (s/n): "
            ).strip().lower() == "s"

            if not sistema:
                print("\nEl equipo enciende y muestra imagen, "
                      "pero existe un problema al iniciar el sistema.")

                error = input(
                    "¿Aparece algún mensaje de error? (s/n): "
                ).strip().lower() == "s"

                if error:
                    print("\nPodría existir un problema con Windows/Linux.")
                    print("Anota el mensaje de error para identificar "
                          "el problema específico.")

                else:
                    print("\nEl sistema no inicia correctamente.")
                    print("Podría existir un problema con el disco, "
                          "los archivos del sistema o el proceso de arranque.")

            else:
                print("\nEl sistema operativo inicia correctamente.")

                lento = input(
                    "¿El equipo funciona demasiado lento? (s/n): "
                ).strip().lower() == "s"

                if lento:
                    print("\nEl equipo funciona pero presenta lentitud.")

                    programas = input(
                        "¿La lentitud ocurre al abrir programas? (s/n): "
                    ).strip().lower() == "s"

                    if programas:
                        print("\nPuede existir un problema de rendimiento.")
                        print("Revisa el uso de RAM, CPU y disco.")
                        print("También verifica los programas que "
                              "se ejecutan al iniciar Windows.")

                    else:
                        internet = input(
                            "¿La lentitud ocurre principalmente al navegar "
                            "por Internet? (s/n): "
                        ).strip().lower() == "s"

                        if internet:
                            print("\nEl problema podría estar relacionado "
                                  "con la conexión a Internet.")
                            print("Revisa la velocidad, el Wi-Fi o el router.")

                        else:
                            print("\nLa lentitud no parece estar relacionada "
                                  "con los programas ni con Internet.")
                            print("Puede ser necesario revisar el estado "
                                  "del disco o la cantidad de memoria RAM.")

                else:
                    print("\nEl equipo funciona correctamente.")

                    falla = input(
                        "¿Existe alguna otra falla específica? (s/n): "
                    ).strip().lower() == "s"

                    if falla:
                        print("\nVamos a analizar esa falla específica.")
                        print("Se recomienda identificar cuándo ocurre "
                              "y qué comportamiento presenta el equipo.")

                    else:
                        print("\nNo se detectó ninguna falla evidente.")
                        print("El equipo parece funcionar correctamente.")

print("\nFin del diagnóstico.")
print("Gracias por utilizar el sistema.")