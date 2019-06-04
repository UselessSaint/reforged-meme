#ifndef FILE_H
#define FILE_H

#include <cstdio>

#include "err.h"

err_t open_file(FILE **fd, const char *path, const char *mode);
void close_file(FILE *fd);

#endif // FILE_H
