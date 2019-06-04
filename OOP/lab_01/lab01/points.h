#ifndef POINTS_H
#define POINTS_H

#include <cstdio>
#include <cstdlib>
#include <cmath>

#include "err.h"
#include "io.h"

#include "point.h"

typedef struct {
    point_t *points_arr;
    int n;
} points_t;

points_t init_points();
err_t alloc_points(points_t *points, int n);
void free_points(points_t *points);
bool is_alloc_points(points_t *points);

err_t get_points(points_t *points, FILE *fd);
err_t copy_points(points_t *points, points_t *copied_points);
err_t get_points_count(int *count, points_t *points);
err_t translate_points(points_t *points, translation_t data);
err_t rotate_points(points_t *points, rotation_t data);
err_t scale_points(points_t *points, scaling_t data);
int put_points(points_t *points, FILE *fd);

#endif // POINTS_H
