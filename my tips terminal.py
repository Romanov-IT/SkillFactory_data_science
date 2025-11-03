command_dict = {'заморозить версии библиотек':'pip freeze > requirements.txt',
                'установить версии библиотек':'pip install -r requirements.txt'
               }

def find_command(name=input('введи имя команды')):
    for key, value in command_dict.items():
        if key.startswith(name):
            print(value)
find_command(name=input('введи имя команды'))