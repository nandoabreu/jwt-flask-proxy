NAME = proxy-compose

CONTAINER := $(shell docker ps --all --quiet --filter="name=$(NAME)")
CONTAINER := $(or ${CONTAINER},${CONTAINER},NO CONTAINER. To create: make)

.PHONY: run build stop start rm

run: build
	@echo "Running compose (up)..."
	docker-compose up --remove-orphans -d
	docker ps --filter="name=$(NAME)"
	@echo "Ready."

build:
	@echo "Building compose image, please wait..."
	docker-compose build --force-rm --pull --quiet
	@echo "Built."

stop:
	@echo "Stopping container..."
	docker container stop "$(CONTAINER)"
	@echo "Stopped."

start:
	@echo "Starting container..."
	docker container start "$(CONTAINER)"
	@echo "Ready."

rm:
	@echo "Cleaning up..."
	docker-compose down --remove-orphans --rmi all
	@echo "Done."

test:
	@echo "\n### Starting curl tests... ##########"
	-bash tests/curl-post.bash
	@echo "\n### Starting unittests... ###########"
	python3 -m pip install -r requirements.txt 1>/dev/null
	python3 -m unittest tests/test_*
	@echo "Done."

up: run
default: run

