from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {"depends_on_past": True}

def myfunction(**context):
    print(int(context["ti"].xcom_pull(task_ids="tarea2")) - 24)


with DAG(dag_id="9-XCom",
         description="",
         schedule_interval="@daily",
         start_date=datetime(2025, 1, 1),
         end_date=datetime(2025, 1, 10),
         default_args=default_args) as dag:

    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 5 && echo $((3*8))")

    #Notése que ti, es una variable que representa una instancia de una tarea expecífica
    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 3 && echo {{ ti.xcom_pull(task_ids='tarea1') }}")

    t3 = PythonOperator(task_id="tarea3",
                        python_callable=myfunction)

    t1 >> t2 >> t3


    # Notas adicionales: La razón por al cual es bash operator comparte su output es porque por defecto tiene el parametro do_xcom_push en True lo mismo podemos hacer con el python operator pero este pusheara lo que coloquemos en el return de la función