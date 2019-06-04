#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QVector>
#include <QPainter>
#include <QMessageBox>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_pushButton_load_clicked();
    void on_pushButton_save_clicked();
    void on_pushButton_translation_clicked();
    void on_pushButton_rotate_clicked();
    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;

    void paintEvent(QPaintEvent *event);

    const int CELLS_IN_ROW = 69;
    const int CELLS_IN_COLUMN = 43;
    const int CANVAS_WIDTH = CELLS_IN_ROW * 15;
    const int CANVAS_HEIGHT = CELLS_IN_COLUMN * 15;
    const int X0 = CELLS_IN_ROW / 2 * 15;
    const int Y0 = CELLS_IN_COLUMN / 2 * 15;
};

#endif // MAINWINDOW_H
