#include "dbg.h"
#include "comb.h"
#include "garray_util.h"
#include <glib/gprintf.h>
#include <stdlib.h>

gint checkio(GArray *arr)
{
    gint min_diff = max(arr);
    gint comb_len;
    for(comb_len =0; comb_len < arr->len; comb_len++)
    {
        GArray* variants = g_array_new (FALSE, FALSE, sizeof (GArray*));
        comb(arr->len, comb_len, 0, 0, variants);
        gint i;
        for(i =0; i < variants->len; i++)
        {
            GArray* comb_i = g_array_index(variants, GArray*, i);
            GArray* combl = g_array_new (FALSE, FALSE, sizeof (gint));
            assoc_index(arr, comb_i, combl);
            gint diff = abs(2 * sum(combl) - sum(arr));
            //print_garray(combl);
            //g_printf("%d\n",diff);
            if(diff < min_diff)
            {
                min_diff = diff;
            }
            g_array_free(combl, TRUE);
        }
        g_array_free(variants, TRUE);
    }
    g_printf("%d\n",min_diff);
    return min_diff;
}

GArray* create_items(int items[], int len)
{
    GArray* a = g_array_new(FALSE, FALSE, sizeof(int));
    g_array_append_vals(a, items, len);
    return a;
}

int main(){
    int i[] = {10,10};
    GArray* batt = create_items(i, 2);
    check_debug(checkio(batt) == 0, "First");

    int i1[] = {10};
    batt = create_items(i1, 1);
    check_debug(checkio(batt) == 10, "Second");

    int i2[] = {5, 8, 13, 27, 14};
    batt = create_items(i2, 5);
    check_debug(checkio(batt) == 3, "Third");

    int i3[] = {5,5,6,5};
    batt = create_items(i3, 4);
    check_debug(checkio(batt) == 1, "Fourth");

    int i4[] = {12, 30, 30, 32, 42, 49};
    batt = create_items(i4, 6);
    check_debug(checkio(batt) == 9, "Fifth");

    g_array_free (batt, TRUE);
    g_printf("All ok\n");
    return 0;
    error:
        return 1;
}
