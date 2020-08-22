import sys
import os
from PIL import Image

#Grab first and second args
pastaOrigem = sys.argv[1]
pastaDestino = sys.argv[2]

#check if new folder exists. If not, create it
pastaExiste = os.path.isdir(pastaOrigem)
if pastaExiste:
    pastaExiste = os.path.isdir(pastaDestino)
    if pastaExiste:
        pass
    else:
        print('Pasta de destino de arquivos não existe')
        os.mkdir(pastaDestino)
        print(f'Pasta de destino {pastaDestino} criada')
        pastaExiste = True
else:
    print ('Pasta de origem de arquivos não existe')

#Loop thru folder
if pastaExiste:
    for arquivos in os.listdir(pastaOrigem):
        print(os.path.join(pastaOrigem, arquivos))
        #convert them to png
        imagem = Image.open(os.path.join(pastaOrigem, arquivos))
        arquivoSemExtensao = os.path.splitext(arquivos)[0]
        #save them to new folder
        print (os.path.join(pastaDestino, f'{arquivoSemExtensao}.png'))
        imagem.save (os.path.join(pastaDestino, f'{arquivoSemExtensao}.png'))

    print('Terminado')
