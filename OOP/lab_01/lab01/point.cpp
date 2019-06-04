#include "point.h"

err_t get_point(point_t *point, FILE *fd)
{
    err_t err;
    err = fget_double(&point->x, fd);
    if (err == NONE_ERR)
        err = fget_double(&point->y, fd);
    if (err == NONE_ERR)
        err = fget_double(&point->z, fd);
    return err;
}

void translate_point(point_t *p, translation_t data)
{
    p->x += data.dx;
    p->y += data.dy;
    p->z += data.dz;
}

void rotate_point(point_t *p, rotation_t data)
{
    axis_t axis = data.axis;
    double angle = data.angel * M_PI / 180;
    double cos_angle = cos(angle);
    double sin_angle = sin(angle);
    double x = p->x;
    double y = p->y;
    double z = p->z;

    switch (axis)
    {
        case X:
            p->y = y * cos_angle - z * sin_angle;
            p->z = y * sin_angle + z * cos_angle;
            break;
        case Y:
            p->x = x * cos_angle + z * sin_angle;
            p->z = z * cos_angle - x * sin_angle;
            break;
        case Z:
            p->x = x * cos_angle - y * sin_angle;
            p->y = x * sin_angle + y * cos_angle;
            break;
    }
}

void scale_point(point_t *p, scaling_t data)
{
    p->x *= data.scale;
    p->y *= data.scale;
    p->z *= data.scale;
}

int put_point(point_t *point, FILE *fd)
{
    return fprintf(fd, "%lf %lf %lf\n", point->x, point->y, point->z);
}
