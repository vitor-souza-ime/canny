import cv2
import numpy as np
import urllib.request
import matplotlib.pyplot as plt

# URL da imagem (troque por outra se quiser testar)
url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Leonardo_da_Vinci_046.jpg/800px-Leonardo_da_Vinci_046.jpg"

# Criar request com User-Agent
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}
)

# Baixar a imagem da internet
resp = urllib.request.urlopen(req)
image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)

# Converter para formato OpenCV
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# Converter para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecção de bordas com Canny
canny_edges = cv2.Canny(gray, 100, 200)  # valores típicos de threshold

# Mostrar as imagens (original e com filtro Canny) em uma grade
titles = ["Original", "Filtro Canny"]
images = [image, canny_edges]

plt.figure(figsize=(10, 5))

for i in range(2):
    plt.subplot(1, 2, i+1)
    if len(images[i].shape) == 2:  # Imagem em escala de cinza
        plt.imshow(images[i], cmap="gray")
    else:  # Imagem colorida
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis("off")

plt.show()
