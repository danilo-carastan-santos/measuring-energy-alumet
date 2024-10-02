import subprocess
from datetime import datetime
import time
import os

NB_CPUS = 16
PROC_TIME_SECONDS = 10
SLEEP_TIME_SECONDS = 1

ALUMET_RESULT_FILENAME = "../Results-CSV/"+datetime.now().strftime('%Y-%m-%d_%H:%M:%S')+"_alumet-output.csv"+".csv"

alumet_command = ["./alumet-local-agent"]

stress_command = ["./stress","-c",str(NB_CPUS),"-t",str(PROC_TIME_SECONDS)]

## Lancer Alumet et la commande stress

alumet_start = time.time()
## Lancer perf stat et ne pas attendre sa fin
alumet_pid = subprocess.Popen(alumet_command).pid

## Attendre un peu pour bien monitorer la commande stress
time.sleep(SLEEP_TIME_SECONDS)    

stress_start = time.time()
## Lancer la commande stress et attendre sa fin
subprocess.run(stress_command)
stress_end = time.time()

## Attendre un peu pour bien monitorer la commande stress
time.sleep(SLEEP_TIME_SECONDS)

## Terminer Alumet en envoyant SIGINT (-2)
## Équivalent à Ctrl+c
subprocess.run(["kill", "-2", str(alumet_pid)])

## Renommer le CSV de sortie d'Alumet
os.rename("./alumet-output.csv", ALUMET_RESULT_FILENAME)
print("Done")