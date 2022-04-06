# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

ls_7_path = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for root, folders in ls_7_path.items():
    if os.path.exists(root):
        print(root, 'такая папка уже существует')
    else:
        for folder in folders:
            ls_path_dz = os.path.join(root, folder)
            os.makedirs(ls_path_dz)
