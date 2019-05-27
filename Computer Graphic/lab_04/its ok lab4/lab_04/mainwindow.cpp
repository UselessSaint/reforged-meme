#include "mainwindow.h"
#include "ui_mainwindow.h"

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

void MainWindow::paintEvent(QPaintEvent *)
{
    QPainter paint(this);

    paint.translate(360, 0);
    paint.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, QBrush(Qt::white));
    paint.setPen(Qt::gray);
    paint.drawLine(0, 0, 0, CANVAS_HEIGHT);
    paint.drawLine(0, 0, CANVAS_WIDTH, 0);
    paint.drawLine(CANVAS_WIDTH, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    paint.drawLine(0, CANVAS_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT);

    int n = points.length();
    for (int i = 0; i < n; ++i)
    {
        paint.setPen(QPen(colors[i]));
        if (q_points_a[i])
        {
            paint.drawEllipse(points[i], q_points_a[i], q_points_b[i]);
        }
        else
            paint.drawPoint(points[i]);
    }
}

// Set point

void MainWindow::set_point(int x, int y, Qt::GlobalColor color_value)
{
    points << QPoint(x, y);
    QColor color(color_value);
    colors << QColor(color);
    q_points_a << 0;
    q_points_b << 0;
}

// Draw circle/ellipse

void MainWindow::on_pushButton_draw_clicked()
{
    int color_index = ui->color->currentIndex();
    Qt::GlobalColor color;
    switch (color_index) {
    case 0:
        color = Qt::red;
        break;
    case 1:
        color = Qt::green;
        break;
    case 2:
        color = Qt::blue;
        break;
    case 3:
        color = Qt::white;
        break;
    }

    if (ui->circle->isChecked())
    {
        int cx = ui->spinBox_cx->value();
        int cy = ui->spinBox_cy->value();
        int r = ui->spinBox_r->value();
        int algorythm = ui->algorithm->currentIndex();
        switch (algorythm) {
        case 0:
            draw_circle_br(cx, cy, r, color);
            break;
        case 1:
            draw_circle_midpoint(cx, cy, r, color);
            break;
        case 2:
            draw_circle_canon(cx, cy, r, color);
            break;
        case 3:
            draw_circle_param(cx, cy, r, color);
            break;
        case 4:
            draw_circle_qt(cx, cy, r, color);
            break;
        }
    }
    else
    {
        int cx = ui->spinBox_cx->value();
        int cy = ui->spinBox_cy->value();
        int a = ui->spinBox_a->value();
        int b = ui->spinBox_b->value();
        int algorythm = ui->algorithm->currentIndex();
        switch (algorythm) {
        case 0:
            draw_ellipse_br(cx, cy, a, b, color);
            break;
        case 1:
            draw_ellipse_midpoint(cx, cy, a, b, color);
            break;
        case 2:
            draw_ellipse_canon(cx, cy, a, b, color);
            break;
        case 3:
            draw_ellipse_param(cx, cy, a, b, color);
            break;
        case 4:
            draw_ellipse_qt(cx, cy, a, b, color);
            break;
        }
    }
    repaint();
}

// Draw spectrum

void MainWindow::on_pushButton_spectrum_clicked()
{
    int color_index = ui->color->currentIndex();
    Qt::GlobalColor color;
    switch (color_index) {
    case 0:
        color = Qt::red;
        break;
    case 1:
        color = Qt::green;
        break;
    case 2:
        color = Qt::blue;
        break;
    case 3:
        color = Qt::white;
        break;
    }

    if (ui->circle->isChecked())
    {
        int cx = CANVAS_WIDTH / 2;
        int cy = CANVAS_HEIGHT / 2;
        int h = ui->spinBox_h->value();
        int n = ui->spinBox_n->value();
        int algorythm = ui->algorithm->currentIndex();
        int ir = ui->spinBox_r->value();
        for (int i = 0; i < n; ++i)
        {
            switch (algorythm) {
            case 0:
                draw_circle_br(cx, cy, ir, color);
                break;
            case 1:
                draw_circle_midpoint(cx, cy, ir, color);
                break;
            case 2:
                draw_circle_canon(cx, cy, ir, color);
                break;
            case 3:
                draw_circle_param(cx, cy, ir, color);
                break;
            case 4:
                draw_circle_qt(cx, cy, ir, color);
                break;
            }
            ir += h;
        }
    }
    else
    {
        int cx = CANVAS_WIDTH / 2;
        int cy = CANVAS_HEIGHT / 2;
        int h = ui->spinBox_h->value();
        int n = ui->spinBox_n->value();
        int algorythm = ui->algorithm->currentIndex();
        int ia = ui->spinBox_a->value(), ib = ui->spinBox_b->value();
        for (int i = 0; i < n; ++i)
        {
            switch (algorythm) {
            case 0:
                draw_ellipse_br(cx, cy, ia, ib, color);
                break;
            case 1:
                draw_ellipse_midpoint(cx, cy, ia, ib, color);
                break;
            case 2:
                draw_ellipse_canon(cx, cy, ia, ib, color);
                break;
            case 3:
                draw_ellipse_param(cx, cy, ia, ib, color);
                break;
            case 4:
                draw_ellipse_qt(cx, cy, ia, ib, color);
                break;
            }
            ia += h;
            ib += h;
        }
    }
    repaint();
}

// Circle

void MainWindow::draw_circle_br(int cx, int cy, int r, Qt::GlobalColor color)
{
    int x = 0;
    int y = r;
    int d = 2 * (1 - r);
    while (y >= 0)
    {
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);

        if (d < 0)
        {
            int dtmp = 2 * d + 2 * y - 1;
            if (dtmp < 0)
            {
                ++x;
                d = d + 2 * x + 1;
            }
            else
            {
                ++x;
                --y;
                d = d + 2 * (x - y + 1);
            }
        }
        else if (d == 0)
        {
            ++x;
            --y;
            d = d + 2 * (x - y + 1);
        }
        else
        {
            int dtmp = 2 * d - 2 * x - 1;
            if (dtmp < 0)
            {
                ++x;
                --y;
                d = d + 2 * (x - y + 1);
            }
            else
            {
                --y;
                d = d - 2 * y + 1;
            }
        }
    }
}

void MainWindow::draw_circle_midpoint(int cx, int cy, int r, Qt::GlobalColor color)
{
    int x = 0;
    int y = r;
    int d = 1 - r;
    do
    {
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);

        set_point(cx + y, cy + x, color);
        set_point(cx + y, cy - x, color);
        set_point(cx - y, cy + x, color);
        set_point(cx - y, cy - x, color);

        ++x;

        if (d < 0)
            d += 2 * x + 1;
        else
        {
            --y;
            d += 2 * (x - y) + 1;
        }
    }
    while(x <= y);
}

void MainWindow::draw_circle_canon(int cx, int cy, int r, Qt::GlobalColor color)
{
    int rr = r * r;
    for (int x = 0; x <= r; ++x)
    {
        int y = round(sqrt(rr - x * x));
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);

        set_point(cx + y, cy + x, color);
        set_point(cx + y, cy - x, color);
        set_point(cx - y, cy + x, color);
        set_point(cx - y, cy - x, color);
    }
}

void MainWindow::draw_circle_param(int cx, int cy, int r, Qt::GlobalColor color)
{
    double d = (double)1 / r;

    for (double i = M_PI_2l; i >= M_PI_4l; i -= d)
    {
        int x = round(r * cos(i));
        int y = round(r * sin(i));
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);

        set_point(cx + y, cy + x, color);
        set_point(cx + y, cy - x, color);
        set_point(cx - y, cy + x, color);
        set_point(cx - y, cy - x, color);
    }
}

void MainWindow::draw_circle_qt(int cx, int cy, int r, Qt::GlobalColor color)
{
    points << QPoint(cx, cy);
    colors << QColor(color);
    q_points_a << r;
    q_points_b << r;
}

// Ellipse

void MainWindow::draw_ellipse_br(int cx, int cy, int a, int b, Qt::GlobalColor color)
{
    int x = 0, y = b;
    int aa = a * a;
    int bb = b * b;
    int d = aa + bb - 2 * aa * y;
    while (y >= 0)
    {
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);

        if (d < 0) // разность квадр раст от центра до диаг пикселя и до идеального эллипса
        {
            int dtmp = 2 * d + 2 * aa * y - aa; // lг - lд
            ++x;
            if (dtmp < 0)
                d = d + 2 * bb * x + bb;
            else
            {
                --y;
                d = d + 2 * bb * x + bb + aa - 2 * aa * y;
            }
        }
        else if (d == 0)
        {
            ++x;
            --y;
            d = d + 2 * bb * x + bb + aa - 2 * aa * y;
        }
        else
        {
            int dtmp = 2 * d - 2 * bb * x - bb;
            --y;
            if (dtmp < 0)
            {
                ++x;
                d = d + 2 * bb * x + bb + aa - 2 * aa * y;
            }
            else
                d = d - 2 * aa * y + aa;
        }
    }
}

void MainWindow::draw_ellipse_midpoint(int cx, int cy, int a, int b, Qt::GlobalColor color)
{
    int x = 0;
    int y = b;
    int aa = a * a;
    int bb = b * b;
    int d = bb + aa * (y - 0.5) * (y - 0.5) - (long long)aa * bb;
    int p = aa / sqrt (bb + aa);

    while (x <= p)
    {
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);

        ++x;

        if (d > 0)
        {
            --y;
            d += aa * -2 * y;
        }
        d += bb * (2 * x + 1);
    }

    d += 0.75 * (aa - bb) - (bb * x + aa * y);
    while (y >= 0)
    {
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);

        --y;

        if (d < 0)
        {
            ++x;
            d += bb * (2 * x);
        }
        d += aa * (-2 * y + 1);
    }
}

void MainWindow::draw_ellipse_canon(int cx, int cy, int a, int b, Qt::GlobalColor color)
{
    int aa = a * a;
    int bb = b * b;
    double d = qRound(aa / sqrt(aa + bb));
    for (int x = 0; x <= d; ++x)
    {
        int y = round((double)b * sqrt(1.0 - (double)(x * x) / aa));
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);
    }
    d = qRound(bb / sqrt(aa + bb));
    for (int y = 0; y <= d; ++y)
    {
        int x = round((double)a * sqrt(1.0 - (double)(y * y) / bb));
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);
    }
}

void MainWindow::draw_ellipse_param(int cx, int cy, int a, int b, Qt::GlobalColor color)
{
    double m = (a > b) ? a : b;
    int l = round(M_PIl * m / 2);
    for (int i = 0; i <= l; ++i)
    {
        int x = round(a * cos((double)i / m));
        int y = round(b * sin((double)i / m));
        set_point(cx + x, cy + y, color);
        set_point(cx + x, cy - y, color);
        set_point(cx - x, cy + y, color);
        set_point(cx - x, cy - y, color);
    }
}

void MainWindow::draw_ellipse_qt(int cx, int cy, int a, int b, Qt::GlobalColor color)
{
    points << QPoint(cx, cy);
    colors << QColor(color);
    q_points_a << a;
    q_points_b << b;
}

// Clear

void MainWindow::on_pushButton_clear_clicked()
{
    points.clear();
    colors.clear();
    q_points_a.clear();
    q_points_b.clear();

    repaint();
}
