
all:
	make build
	make view

build:
	rm -rf ./out/
	mkdir -p ./out/
	python3 ./src/netx01.py
	python3 ./src/netx02.py
	python3 ./src/netx03.py

view:
	sxiv out/

