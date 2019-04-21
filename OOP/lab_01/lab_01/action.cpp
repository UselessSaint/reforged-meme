#include "action.h"
#include "model.h"

void do_action(command cmd, const union input_data &inp_data)
{
	static model current_model;

	switch (cmd)
	{
	case LOAD:
		load(current_model, inp_data.input_model);
	}
}
/*
void load(model &curr_model, model inp_model)
{

}
*/
