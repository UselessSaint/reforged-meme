#ifndef DRAW_H
#define DRAW_H

#include <QPainter>

#include "command_type.h"
#include "model.h"

void draw_edges(points_t *points, edges_t *edges, const render_data_t *render_data);
void draw_edge(point_t p1, point_t p2, const render_data_t *render_data);

#endif // DRAW_H
