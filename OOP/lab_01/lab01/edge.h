#ifndef EDGE_H
#define EDGE_H

#include <cstdio>
#include <cstdlib>

#include "err.h"
#include "transform_type.h"
#include "io.h"

typedef struct {
    int p1;
    int p2;
} edge_t;

err_t get_edge(edge_t *edge, FILE *fd);
int put_edge(edge_t *edge, FILE *fd);

#endif // EDGE_H
