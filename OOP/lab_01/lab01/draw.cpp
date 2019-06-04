#include "draw.h"

void draw_edges(points_t *points, edges_t *edges, const render_data_t *render_data)
{
    int n = edges->n;
    for (int i = 0; i < n; ++i)
        draw_edge(points->points_arr[edges->edges_arr[i].p1],
                  points->points_arr[edges->edges_arr[i].p2],
                  render_data);
}

void draw_edge(point_t p1, point_t p2, const render_data_t *render_data)
{
    QPainter *paint = render_data->paint;
    paint->drawLine(p1.x * 15, -p1.y * 15,
                    p2.x * 15, -p2.y * 15);
}
