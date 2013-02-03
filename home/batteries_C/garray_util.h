#ifndef __garray_util_h__
#define __garray_util_h__
#include <glib.h>
#include <glib/gprintf.h>
//associate a list of indices with an array of ints
void assoc_index(GArray* arr, GArray* indices, GArray* ret);
//These utils are all typed to contain ints inside the GArray's
void print_garray(GArray* arr);
gint sum(GArray *arr);
gint max(GArray *arr);
#endif
