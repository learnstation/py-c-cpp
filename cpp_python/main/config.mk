#
# (C) Copyleft 2011
# Late Lee from http://www.latelee.org
# 
# A simple file to specify compier and macros and flags
# and ways to compile .c & .cpp
# 这个文件不能自己独立运行，必须作为子makefile文件被其他主makefile引用
# 设置全局性的变量
# cross compile...
CROSS_COMPILE = 

CC = $(CROSS_COMPILE)gcc
CXX = $(CROSS_COMPILE)g++
AR = $(CROSS_COMPILE)ar

ARFLAGS = cr
RM = -rm -rf
ifeq ($(shell uname), Linux)
MAKE = make
else
MAKE = mingw32-make
endif

CFLAGS = #-Wall
DEBUG = y

ifeq ($(DEBUG), y)
CFLAGS += -g
DEBREL = Debug
else
CFLAGS += -O2 -s
DEBREL = Release
endif

DEFS = 

CFLAGS += $(DEFS)

LDFLAGS = $(LIBS)


# export to other Makefile
export CC
export CFLAGS
export INCDIRS
export AR
export ARFLAGS
export RM

###############################################################################
# 定义与当前项目有关的目录结构变量
INCDIRS = ../include/

CFLAGS +=-I$(INCDIRS)

#build file directory
BUILD_DIR := ../../build

# binary file directory
BIN_DIR := ../../bin

#static file directory
STATIC_DIR := ../../bin/static

# share libs file directory
LIBs_DIR := ../../bin/shared/libs
SHARED_DIR := ../../bin/shared

OBJTREE	:= $(if $(BUILD_DIR),$(BUILD_DIR),$(CURDIR))

# 在build目录下生成与程序目录相同的目录结构
obj := $(OBJTREE)/$(notdir $(CURDIR))/

ifneq ($(BUILD_DIR),)
$(shell mkdir -p $(obj))
endif

ifneq ($(BIN_DIR),)
$(shell mkdir -p $(BIN_DIR))
endif

ifneq ($(STATIC_DIR),)
$(shell mkdir -p $(STATIC_DIR))
endif

ifneq ($(LIBs_DIR),)
$(shell mkdir -p $(LIBs_DIR))
endif

ifneq ($(SHARED_DIR),)
$(shell mkdir -p $(SHARED_DIR))
endif

# 输出OBJTREE 给其他，makefile使用
export OBJTREE
