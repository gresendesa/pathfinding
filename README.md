# pathfinding


## Instalação

 1. Instale o virtualenv e algumas dependências
```console
$ sudo apt-get install virtualenv build-essential python-dev libxml2 libxml2-dev zlib1g-dev
```
 2. Crie um ambiente virtual e instale a biblioteca igraph
```console
$ virtualenv -p python2 venv_py2
$ source venv_py2/bin/activate
(venv_py2) $ pip install python-igraph pycairo pydot
```
 3. Inicie o ambiente virtual e rode algum dos scripts

```console
$ source venv_py2/bin/activate
(venv_py2) $ cd pathfinding
(venv_py2) $ python djikstra.py
```