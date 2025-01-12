# Proyecto para el curso de Airflow de Platzi

## Contexto:

Se busca desarrollar un flujo en Airflow que satisfaga el problema planteado en el archivo Proyecto.pdf (leer)

El DAG, que da solución a este planteamiento (solución reto) es dags/py-satellite.py



To run:

1. Activate virtual environment and launch Airflow webserver exexuting the file run_airflow.sh with the command: source run_airflow.sh

2. Open in Browser http://localhost:8080

3. On Airflow Webserver, run "py-satellite.py" DAG

4. See in the logs of the task number five (ShowDataCollected) the data "collected" from the satellite.


PD: En este ejercicio por cuestiones de tiempo, se omitieron los nodos 5 y 6 que debían ser tareas personalizadas que enviasen una notificación al equipo de análica y marketing, se reemplazo con un nuevo nodo llamado ShowDataCollected
