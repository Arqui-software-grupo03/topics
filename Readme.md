to run:

    docker-compose build && docker-compose up

    docker exec -it appTopics ./manage.py makemigrations topics

    docker exec -it appTopics ./manage.py migrate

    docker exec -it appTopics python ./manage.py runserver 0.0.0.0:8000

    try it:
        http://localhost:8000/admin