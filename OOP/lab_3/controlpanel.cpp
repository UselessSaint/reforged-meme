#include "controlpanel.h"

Control_panel::Control_panel(QObject *parent) : QObject(parent)
{
    current_state = FREE;
    cur_direction = STAY;
    cur_floor = 0;

    for (int i = 0; i < NUM_FLOORS; i++)
        calls[i] = false;
}

void Control_panel::set_new_target(int floor)
{
    current_state = BUSY;
    calls[floor - 1] = true;
    next_target(floor);
    emit set_target(floor);
}

void Control_panel::achieved_floor(int floor)
{
    if (current_state == BUSY)
    {
        cur_floor = floor;
        cur_direction = STAY;
        calls[floor - 1] = false;

        if (next_target(floor))
        {
            emit set_target(floor);
        }
        else
        {
            current_state = FREE;
        }
    }
}

void Control_panel::passed_floor(int floor)
{
    emit change_note_text("Лифт преодолел " + QString::number(floor) + " этаж.");
}

bool Control_panel::next_target(int &floor)
{
    int step = -1;
    if (cur_direction == UP)
    {
        step = 1;
    }
    for (int i = cur_floor; i <= NUM_FLOORS && i > 0; i += step)
    {
        if (calls[i - 1])
        {
            floor = i;
            return true;
        }
    }
    step = -step;
    for (int i = cur_floor; i <= NUM_FLOORS && i > 0; i += step)
    {
        if (calls[i - 1])
        {
            floor = i;
            return true;
        }
    }
    return false;
}
