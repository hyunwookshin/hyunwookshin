FRONTEND := src/frontend/bootstrapvue
DIST := $(FRONTEND)/dist

install: setup
	sudo npm install -g @vue/cli
	cd $(FRONTEND) && npm i vue bootstrap-vue bootstrap

setup:
	make -C src/db setup

run:
	cd $(FRONTEND) && npm run serve

build: $(DIST)
	cd $(FRONTEND) && npm run build

clean:
	make -C src/db clean


.PHONY: install run build
