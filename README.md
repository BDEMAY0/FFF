# Fast Forensic Finder

This tool is based on [volatility](https://github.com/volatilityfoundation/volatility3), it automates everything and allows you to highlight elements that could be interesting

https://github.com/BDEMAY0/FFF/wiki


### Installation 
git clone https://github.com/BDEMAY0/FFF.git
\
cd FFF
\
git clone https://github.com/volatilityfoundation/volatility3.git

python -m venv venv

Activez l'environnement virtuel :

> Windows: .\venv\Scripts\activate
> 
> Linux/Mac: source venv/bin/activate

pip3 install -r requirements.txt
\
cd volatility3
\
pip3 install -r requirements.txt volatility3/requirements.txt 
\
cd ..
\

python main.py -f dump.dmp

options : 
