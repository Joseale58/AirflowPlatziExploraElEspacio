from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.sensors.filesystem import FileSensor

with DAG(dag_id="6.3-filesensor",
         description="",
         schedule_interval="@daily",
         start_date=datetime(2025, 1, 1),
         end_date=datetime(2025, 1, 10)) as dag:


    t1 = BashOperator(task_id="creating_file",
                      bash_command="sleep 10 && touch /tmp/airflow.txt")

    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/airflow.txt")

    t3 = BashOperator(task_id="end_task",
                      bash_command="echo 'El fichero ha llegado'")

    t1 >> t2 >> t3