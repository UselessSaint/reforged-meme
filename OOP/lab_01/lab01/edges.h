#ifndef EDGES_H
#define EDGES_H

#include "edge.h"

typedef struct {
    edge_t *edges_arr;
    int n;
} edges_t;

edges_t init_edges();
err_t alloc_edges(edges_t *edges, int n);
void free_edges(edges_t *edges);
bool is_alloc_edges(edges_t *edges);

err_t get_edges(edges_t *edges, FILE *fd);
err_t copy_edges(edges_t *edges, edges_t *copied_edges);
int put_edges(edges_t *edges, FILE *fd);
err_t get_edges_count(int *count, edges_t *edges);


#endif // EDGES_H
