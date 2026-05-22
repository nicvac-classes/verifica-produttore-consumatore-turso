import threading
import random

DIM_BUFFER = 7
N_PRODUTTORI = 4
N_CONSUMATORI = 3
N_RICHIESTE = 4

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_drone():
    return f"DRN-{random.randint(100, 999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

   self.dato=genera_drone()
   def run(self):
    global
    genera_drone=0
    while genera_drone<N_RICHIESTE
        vuoto.acquire()
        mutexP.acquire()
        i_metti=metti
        metti=(metti+1) %DIM_BUFFER
        mutexP.relase()
        buffe[i_metti]=self.dato
        genera_drone+=1
        print{f"[SENSOR-N--{self.idx} drone segnalato{self-dato} inserito nel buffer {i_metti}]"}
        self.dato=genera_drone
     pieno.relase()


class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    def run(self)
        global=togli
        termina=None4
        while not(None):
            pieno.acquire()
            mutexC.acquire()
            i_togli=togli
            togli=(togli+1)%DIM_BUFFER
            mutexC.relase()
            if dato==None
            termina= True
            else:
                print(f"[RUNWAY-N{self.idx} autorizza atterraggio {self.dato} inserito nel buffer {i_metti}]")
        pieno.relase()
            


def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]
  
    for c in consumatori:
        c.start()
    for p in produttori
        c.start()

   
    for p in produttori
        p.join ()

    print("Tutti i sensori hanno terminato. Chiusura piste...")

    
    for _ in range(N_CONSUMATORI):
       vuoto.acquire()
       pieno.relase()
        pass


  for c in consumatori:
    c.join()


    print("Torre operativa chiusa.")


if __name__ == "__main__":
    main()
