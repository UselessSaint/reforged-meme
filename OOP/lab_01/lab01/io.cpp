#include "io.h"

err_t fget_int(int *value, FILE *fd)
{
    err_t err = NONE_ERR;
    if (fscanf(fd, "%d", value) != 1)
        err = INCORRECT_INPUT_ERR;
    return err;
}

err_t fget_double(double *value, FILE *fd)
{
    err_t err = NONE_ERR;
    if (fscanf(fd, "%lf", value) != 1)
        err = INCORRECT_INPUT_ERR;
    return err;
}
