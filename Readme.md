

## Step1: 
- clone the mongodb repo from https://github.com/Arqui-software-grupo03/mongodb.git
- `cd mongodb`
- `docker-compose up`

## Step 2
- Open a new terminal
- go to the users repo 
- `cd topics`
- `docker-compose build` && `docker-compose up`
- `docker exec -it appTopics ./manage.py makemigrations topics`
- `docker exec -it appTopics ./manage.py migrate`
- `docker exec -it appTopics python ./manage.py runserver 0.0.0.0:8080`
- try it:
        http://localhost:8000/admin