#include "garray_util.h"
#include <glib/gprintf.h>

void print_garray(GArray* arr)
{
    gint i;
    g_printf("Length: %d, ", arr->len);
    g_printf("[");
    for(i =0; i < arr->len; i++)
    {
        g_printf("%d ", g_array_index(arr, gint, i));
    }
    g_printf("]\n");
}

void assoc_index(GArray* arr, GArray* indices, GArray* ret)
{
    gint i;
    for(i =0; i < indices->len; i++)
    {
        gint index =  g_array_index(indices, gint, i);
        gint val =  g_array_index(arr, gint, index);
        g_array_append_val(ret, val);
    }
}

gint sum(GArray *arr)
{
    gint sum = 0;
    gint i;
    for(i =0; i < arr->len; i++)
    {
        gint val =  g_array_index(arr, gint, i);
        sum += val;
    }
    return sum;
}

gint max(GArray *arr)
{
    gint max = G_MININT;
    gint i;
    for(i =0; i < arr->len; i++)
    {
        gint val =  g_array_index(arr, gint, i);
        if(max < val)
        {
            max = val;
        }
    }
    return max;
}

