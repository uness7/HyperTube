all: build run

run:
	docker compose up -d

build-and-run:
	docker compose up --build 

stop:
	docker compose stop

clean:
	docker compose down -v

fclean: clean
	docker system prune -af

db:
	docker compose exec db psql -U hypertube -d hypertube

migrate:
	docker compose exec backend python3 manage.py makemigrations

show-migrations:
	docker compose exec backend python3 manage.py showmigrations

re: stop run
