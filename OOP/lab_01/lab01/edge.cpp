#include "edge.h"

err_t get_edge(edge_t *edge, FILE *fd)
{
    err_t err;
    err = fget_int(&edge->p1, fd);
    if (err == NONE_ERR)
        err = fget_int(&edge->p2, fd);
    return err;
}

int put_edge(edge_t *edge, FILE *fd)
{
    return fprintf(fd, "%d %d\n", edge->p1, edge->p2);
}
