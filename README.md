# Reconhecimento facial com IA

## Configuração do projeto

### 1. Instalando `virtualenv`

​	Virtualenvs são uma forma de isolar diversos ambientes de desenvolvimento, assim permitindo ao programador utilizar versões específicas de diversos pacotes sem impactar instalações de outras aplicações ou sistemas.

1. Abra seu Prompt de comando e digite:

> ```py
> pip install virtualenv
> ```

2. Dentro do seu projeto, crie uma virtualenv:

   > ```py
   > python -m venv <nome da venv>
   > ```

3. Ativar a venv criada:

> ```py
> .\<nome da venv>\Scripts\activate
> ```

​	Após pressionar no **Enter**, irá aparecer nessa forma:

> ```assembly
> (nome da venv) C:\User\...\Desktop\(nome do seu projeto)
> ```

### 2. Instalação das ferramentas `opencv` e `mediapipe`

* Instalação opencv:

> ```py
> pip install opencv-python
> ```

* Instalação mediapipe:

> ```py
> pip install mediapipe
> ```



## Sites utilizados

1. [OPENCV](https://docs.opencv.org/3.4/index.html)

2. [MEDIAPIPE](https://google.github.io/mediapipe/)