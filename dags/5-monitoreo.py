from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def myfunction():
    pass


with DAG(dag_id="5-monitoreo",
    description="",
    schedule_interval="@daily",
    start_date=datetime(2025,1,1),
    end_date=datetime(2025,1,12),
    default_args={"depends_on_past": True},
         max_active_runs=1) as dag:


    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 1 && echo 'Tarea 1'")

    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 1 && echo 'Tarea 2!")

    t3 = BashOperator(task_id="tarea3",
                      bash_command="sleep 1 && echo 'Tarea 3'")

    t4 = PythonOperator(task_id="tarea4",
                      python_callable=myfunction)

    t5 = BashOperator(task_id="tarea5",
                      bash_command="sleep 1 && echo 'Tarea 5'")


    t1 >> t2 >> t3 >> t4 >> t5
