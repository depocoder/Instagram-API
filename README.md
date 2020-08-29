# Instagram-API
 

## Описание проекта.   
Этот проект позволяет загружать в инстаграм фото сделанные спутником [Hubble](http://hubblesite.org/api/documentation).    
   
## Подготовка к запуску.  
Уставновить Python 3+.
```
sudo apt-get install python3
```
Установить, создать и активировать виртуальное окружение.
```
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```
Установить библиотеки командой.  
```
pip3 install -r requirements.txt
```
    
Зарегистрируйтесь в [instagram](https://www.instagram.com/accounts/emailsignup/).
# Аргументы
**username** — Ваш логин.   
**password** — Ваш пароль.   
    
## Запуск кода.  
**При запуске обязательно нужно использовать аргументы, логин и пароль от инстаграма**
```
python3 inst_parser.py --username rdepocode --password qwerty10
```
