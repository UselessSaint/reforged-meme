#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPainter>
#include <QMessageBox>
#include <QWidget>

#include <cmath>

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
    void on_pushButton_draw_clicked();

    void on_pushButton_clear_clicked();

    void on_pushButton_spectrum_clicked();

private:
    Ui::MainWindow *ui;

    template<typename T>
    int sgn(T x){ if (x > 0) return 1; if (x < 0) return -1; return 0; }

    void paintEvent(QPaintEvent *event);
    void set_point(int x, int y, Qt::GlobalColor color_value);

    void draw_circle_br(int cx, int cy, int r, Qt::GlobalColor color);
    void draw_circle_midpoint(int cx, int cy, int r, Qt::GlobalColor color);
    void draw_circle_canon(int cx, int cy, int r, Qt::GlobalColor color);
    void draw_circle_param(int cx, int cy, int r, Qt::GlobalColor color);
    void draw_circle_qt(int cx, int cy, int r, Qt::GlobalColor color);

    void draw_ellipse_br(int cx, int cy, int a, int b, Qt::GlobalColor color);
    void draw_ellipse_midpoint(int cx, int cy, int a, int b, Qt::GlobalColor color);
    void draw_ellipse_canon(int cx, int cy, int a, int b, Qt::GlobalColor color);
    void draw_ellipse_param(int cx, int cy, int a, int b, Qt::GlobalColor color);
    void draw_ellipse_qt(int cx, int cy, int a, int b, Qt::GlobalColor color);

    const int CANVAS_WIDTH = 1000;
    const int CANVAS_HEIGHT = 650;

    const int X0 = CANVAS_WIDTH / 2;
    const int Y0 = CANVAS_HEIGHT / 2;

    QVector<QPoint> points;
    QVector<QColor> colors;
    QVector<int> q_points_a;
    QVector<int> q_points_b;
};

#endif // MAINWINDOW_H
