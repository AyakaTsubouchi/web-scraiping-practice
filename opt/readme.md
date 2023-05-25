How to run
1. Start Docker App
2. type the following command
`docker compose up -d --build`
3. see docker image list with `docker image ls`. you'll find the image named 'webscrapingpractice-python3'.
4. see the running container with `docker container ls`. you'll se python3
5. コンテナが走っていることを確認したところで、次のコマンドでコンテナへ接続（コンテナの中の環境に入ってその環境下でコマンドを打てるように）します。python3というのはdocker-compose.ymlで指定したコンテナの名前です。
type `docker compose exec python3 bash` python3というのはdocker-compose.ymlで指定したコンテナの名前です。これで次からターミナルで打つコマンドはコンテナ内の環境下で実行されるようになります。
6. run python file with `python sample.py 180.0`

How to finish
1. Kill the connection with `exit`
2. Terminate the container with `docker compose down`
3. Type `docker container ls` to check if docker is terminated.

How to restart
`docker compose up -d`

How to delete image
1. get the image id with `docker image ls`
2. `docker image rm imageid`

reference 
https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5