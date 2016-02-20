NAME       := $(shell python setup.py --name)
VERSION    := $(shell python setup.py --version)

image:
	docker build -t ${NAME}:${VERSION} .

package:
	python setup.py sdist bdist_wheel

