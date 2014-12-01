#include <Python.h>
 
static PyObject* add(PyObject* self, PyObject* args){
    int a = 0;
    int b = 0;
    if(!PyArg_ParseTuple(args, "i|i", &a, &b))
        return NULL;
    return Py_BuildValue("i", a+b);
}
 
static PyObject* sub(PyObject* self, PyObject* args){
    int a = 0;
    int b = 0;
    if(!PyArg_ParseTuple(args, "i|i", &a, &b))
        return NULL;
    return Py_BuildValue("i", a-b);
}
 
static PyMethodDef addMethods[]={
    {"add", add, METH_VARARGS},
    {"sub", sub, METH_VARARGS},
    {NULL, NULL, 0, NULL}
};
 
void initmytest(){
    Py_InitModule("mytest", addMethods);
}