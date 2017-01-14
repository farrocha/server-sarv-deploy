import warnings
import json
import sys
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("/home/sarv/dejavu/dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

print "parametros..."
for arg in sys.argv:
    print arg

archivo_mp3 = sys.argv[1]
archivo_destino = sys.argv[2]
IDVersion = sys.argv[3]
print "Procesaremos " + archivo_mp3 + " y las huellas quedaran en " + archivo_destino

djv = Dejavu(config)
djv.fingerprint_file(archivo_mp3,archivo_destino,IDVersion)




