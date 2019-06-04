#include "points.h"

points_t init_points()
{
    return {NULL, 0};
}

err_t alloc_points(points_t *points, int n)
{
    err_t err = NONE_ERR;
    points->points_arr = (point_t *)malloc(n * sizeof(point_t));
    if (points->points_arr == NULL)
    {
        err = MEMORY_ALLOC_ERR;
        points->n = 0;
    }
    else
        points->n = n;
    return err;
}

void free_points(points_t *points)
{
    free(points->points_arr);
    points->points_arr = NULL;
    points->n = 0;
}

bool is_alloc_points(points_t *points)
{
    return points->points_arr;
}

err_t get_points(points_t *points, FILE *fd)
{
    err_t err = NONE_ERR;
    int n = points->n;
    for (int i = 0; i < n && err == NONE_ERR; ++i)
        err = get_point(&points->points_arr[i], fd);
    return err;
}

err_t copy_points(points_t *points, points_t *copied_points)
{
    if (!points->points_arr || !copied_points->points_arr ||
        !points->n || !copied_points->n ||
        points->n != copied_points->n)
        return COPY_ERR;

    int n = points->n;
    for (int i = 0; i < n; ++i)
        points->points_arr[i] = copied_points->points_arr[i];
    return NONE_ERR;
}

err_t get_points_count(int *count, points_t *points)
{
    if (!is_alloc_points(points))
        return NOT_ALLOC_YET_ERR;
    *count = points->n;
    return NONE_ERR;
}

err_t translate_points(points_t *points, translation_t data)
{
    if (!is_alloc_points(points))
        return NOT_ALLOC_YET_ERR;

    int n = points->n;
    for (int i = 0; i < n; ++i)
        translate_point(&points->points_arr[i], data);

    return NONE_ERR;
}

err_t rotate_points(points_t *points, rotation_t data)
{
    if (!is_alloc_points(points))
        return NOT_ALLOC_YET_ERR;

    int n = points->n;
    for (int i = 0; i < n; ++i)
        rotate_point(&points->points_arr[i], data);

    return NONE_ERR;
}

err_t scale_points(points_t *points, scaling_t data)
{
    if (!is_alloc_points(points))
        return NOT_ALLOC_YET_ERR;

    int n = points->n;
    for (int i = 0; i < n; ++i)
        scale_point(&points->points_arr[i], data);

    return NONE_ERR;
}

int put_points(points_t *points, FILE *fd)
{
    if (!is_alloc_points(points))
        return NOT_ALLOC_YET_ERR;
    int count = 0;
    int n = points->n;
    for (int i = 0; i < n; ++i)
        count += put_point(&points->points_arr[i], fd);
    return count;
}
