#ifndef IO_H
#define IO_H

#include <cstdio>

#include "err.h"

err_t fget_int(int *value, FILE *fd);
err_t fget_double(double *value, FILE *fd);

#endif // IO_H
