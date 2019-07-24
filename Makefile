FRONTEND := src/frontend/bootstrapvue
DIST := $(FRONTEND)/dist

install:
	sudo npm install -g @vue/cli
	cd $(FRONTEND) && npm i vue bootstrap-vue bootstrap

run:
	cd $(FRONTEND) && npm run serve

build: $(DIST)
	cd $(FRONTEND) && npm run build

.PHONY: install run build
