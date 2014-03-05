all: definitions

definitions: example-definitions/arithmetic.entangle
	@entangle generate python2 example-definitions/arithmetic.entangle definitions

clean:
	@rm -rf definitions

.PHONY: clean
