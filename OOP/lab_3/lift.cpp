#include "lift.h"

Lift::Lift()
{
    // передача цели кабине
    QObject::connect(&control_panel, SIGNAL(set_target(int)), &lift_cabin, SLOT(cabin_set_target(int)));
    QObject::connect(&lift_cabin, SIGNAL(crossing_floor(int, direction)), &control_panel, SLOT(passed_floor(int)));
    QObject::connect(&lift_cabin, SIGNAL(cabin_stopped(int)), &control_panel, SLOT(achieved_floor(int)));

    QObject::connect(&control_panel, SIGNAL(change_note_text(QString)), this, SIGNAL(change_note_text(QString)));
    QObject::connect(&lift_cabin, SIGNAL(change_note_text(QString)), this, SIGNAL(change_note_text(QString)));
}

// получание сигнала от кнопки
void Lift::add_call(int floor)
{
    control_panel.set_new_target(floor);
}

