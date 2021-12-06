#.ONESHELL:
SHELL:=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

APP_NAME=python_aad_validation
VENV=/tmp/${APP_NAME}/env
GIT_DI:=$(shell pwd)
PYTHON=3.9

install: _install

setup: _setup_conda _install_modules

test: _unit_test

deploy:

build:

clean:

_install:
	( \
	apt-get update ;\
	apt-get upgrade ;\
	apt-get -y install make ;\
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh ;\
	chmod +x Miniconda3-latest-Linux-x86_64.sh ;\
	./Miniconda3-latest-Linux-x86_64.sh ;\
	)

_setup_conda:
	( \
	rm -fr ${VENV} ;\
	conda create -y --prefix ${VENV} python=${PYTHON} ;\
	conda init bash ;\
	)

_clean:
	( \
	del ${VENV} -Recurse -Force -Confirm:$false ;\
	)

_install_modules:
	( \
	$(CONDA_ACTIVATE) ${VENV} ;\
	python${PYTHON} -m pip install -r requirements.txt ;\
	which pip ;\
	pip list ;\
	)

_unit_test:
	( \
	$(CONDA_ACTIVATE) ${VENV} ;\
	cd unittest ;\
	python${PYTHON} -m unittest discover ;\
	)


_functional_test:
	( \
	$(CONDA_ACTIVATE) ${VENV} ;\
	cd functionaltest ;\
	python${PYTHON} -m unittest discover ;\
	)

_integration_test:
	( \
	$(CONDA_ACTIVATE) ${VENV} ;\
	cd _integration_test ;\
	python${PYTHON} -m unittest discover ;\
	)