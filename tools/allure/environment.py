import platform
import sys
from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(
            f"{properties}\nos_info={platform.system()}, {platform.release()}\npython_version={sys.version}")  # Записываем переменные в файл
