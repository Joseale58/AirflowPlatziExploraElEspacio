from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_date():
    print("La fecha es: " + str(datetime.now()))

with DAG(dag_id="python_operator",
         description="Ejemplo de operador python",
         start_date=datetime(2025, 1, 10),
         schedule_interval="@once") as dag:

    #Tareas
    t1 = PythonOperator(task_id="hello_w_python",
                        python_callable=print_date)