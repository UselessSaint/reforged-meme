#ifndef MODEL_H
#define MODEL_H

#include "line.h"

typedef struct model model;

struct model
{
	line *edges;
	int amount_of_edges;
};

#endif // MODEL_H
