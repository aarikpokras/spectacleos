ALL: build
build:
	@cmake -Bbin
	@cd bin
	@make
