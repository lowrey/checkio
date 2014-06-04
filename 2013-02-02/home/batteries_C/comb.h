#ifndef __comb_h__
#define __comb_h__
#include <stdio.h>
#include <glib.h>
typedef unsigned long marker;
void comb(gint pool, gint need, marker chosen, gint at, GArray* combs);
#endif
