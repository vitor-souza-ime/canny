# Canny Edge Detection

Este repositório contém um exemplo simples em **Python** utilizando **OpenCV** e **Matplotlib** para aplicar o filtro **Canny** em imagens obtidas diretamente da internet.

---

## 📂 Estrutura do Projeto

```

.
├── main.py        # Código principal com detecção de bordas
└── README.md      # Documentação do projeto

````

---

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/vitor-souza-ime/canny
cd canny
````

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Se não existir um `requirements.txt`, basta instalar manualmente:

```bash
pip install opencv-python numpy matplotlib
```

### 4. Execute o código

```bash
python main.py
```

---

## 📷 Exemplo

O código baixa uma imagem de Leonardo da Vinci, converte para tons de cinza e aplica o filtro **Canny**, exibindo o resultado:

* **Imagem Original**
* **Detecção de Bordas (Canny)**
<img width="725" height="427" alt="image" src="https://github.com/user-attachments/assets/73aeb124-bce8-430f-b03b-5f109f8b90f4" />

---

## 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

---

## 📌 Observações

* A URL da imagem pode ser trocada dentro do código (`main.py`), basta alterar a variável `url`.
* Os limiares do filtro Canny podem ser ajustados nos parâmetros:

  ```python
  cv2.Canny(gray, threshold1, threshold2)
  ```

---

## 📄 Licença

Este projeto é apenas para fins educacionais e está disponível sob a licença **MIT**.


