CC=gcc
CFLAGS = `pkg-config --cflags glib-2.0` -Wall -g
LDFLAGS= `pkg-config --libs glib-2.0`
all: batteries

batteries: comb.o garray_util.o batteries.o
	gcc -o $@ $^ $(CFLAGS) $(LDFLAGS)  

clean: FRC
	rm batteries *.o

# This is an explicit suffix rule. It may be omitted on systems
# that handle simple rules like this automatically.
.c.o:
	$(CC) $(CFLAGS) -c $<

FRC:
.SUFFIXES: .c
