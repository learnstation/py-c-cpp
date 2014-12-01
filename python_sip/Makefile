TARGET = mymath.pyd
OFILES = sipmymathcmodule.o
HFILES = sipAPImymath.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DUNICODE -DQT_LARGEFILE_SUPPORT -I. -IC:\Python27\include
CFLAGS = -O2 -Wall
CXXFLAGS = -O2 -Wall
LFLAGS = -mthreads -Wl,-enable-stdcall-fixup -Wl,-enable-auto-import -Wl,-enable-runtime-pseudo-reloc -shared -Wl,-subsystem,windows -Wl,-s
LIBS = -L. -LC:\Python27\libs -lmymath -lpython27
.SUFFIXES: .cpp .cxx .cc .C .c


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@if not exist C:\Python27\Lib\site-packages mkdir C:\Python27\Lib\site-packages
	copy /y $(TARGET) C:\Python27\Lib\site-packages\$(TARGET)
	strip C:\Python27\Lib\site-packages\$(TARGET)

clean:
	-del $(TARGET)
	-del sipmymathcmodule.o
