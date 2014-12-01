#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

#include "hello.h"
#include "world.h"

#define _snprintf_s(a,b,c,...) snprintf(a,b,__VA_ARGS__)


static int add_path(char* path_)
{
    char buff[1024];
    _snprintf_s(buff, sizeof(buff), "import sys\nif '%s' not in sys.path:\n\tsys.path.append('%s')\n", path_, path_);
    PyRun_SimpleString(buff);
    return 0;
}

int main(int argc, char const *argv[])
{
    hello();
    world();
    #ifdef _WIN32
    char pyHome[] = "python27";
    Py_SetPythonHome(pyHome);
    #endif
    char myPath[] = "papp";
    Py_Initialize();
    add_path(myPath);
    printf("Prefix: %s\nExec Prefix: %s\nPython Path: %s\n",
        Py_GetPrefix(),
        Py_GetExecPrefix(),
        Py_GetProgramFullPath());
    printf("Module Path: %s\n",
        Py_GetPath());
        printf("Version: %s\nPlatform: %s\nCopyright: %s\n",
        Py_GetVersion(),
        Py_GetPlatform(),
        Py_GetCopyright());
    printf("Compiler String: %s\nBuild Info: %s\n",
        Py_GetCompiler(),
        Py_GetBuildInfo());
        PyRun_SimpleString("import string");
    PyRun_SimpleString("words = string.split('rod jane freddy')");
    PyRun_SimpleString("print string.join(words,', ')");


    PyObject *strret, *mymod, *strfunc, *strargs;
    char *cstrret;
    mymod = PyImport_ImportModule("main");
    strfunc = PyObject_GetAttrString(mymod, "rstring");
    strargs = Py_BuildValue("(s)", "Hello World");
    strret = PyEval_CallObject(strfunc, strargs);
    PyArg_Parse(strret, "s", &cstrret);
    printf("Reversed string: %s\n", cstrret);

    Py_Finalize();
    return 0;
}
