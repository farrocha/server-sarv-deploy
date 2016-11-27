import json
import sys
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


speech_to_text = SpeechToTextV1(
    username='0c07e9f9-3cdc-419f-9030-7d8e529a104c',
    password='xoaRYdgel8kk',
    x_watson_learning_opt_out=False
)

archivo = sys.argv[1]
archivoDestino = sys.argv[2]

print '2.0 : Procesaremos el archivo ' + archivo
#print(json.dumps(speech_to_text.models(), indent=2))

print(json.dumps(speech_to_text.get_model('es-ES_BroadbandModel'), indent=2))
strJson =""
strResp=""

with open(archivo, 'rb') as audio_file:
    strResp = speech_to_text.recognize(audio_file, content_type='audio/ogg;codec=opus',model='es-ES_BroadbandModel', timestamps=True, word_confidence=True)
    strJson = json.dumps(strResp,indent=2,ensure_ascii=False).encode('utf8')


with open(archivoDestino, 'w') as destino:
    destino.write(strJson)

print 'DONE'