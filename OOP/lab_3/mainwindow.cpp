#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QObject::connect(&lift, SIGNAL(change_note_text(QString)), this, SLOT(set_note_text(QString)));
    QObject::connect(this, SIGNAL(change_note_text(QString)), this, SLOT(set_note_text(QString)));

    emit change_note_text("Лифт находится в режиме ожидания.");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::set_note_text(QString text)
{
    ui->label->setText(text);
}

void MainWindow::on_button_cabin_1_clicked()
{
    emit change_note_text("В лифте нажали кнопку 1.");
    lift.add_call(1);
}

void MainWindow::on_button_cabin_2_clicked()
{
    emit change_note_text("В лифте нажали кнопку 2.");
    lift.add_call(2);
}

void MainWindow::on_button_cabin_3_clicked()
{
    emit change_note_text("В лифте нажали кнопку 3.");
    lift.add_call(3);
}

void MainWindow::on_button_cabin_4_clicked()
{
    emit change_note_text("В лифте нажали кнопку 4.");
    lift.add_call(4);
}

void MainWindow::on_button_cabin_5_clicked()
{
    emit change_note_text("В лифте нажали кнопку 5.");
    lift.add_call(5);
}

void MainWindow::on_button_cabin_6_clicked()
{
    emit change_note_text("В лифте нажали кнопку 6.");
    lift.add_call(6);
}

void MainWindow::on_button_cabin_7_clicked()
{
    emit change_note_text("В лифте нажали кнопку 7.");
    lift.add_call(7);
}

void MainWindow::on_button_cabin_8_clicked()
{
    emit change_note_text("В лифте нажали кнопку 8.");
    lift.add_call(8);
}

void MainWindow::on_button_cabin_9_clicked()
{
    emit change_note_text("В лифте нажали кнопку 9.");
    lift.add_call(9);
}

void MainWindow::on_button_cabin_10_clicked()
{
    emit change_note_text("В лифте нажали кнопку 10.");
    lift.add_call(10);
}

void MainWindow::on_button_floor_1_clicked()
{
    emit change_note_text("На 1 этаже был вызван лифт.");
    lift.add_call(1);
}

void MainWindow::on_button_floor_2_clicked()
{
    emit change_note_text("На 2 этаже был вызван лифт.");
    lift.add_call(2);
}

void MainWindow::on_button_floor_3_clicked()
{
    emit change_note_text("На 3 этаже был вызван лифт.");
    lift.add_call(3);
}

void MainWindow::on_button_floor_4_clicked()
{
    emit change_note_text("На 4 этаже был вызван лифт.");
    lift.add_call(4);
}

void MainWindow::on_button_floor_5_clicked()
{
    emit change_note_text("На 5 этаже был вызван лифт.");
    lift.add_call(5);
}

void MainWindow::on_button_floor_6_clicked()
{
    emit change_note_text("На 6 этаже был вызван лифт.");
    lift.add_call(6);
}

void MainWindow::on_button_floor_7_clicked()
{
    emit change_note_text("На 7 этаже был вызван лифт.");
    lift.add_call(7);
}

void MainWindow::on_button_floor_8_clicked()
{
    emit change_note_text("На 8 этаже был вызван лифт.");
    lift.add_call(8);
}

void MainWindow::on_button_floor_9_clicked()
{
    emit change_note_text("На 9 этаже был вызван лифт.");
    lift.add_call(9);
}

void MainWindow::on_button_floor_10_clicked()
{
    emit change_note_text("На 10 этаже был вызван лифт.");
    lift.add_call(10);
}

