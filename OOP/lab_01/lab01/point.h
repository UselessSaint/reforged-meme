#ifndef POINT_H
#define POINT_H

#include <cstdio>
#include <cstdlib>
#include <cmath>

#include "err.h"
#include "transform_type.h"
#include "io.h"

typedef struct {
    double x;
    double y;
    double z;
} point_t;

err_t get_point(point_t *point, FILE *fd);
void translate_point(point_t *p, translation_t data);
void rotate_point(point_t *p, rotation_t data);
void scale_point(point_t *p, scaling_t data);
int put_point(point_t *point, FILE *fd);

#endif // POINT_H
