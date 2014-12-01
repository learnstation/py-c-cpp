#
# (C) Copyleft 2011
# Late Lee from http://www.latelee.org
# 
# A simple Makefile for lib(libxxx.a)
# You just need to change library name and source file(s)
#

# 根目录
ROOTDIR = $(dir ${CURDIR})main

# 引入全局配置文件
include $(ROOTDIR)/config.mk

# static library name

Target = helloworld

ifeq ($(shell uname), Linux)
StaticLIB = $(obj)lib$(Target).a
LIB = $(obj)lib$(Target).a
ShareLib = $(SHARED_DIR)/lib$(Target).so
ShareFlags = -fPIC
else
StaticLIB = $(obj)lib$(Target).a
LIB = $(LIBs_DIR)/lib$(Target).a
ShareLib = $(SHARED_DIR)/lib$(Target).dll
ShareFlags = -DSHARE_EXE -DDLLEXPORT -s -shared -Wl,--subsystem,windows,--out-implib,$(LIB)
endif

CFLAGS += -I../helloworld/
# source file(s), including c file(s) cpp file(s)
# you can also use $(wildcard *.c) or *.c, etc.
SRC_C   := $(wildcard *.c) 
SRC_CPP := $(wildcard *.cpp)

# object file(s)
OBJ_C   := $(addprefix $(obj),$(patsubst %.c,%.o,$(SRC_C)))
OBJ_CPP := $(addprefix $(obj),$(patsubst %.cpp,%.o,$(SRC_CPP)))

all: $(StaticLIB) $(obj).depend share

share: $(ShareLib)

config:
	@echo "CURDIR is $(CURDIR)"
	@echo "ROOTDIR is $(ROOTDIR)"
	@echo "OBJTREE is $(OBJTREE)"
	@echo "obj is: $(obj)"
	@echo "$(ROOTDIR)/config.mk"
	@echo "$(ROOTDIR)/public.mk"

$(StaticLIB):  $(OBJ_C) $(OBJ_CPP)
	@echo "Generating static library: " $(notdir $@)
	$(AR) $(ARFLAGS) $@ $^

$(ShareLib):  $(SRC_C) $(SRC_CPP)
	@echo "Generating share library: " $(notdir $@)
	$(CXX)  -shared $(ShareFlags) $(CFLAGS) $^ -o $@

clean:
	@echo "Cleaning..."
	$(RM) $(StaticLIB) $(LIB) $(OBJ_C) $(OBJ_CPP) $(LIB) $(ShareLib) *.bak *~ $(obj).depend *.o

.PHONY: all  config $(LIB) clean

# 引入.c .cpp -> .o 和 .depend文件生成的规则
include $(ROOTDIR)/public.mk
