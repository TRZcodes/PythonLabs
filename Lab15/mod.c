#include <Python.h>
#include "insertion.h"
#include "euclidean.h"
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met1(PyObject *self, PyObject *args){
	int a,b,c=0;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=a+b+c;
  
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
			s+=PyLong_AsLong(PyList_GetItem(d,i));
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyObject *mod_met2(PyObject *self, PyObject *args){
	PyObject *a;
	if(!PyArg_ParseTuple(args, "O", &a)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
		int r=PyList_Size(a);
    int arr[r];
		for(int i=0; i<r; i++){
			arr[i]=PyLong_AsLong(PyList_GetItem(a,i));
		}
    
    InsertionSortCLang(arr,r);
    
    PyObject *newPyList=PyList_New(0);
    for(int i=0;i<r;++i)
    {
      PyList_Append(newPyList,PyLong_FromLong(arr[i]));
    }
	
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", newPyList);
}

static PyObject *mod_met3(PyObject *self, PyObject *args){
	PyObject *d;
	if(!PyArg_ParseTuple(args, "O", &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
		int r=PyDict_Size(d);
		int keys[r],values[r];
    PyObject* k, *v;
    k=PyDict_Keys(d);
    v=PyDict_Values(d);
    for(int i=0;i<r;i++)
    {
      keys[i]=PyLong_AsLong(PyList_GetItem(k,i));
      values[i]=PyLong_AsLong(PyList_GetItem(v,i));
    }

    PyObject *newPyDict=PyDict_New();
    for(int i=0;i<r;i++)
    {
      PyObject *newPyTuple=PyTuple_New(2);
      PyTuple_SetItem(newPyTuple,0,PyLong_FromLong(keys[i]));
      PyTuple_SetItem(newPyTuple,1,PyLong_FromLong(values[i]));
      PyDict_SetItem(newPyDict,newPyTuple,PyLong_FromLong(euclidean(keys[i],values[i])));
    }
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", newPyDict);
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met1", (PyCFunction)mod_met1, METH_VARARGS, "Funkcja 1"}, 
  {"met2", (PyCFunction)mod_met2, METH_VARARGS, "Funkcja 2"},
  {"met3", (PyCFunction)mod_met3, METH_VARARGS, "Funkcja 2"},
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}