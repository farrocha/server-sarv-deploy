import multiprocessing
print ("Determinando cantidad de procesadores")
cantidad = multiprocessing.cpu_count()
print ("Hay " + str(cantidad))

