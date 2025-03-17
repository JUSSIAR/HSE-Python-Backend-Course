## Setup

1) установите docker
2) установите python3
3) установите make
4) установите npx


## Launch

1) start storage

    ```shell
    cd storage
    chmod +x run.sh
    chmod +x stop.sh
    ./stop.sh
    ./run.sh
    cd ..
    ```
   
2) start web-server for frontend static

    ```shell
    make start_static_server
    ```
   
3) start django-server (backend & frontend api)

    ```shell
    make up_service
    ```