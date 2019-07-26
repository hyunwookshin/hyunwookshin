FRONTEND := src/frontend/bootstrapvue
BACKEND := src/backend
DIST := $(FRONTEND)/dist

install: setup
	sudo npm install -g @vue/cli
	cd $(FRONTEND) && npm i vue bootstrap-vue bootstrap axios

backend: config setup
	sudo npm install --save serverless-python-requirements
	sls deploy

config:
	envsubst < $(BACKEND)/serverless.yml.tpt > serverless.yml
	envsubst < $(BACKEND)/handler.py.tpt > handler.py
	chmod a+x handler.py

setup:
	make -C src/db setup

run:
	cd $(FRONTEND) && npm run serve

build: $(DIST)
	cd $(FRONTEND) && npm run build

clean:
	make -C src/db clean
	rm -f serverless.yml
	rm -rf handler.py

clobber:
	sls remove || true

.PHONY: install run build clean setup run config check backend
