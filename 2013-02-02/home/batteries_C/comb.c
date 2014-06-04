#include "comb.h"
marker one = 1;
void comb(gint pool, gint need, marker chosen, gint at, GArray* combs)
{
	if (pool < need + at) return; /* not enough bits left */
 
	if (!need) {
		/* got all we needed; print the thing.  if other actions are
		 * desired, we could have passed in a callback function. */
        GArray *combl = g_array_new (FALSE, FALSE, sizeof (gint));
		for (at = 0; at < pool; at++){
			if (chosen & (one << at)){
                //printf("%d ", at);
                g_array_append_val(combl, at);
            }
        }
        g_array_append_val(combs, combl);
        //printf("\n");

		return;
	}
	/* if we choose the current item, "or" (|) the bit to mark it so. */
	comb(pool, need - 1, chosen | (one << at), at + 1, combs);
	comb(pool, need, chosen, at + 1, combs);  /* or don't choose it, go to next */
}

