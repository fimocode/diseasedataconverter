# Installation
## Install pip

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update

sudo apt-get install python3.6

sudo rm /usr/bin/python3

sudo ln -s python3.6 /usr/bin/python3

sudo apt install python3.6-dev libpython3-dev

sudo apt install python-pip python-wheel python-dev virtualenv

sudo virtualenv --system-site-packages -p python3.6 ./venv3

sudo apt-get install python-tk python3-tk tk-dev

source venv3/bin/activate

pip install -r requirements.txt

In case failed:

cat requirements.txt | xargs -n 1 pip install

cp .env.example .env
## Initialize DB

mysql -u root -p < schema.sql

# Run

python main.py
