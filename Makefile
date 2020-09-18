APP=thermometer
NS=texastribune

build:
	docker build --tag=${NS}/${APP} .

interactive: build
	docker run \
		--workdir=/app \
		--volume=$$(pwd):/app \
		--env-file=env \
		--rm --interactive --tty \
		--entrypoint=sh \
		--name=${APP} ${NS}/${APP}
