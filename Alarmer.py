import time
import winsound

def Periodic_Point_Alarm(Begin_Hour='08:00', Final_Hour='22:00', Target_Minute=0, Duration_Second=5):
    """
    Genera una alarma cada una hora en un minuto especificado entre las horas especificadas.

    :param Begin_Hour: Hora de inicio en formato 24 horas (ejemplo: "08:00").
    :param Final_Hour: Hora de fin en formato 24 horas (ejemplo: "18:00").
    :param Target_Minute: Minuto dentro de cada hora donde suena la alarma (por defecto suena en el minuto 0).
    :param Duration_Seconds: Cuántos segundos dura la alarma.

    """

    while True:
        # Obtener la hora actual
        Now = time.localtime()
        Actual_Hour = time.strftime("%H:%M", Now)

        # Verificar si la hora actual está dentro del rango especificado.
        if Begin_Hour <= Actual_Hour < Final_Hour:
            # Si es el minuto y segundo exacto del Target_Minute
            if Now.tm_min == Target_Minute and Now.tm_sec == 0:
                # Reproducir el sonido de la alarma
                winsound.Beep(1000, Duration_Second*1000)  # Frecuencia 1000 Hz, duración 3000 ms.

            # Dormir hasta el siguiente segundo para no repetir el beep
            time.sleep(1)

        else:
            # Si no estamos en el rango de horas, dormir 60 segundos antes de verificar de nuevo
            time.sleep(60)

# Iniciar el programa de alarma.
Periodic_Point_Alarm()