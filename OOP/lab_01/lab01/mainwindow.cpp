#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "command.h"
#include "err.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    command(QUIT, NULL);
    delete ui;
}

void MainWindow::paintEvent(QPaintEvent *)
{
    QPainter paint(this);

    paint.translate(320, 0);
    paint.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, QBrush(Qt::white));

    paint.setPen(Qt::lightGray);
    for (int i = 0; i <= CANVAS_WIDTH; i += 15){
        paint.drawLine(i, 0, i, CANVAS_HEIGHT);
    }
    for (int i = 0; i <= CANVAS_HEIGHT; i += 15){
        paint.drawLine(0, i, CANVAS_WIDTH, i);
    }
    paint.setPen(Qt::black);
    paint.drawLine(X0, 0, X0, CANVAS_HEIGHT);
    paint.drawLine(0, Y0, CANVAS_WIDTH, Y0);

    paint.setPen(QPen(Qt::red, 2));
    command_data_t cmd_data;
    cmd_data.render_data.paint = &paint;
    paint.translate(X0, Y0);
    command(RENDER, &cmd_data);
}

void MainWindow::on_pushButton_load_clicked()
{
    command_data_t cmd_data;
    QString lineEdit = ui->lineEdit_load->text();
    QByteArray ba = lineEdit.toLocal8Bit();
    const char *path = ba.data();
    cmd_data.load_data.load_path = path;

    err_t err;
    err = command(LOAD, &cmd_data);

    if (err == FILE_OPEN_ERR)
        QMessageBox::critical(this, "Ошибка!", "Невозможно открыть файл.");
    else if (err == INCORRECT_INPUT_ERR)
        QMessageBox::critical(this, "Ошибка!", "Некорректный ввод из файла.");
    else
    {
        QMessageBox::information(this, "Загрузка", "Модель успешно загружена.");
        repaint();
    }
}

void MainWindow::on_pushButton_save_clicked()
{
    command_data_t cmd_data;
    QString lineEdit = ui->lineEdit_save->text();
    QByteArray ba = lineEdit.toLocal8Bit();
    const char *path = ba.data();
    cmd_data.save_data.save_path = path;

    err_t err;
    err = command(SAVE, &cmd_data);

    if (err == FILE_OPEN_ERR)
        QMessageBox::critical(this, "Ошибка!", "Невозможно открыть файл для записи.");
    else if (err == NOT_LOAD_YET_ERR)
        QMessageBox::critical(this, "Ошибка!", "Невозможно сохранить пустую модель.");
    else
        QMessageBox::information(this, "Сохранение", "Файл с моделью успешно сохранен.");
}

void MainWindow::on_pushButton_translation_clicked()
{
    bool ok;

    double dx = ui->lineEdit_dx->text().toDouble(&ok);
    if (!ok)
    {
        QMessageBox::critical(this, "Ошибка!", "Некорректный ввод. Повторите попытку.");
        return;
    }
    double dy = ui->lineEdit_dy->text().toDouble(&ok);
    if (!ok)
    {
        QMessageBox::critical(this, "Ошибка!", "Некорректный ввод. Повторите попытку.");
        return;
    }
    double dz = ui->lineEdit_dz->text().toDouble(&ok);
    if (!ok)
    {
        QMessageBox::critical(this, "Ошибка!", "Некорректный ввод. Повторите попытку.");
        return;
    }

    command_data_t cmd_data;
    cmd_data.transform_data.transform_type = TRANSLATION;
    cmd_data.transform_data.translation.dx = dx;
    cmd_data.transform_data.translation.dy = dy;
    cmd_data.transform_data.translation.dz = dz;
    command(TRANSFORM, &cmd_data);

    repaint();
}

void MainWindow::on_pushButton_rotate_clicked()
{
    bool ok;

    double angle = ui->lineEdit_angle->text().toDouble(&ok);
    if (!ok)
    {
        QMessageBox::critical(this, "Ошибка!", "Некорректный ввод. Повторите попытку.");
        return;
    }
    QString cur = ui->comboBox->currentText();
    QByteArray ba = cur.toLocal8Bit();
    const char *axis = ba.data();

    command_data_t cmd_data;
    cmd_data.transform_data.transform_type = ROTATION;
    cmd_data.transform_data.rotation.angel = angle;
    switch (axis[1]) {
    case 'X':
        cmd_data.transform_data.rotation.axis = X;
        break;
    case 'Y':
        cmd_data.transform_data.rotation.axis = Y;
        break;
    case 'Z':
        cmd_data.transform_data.rotation.axis = Z;
        break;
    }
    command(TRANSFORM, &cmd_data);

    repaint();
}

void MainWindow::on_pushButton_clicked()
{
    bool ok;
    double scale = ui->lineEdit_scale->text().toDouble(&ok);
    if (!ok)
    {
        QMessageBox::critical(this, "Ошибка!", "Некорректный ввод. Повторите попытку.");
        return;
    }

    command_data_t cmd_data;
    cmd_data.transform_data.transform_type = SCALING;
    cmd_data.transform_data.scaling.scale = scale;
    command(TRANSFORM, &cmd_data);

    repaint();
}
