#include "edges.h"

edges_t init_edges()
{
    return {NULL, 0};
}

err_t alloc_edges(edges_t *edges, int n)
{
    err_t err = NONE_ERR;
    edges->edges_arr = (edge_t *)malloc(n * sizeof(edge_t));
    if (edges->edges_arr == NULL)
    {
        err = MEMORY_ALLOC_ERR;
        edges->n = 0;
    }
    else
        edges->n = n;
    return err;
}

void free_edges(edges_t *edges)
{
    free(edges->edges_arr);
    edges->edges_arr = NULL;
    edges->n = 0;
}

bool is_alloc_edges(edges_t *edges)
{
    return edges->edges_arr;
}

err_t get_edges(edges_t *edges, FILE *fd)
{
    err_t err = NONE_ERR;
    int n = edges->n;
    for (int i = 0; i < n && err == NONE_ERR; ++i)
        err = get_edge(&edges->edges_arr[i], fd);
    return err;
}

err_t copy_edges(edges_t *edges, edges_t *copied_edges)
{
    if (!edges->edges_arr || !copied_edges->edges_arr ||
        !edges->n || !copied_edges->n ||
        edges->n != copied_edges->n)
        return COPY_ERR;

    int n = edges->n;
    for (int i = 0; i < n; ++i)
        edges->edges_arr[i] = copied_edges->edges_arr[i];
    return NONE_ERR;
}

err_t get_edges_count(int *count, edges_t *edges)
{
    if (!is_alloc_edges(edges))
        return NOT_ALLOC_YET_ERR;
    *count = edges->n;
    return NONE_ERR;
}

int put_edges(edges_t *edges, FILE *fd)
{
    if (!is_alloc_edges(edges))
        return NOT_ALLOC_YET_ERR;
    int count = 0;
    int n = edges->n;
    for (int i = 0; i < n; ++i)
        count += put_edge(&edges->edges_arr[i], fd);
    return count;
}
