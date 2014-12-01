#include <stdio.h>
#include <string.h>
#include <math.h>
#ifdef _WIN32
#include <cstdlib>
#endif

#include "ffpython.h"

#include "hello.h"
#include "world.h"


static int cp(int n)
{
    float result=0;
    for (int i = 0; i < n; ++i)
    {
        result += pow(1.1, sin(i) + cos(i));
    }
    return result;
}

static int cp1(int n)
{
    long lResult = 0;
    for(int i = 0; i < n ; i ++)
    {
         for(  int j = 0; j < n; j ++)
         {
                lResult += (long) ( i * j );
         }
    }
    return lResult;
}


int main(void)
{
    hello();
    world();
    #ifdef _WIN32
    char pyHome[] = "python27";
    Py_SetPythonHome(pyHome);
    #endif

    Py_Initialize();
    ffpython_t::add_path("./papp");
    ffpython_t ffpython;
    printf("sys.version=%s\n", ffpython.get_global_var<string>("sys", "version").c_str());
    ffpython.call<void>("main", "main");

    ffpython_t numc;
    numc.reg(&cp, "cp")\
    .reg(&cp1, "cp1");

    numc.init("numc");
    numc.call<void>("main", "cp_cpp");

    Py_Finalize();
    printf("====================\n");
    return 0;
}
