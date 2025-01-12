from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def print_date():
    print("La fecha es: " + str(datetime.now()))

with DAG(dag_id="dependencia",
         description="Ejemplo de dependencia entre tareas",
         start_date=datetime(2025, 1, 10),
         schedule_interval="@once") as dag:

    #Tareas
    t1 = PythonOperator(task_id="print_date3",
                        python_callable=print_date)

    t2 = BashOperator(task_id="wait_53",
                      bash_command="sleep 5")

    t3 = BashOperator(task_id="wait_13",
                      bash_command="echo 'Andy no me toques los cojones'")

    t4 = BashOperator(task_id="finaliza",
                      bash_command="sleep 1")

    t1 >> t2 >> [t3,t4]