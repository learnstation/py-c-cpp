#
# (C) Copyleft 2011
# Late Lee from http://www.latelee.org
# 
# A simple Makefile for multi-directory
# Most idea comes from U-boot project
#

ROOTDIR	:= $(CURDIR)

include $(ROOTDIR)/config.mk

###############################################################################
# libs
target_helloworld = helloworld
targets :=  $(target_helloworld) m

_LIBS := \
../$(target_helloworld)/lib$(target_helloworld).a

LIBS := $(addprefix $(obj),$(_LIBS))

LDFLAGS = $(addprefix $(obj),$(_LIBS))

CFLAGS += -I../helloworld/

ifeq ($(shell uname), Linux)
CFLAGS += -I/usr/include/python2.7/
SharedLibPath_LDFLAGS = $(addprefix -L,$(SHARED_DIR))
SharedLibPath_LDFLAGS += -L/usr/lib/python2.7/config-i386-linux-gnu/
Sharedlibs := $(addprefix -l, $(targets))
Sharedlibs += -lpython2.7

else
CFLAGS += -I"C:\\Python27\\include"
SharedLibPath_LDFLAGS = $(addprefix -L,$(LIBs_DIR))
SharedLibPath_LDFLAGS += -L"C:\\Python27\\libs"

Sharedlibs := $(addprefix -l, $(targets))
Sharedlibs += -lpython27
endif

SharedLibaryPath = $(abspath $(BIN_DIR))

# main.cpp in this directory, can be empty

# source file(s), including c file(s) cpp file(s)
# you can also use $(wildcard *.c), etc.
SRC_C   := $(wildcard *.c)
SRC_CPP := $(wildcard *.cpp)

# object file(s)
OBJ_C   := $(addprefix $(obj),$(patsubst %.c,%.o,$(SRC_C)))
OBJ_CPP := $(addprefix $(obj),$(patsubst %.cpp,%.o,$(SRC_CPP)))

# executable file
target = $(STATIC_DIR)/a
shared_target = $(SHARED_DIR)/main

# python 
papp = papp

###############################################################################
#create static and shared Executable program
all: $(obj).depend share
ifeq ($(shell uname), Linux)
	$(shell cp -rf ../$(papp) $(SHARED_DIR)/)
else
	$(shell cp -rf ../$(papp) $(SHARED_DIR)/)
	$(shell cp -rf ../win32/python27 $(SHARED_DIR)/)
	$(shell cp -rf ../win32/dll/* $(SHARED_DIR)/)
endif

#create static Executable program
static: $(target)

#create shared Executable program
share: $(shared_target)

config:
	@echo "$(shell uname)"
	@echo "$(dir CURDIR)"
	@echo "abspath usage: $(abspath $(CURDIR))"
	@echo "CURDIR is $(CURDIR)"
	@echo "OBJTREE is $(OBJTREE)"
	@echo "obj is :$(obj)"
	@echo "LIBS is: $(LIBS)"
	@echo "CFLAGS is: $(CFLAGS)"
	@echo "LDFLAGS is: $(LDFLAGS)"
	@echo "SharedLibPath_LDFLAGS is : $(SharedLibPath_LDFLAGS)"

$(target): $(LIBS) exe

$(shared_target): $(LIBS) sharedexe

exe: $(OBJ_CPP) $(OBJ_C)
	@echo "Generating static executable file..." $(notdir $(target))
	$(CC) $(CFLAGS) $^ -o $(target) $(LDFLAGS)

sharedexe: $(OBJ_CPP) $(OBJ_C)
	@echo "Generating shared executable file..." $(notdir $(shared_target))
	$(CC) $^ -o $(shared_target) $(SharedLibPath_LDFLAGS) $(Sharedlibs) -Wl,-rpath, .

$(LIBS):
	@echo "***************************************"
	$(MAKE) -C $(dir $(subst $(obj),,$@))
	@echo "***************************************"

clean:
	@echo "cleaning..."
	@$(RM) $(target) $(shared_target)
	@find $(OBJTREE) $(BIN_DIR) $(LIBs_DIR) -type f \
		\( -name 'core' -o -name '*.bak' -o -name '*~' \
		-o -name '*.o'	-o -name '*.a' -o -name '*.exe'	-o -name '.depend' -o -name '*.so' -o -name '*.dll' \) -print \
		| xargs rm -f
	@$(RM) $(SHARED_DIR)/*

distclean:
	@echo "distcleaning..."
	@$(RM) $(target) $(shared_target)
	@find $(OBJTREE) $(BIN_DIR) $(LIBs_DIR) -type f \
		\( -name 'core' -o -name '*.bak' -o -name '*~' \
		-o -name '*.o'	-o -name '*.a' -o -name '*.exe'	-o -name '.depend' -o -name '*.so' -o -name '*.dll'\) -print \
		| xargs rm -f
	@$(RM) $(obj) $(BUILD_DIR)
	@$(RM) $(BIN_DIR)
	@$(RM) $(SHARED_DIR)


.PHONY: all clean distclean $(LIBS) exe


include $(ROOTDIR)/public.mk