COMPOSE ?= docker-compose -f docker-compose.yml
DEV_IMAGE ?= p-bot:dev

.EXPORT_ALL_VARIABLES:

run: build
	$(COMPOSE) up

build:
	docker build -t $(DEV_IMAGE) .

rm:
	$(COMPOSE) stop
	$(COMPOSE) rm -f
