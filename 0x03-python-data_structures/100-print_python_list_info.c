#include <Python.h>
/**
 * print_python_list_info - Python Shared Code
 * @p: list head
 *
 * prints some basic info about Python lists.
 *
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	size_t list_size = PyList_Size(p), i;
	size_t list_allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_allocated);
	for (i = 0; i < list_size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
