include ../../common.mk

VIRTUAL_ENV := $(GIT_ROOT)/src/db/venv

setup: $(VIRTUAL_ENV)
	./setup.sh $(VIRTUAL_ENV)

$(VIRTUAL_ENV):
	virtualenv -p python3 --system-site-packages $@

clean:
	rm -rf *.pyc
	rm -rf $(VIRTUAL_ENV)
