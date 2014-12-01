ifeq ($(shell uname), Linux)
MAKE = make
else
MAKE = mingw32-make
endif

target = mytest
SRC_i = $(target).i

all:swig
	python setup.py build
	cp ./build/lib.win32-2.7/* ./../
	@echo "clean build"
	@$(MAKE) swigclean

swig:
	@echo "swig to python file....."
	swig -python $(SRC_i)

swigclean:
	@echo "clean swig output file....."
	@rm -rf $(target).py
	@rm -rf $(target)_wrap.c
	@rm -rf build

clean:
	@rm -rf *_wrap.c
	@rm -rf build
	@rm -rf *.pyc