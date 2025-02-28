## Домашняя работа 4


### Формат сдачи домашки

- [формат](../../docs/homework-flow.md)


### Само дз + оценка


- **на 1 балл**:

    создать пустой проект в корне репозитория с файлом `README.md` с каким то описанием и пустым `requirements.txt`


- **на 2 балла**:

    добавить в корне проекта файл `server.py` и проинициализировать в нем приложение `flask`

    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
  
    @app.route("/")
    def server_info():
        return "My server"
  
  
    if __name__ == "__main__":
        app.run(debug=True, port=5000)
    ```
  
    также в `requirements.txt` добавить зависимость для `flask` (можно без версии)


- **на 3 балла**: 

    добавить в файле `server.py` вьюшку для того, чтобы узнать автора:

    ```python
    ...
  
    from flask import jsonify
    
    ...
    
    @app.route("/author")
    def author():
        author = {
            "name": "Stas",
            "course": 3,
            "age": 21,
        }
        return jsonify(author)
  
    ...
    ```
  

- **на 4 балла**: 

    добавить конфиг и зависимость в коде от конфига:

    создаем в корне файл `.env` и создаем там какие угодно настройки, например так:

    ```dotenv
    MODE=development
    DEBUG=True
    PORT=5000
    ```
  
    далее добавляем пакет `dotenv` в `requirements.txt` и в файле `server.py` добавляем любое применение конфига:
    
    ```python
    ...
  
    from dotenv import dotenv_values
  
    ...
  
    def get_port():
        config = dotenv_values(".env")
        if "PORT" in config:
            return config["PORT"]
        return 5000
    
    ...
    ```
  
    затем используем это в запуске приложение в том же файле `server.py`:

    ```python
    ...
  
    if __name__ == "__main__":
        app.run(debug=True, port=get_port())
    ```


- **на 5 баллов**:

    надо добавить файлик `Makefile` и описать в нем любой конфиг управления проектом, например так(для `macOS`):

    ```makefile
    PIP := venv/bin/pip
    PYTHON3 := venv/bin/python3
    
    clear:
        rm -rf venv
    
    venv:
        python3 -m venv venv
    
    install_requirements:
        ${PIP} install -r requirements.txt
    
    run:
        ${PYTHON3} server.py

    ```
  

- **на 6 баллов**: 
      
    добавить ручку, которая умела бы складывать числа из параметров - в файл `server.py` добавить:
    
    ```python
    ...
    
    from flask import request
  
    ...
  
    @app.route("/sum")
    def runner():
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
        return jsonify({'sum': a + b})
  
    ...

    ```
  
    пример гет запроса: `http://localhost:5000/sum?a=1&b=2`


- **на 7 баллов**:

    вынести сумму как функцию в контроллер:

    + создать в корне `controllers.py` с подобным содержанием:
        
        ```python
        def operation(a, b):
            if (a == None) or (b == None):
                return None
            return a + b
        ```
    
    + добавить в `server.py` использование контроллера:

        ```python
        ...

        from .controllers import operation

        ...

        @app.route("/sum")
        def runner():
            a = request.args.get('a', type=int)
            b = request.args.get('b', type=int)
            return jsonify({'sum': operation(a, b)})

        ...
        ```
    
- **на 8 баллов**: 

    покрыть контроллер тестами

    + добавляем пакет `pytest` в `requirements.txt`
    + добавлем в корне файл `test_controllers.py`:

        ```python
        import pytest
        from .controllers import operation
      
      
        @pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (5, -4, 1), (7, 8, 15)]
        def test_operation(a, b, expected):
            received = operation(a, b)
            assert received == expected
        ```
    + в файле `Makefile` добавляем сценарий для тестов:
  
        ```makefile
        ...
      
        TESTS := venv/bin/pytest -v ./test_controllers.py
      
        ...
      
        test:
            ${TESTS}
        ```
- **на 9 баллов**:

    добавить тайпинги где захочется
    
    + можно типизировать функцию извлечения порта из конфига
  
        ```python
        ...
      
        def get_port() -> int:
            config = dotenv_values(".env")
            if "PORT" in config:
                return config["PORT"]
            return 5000
        ...
        ```
        
    + можно типизировать контроллер

        ```python
        def operation(a: int, b: int) -> int:
            if (a == None) or (b == None):
                return None
            return a + b
        ```

    + можно типизировать тесты

        ```python
        @pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (5, -4, 1), (7, 8, 15)]
        def test_operation(a: int, b: int, expected: int) -> None:
            received = operation(a, b)
            assert received == expected
        ```

    + можно все что еще захочется

- **А если все это заработает, то будет 10!**

### Дедлайны

- Дедлайн без понижающего коэффициента: **30.12.2024**
- Дедлайн с понижающим коэффициентом 0.5: **15.01.2025**
- Далее понижающий коэффицент равен 0.1 и не сгорает

Финальный дедлайн по всем ДЗ - 25.03.2025 (25 марта) !!!
