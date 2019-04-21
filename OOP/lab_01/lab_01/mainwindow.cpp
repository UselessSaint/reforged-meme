#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_load_button_clicked()
{
	QString file_name;
	const char *cfile_name;

	file_name = QFileDialog::getOpenFileName(this, tr("Open File"),
											 "");
	cfile_name = qPrintable(file_name);


}
