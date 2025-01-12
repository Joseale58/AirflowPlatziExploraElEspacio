from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.sensors.external_task import ExternalTaskSensor


with DAG(dag_id="6.2-externalTaskSensor",
         description="",
         schedule_interval="@daily",
         start_date=datetime(2025, 1, 1),
         end_date=datetime(2025, 1, 10)) as dag:


    t1 = ExternalTaskSensor(task_id="waitingDAG",
                            external_dag_id="6-externalTaskSensor",
                            external_task_id="tarea1", #Si queremos una tarea en específico, sino podemos omitir este parámetro
                            poke_interval=10) #Cada cuánto tiempo se va a estar revisando si la tarea externa ha terminado


    t2 = BashOperator(task_id="tarea2",
                     bash_command="sleep 10 && echo 'DAG 2 finalizado'",
                     depends_on_past=True)


    t1 >> t2