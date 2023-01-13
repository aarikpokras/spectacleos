ALL: build
build:
	@cmake -Bbin
	@cd bin
	@printf "\033[1;31m`cd bin;make`\033[0m"
