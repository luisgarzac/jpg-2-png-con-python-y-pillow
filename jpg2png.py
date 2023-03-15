# Importamos Image de la librería PIL
from PIL import Image

# formato Image.open(fp,mode = 'r',formato)
imagen = Image.open(r'imagen1.jpg') # Creamos el objeto que almacena la imagen en "imagen"
# formato Image.save(fp,formato,parametros)
imagen.save('imagen2.png') # Con save() asignamos el nombre y formato de la nueva imagen