HW_10 PYTHON WEB

hw10_project/utils/docker-compose.yaml --створюємо контейнери для MongoDB , Postgres

hw10_project/utils/seed.py --заповнюємо базу MongoDB з utils/data (HW-8)

В браузері на localhost:8080 за допомогою Mohgo-express маємо доступ до заповненої бази(login: user, password: test123)

В терміналі ./hw10_project/python manage.py migrate -- застосувуємо початкову міграцію для PostgreSQL Django нашого проекту

В терміналі ./hw10_project/python manage.py makemigrations  -- створюємо міграцію

В терміналі ./hw10_project/ python manage.py runserver --  запускаємо наш сервер

В браузері на localhost:8000 --Працюємо з нашим додатком

В теці ./utils/migration.py скрипт для міграції бази MongoDB -> Postgres

Hаш додаток працює  з цитатами та авторами в MongoDB, а з користувачами у Postgres 
