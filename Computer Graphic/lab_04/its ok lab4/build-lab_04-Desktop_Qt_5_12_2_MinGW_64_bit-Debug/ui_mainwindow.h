/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QComboBox *algorithm;
    QSpinBox *spinBox_cx;
    QSpacerItem *verticalSpacer_3;
    QSpacerItem *verticalSpacer_8;
    QLabel *label_9;
    QLabel *label_2;
    QLabel *label_4;
    QSpinBox *spinBox_a;
    QFrame *line_2;
    QLabel *label_3;
    QSpinBox *spinBox_r;
    QFrame *line_4;
    QSpacerItem *verticalSpacer_6;
    QRadioButton *circle;
    QLabel *label_10;
    QPushButton *pushButton_clear;
    QSpinBox *spinBox_n;
    QComboBox *color;
    QLabel *label_8;
    QSpacerItem *verticalSpacer_7;
    QLabel *label;
    QSpinBox *spinBox_h;
    QFrame *line;
    QSpacerItem *verticalSpacer_4;
    QLabel *label_11;
    QSpinBox *spinBox_cy;
    QSpacerItem *verticalSpacer_5;
    QPushButton *pushButton_draw;
    QSpinBox *spinBox_b;
    QSpacerItem *verticalSpacer;
    QRadioButton *ellipse;
    QPushButton *pushButton_spectrum;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1366, 656);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(10, 10, 341, 501));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        algorithm = new QComboBox(gridLayoutWidget);
        algorithm->addItem(QString());
        algorithm->addItem(QString());
        algorithm->addItem(QString());
        algorithm->addItem(QString());
        algorithm->addItem(QString());
        algorithm->setObjectName(QString::fromUtf8("algorithm"));

        gridLayout->addWidget(algorithm, 1, 0, 1, 2);

        spinBox_cx = new QSpinBox(gridLayoutWidget);
        spinBox_cx->setObjectName(QString::fromUtf8("spinBox_cx"));
        spinBox_cx->setMaximum(1000);
        spinBox_cx->setValue(500);

        gridLayout->addWidget(spinBox_cx, 6, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 7, 0, 2, 2);

        verticalSpacer_8 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_8, 18, 0, 1, 2);

        label_9 = new QLabel(gridLayoutWidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout->addWidget(label_9, 12, 1, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 10, 0, 1, 1);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 0, 0, 1, 2);

        spinBox_a = new QSpinBox(gridLayoutWidget);
        spinBox_a->setObjectName(QString::fromUtf8("spinBox_a"));
        spinBox_a->setMaximum(650);
        spinBox_a->setValue(100);

        gridLayout->addWidget(spinBox_a, 11, 1, 1, 1);

        line_2 = new QFrame(gridLayoutWidget);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        gridLayout->addWidget(line_2, 23, 0, 1, 2);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 14, 0, 1, 1);

        spinBox_r = new QSpinBox(gridLayoutWidget);
        spinBox_r->setObjectName(QString::fromUtf8("spinBox_r"));
        spinBox_r->setMaximum(1000);
        spinBox_r->setValue(100);

        gridLayout->addWidget(spinBox_r, 11, 0, 1, 1);

        line_4 = new QFrame(gridLayoutWidget);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);

        gridLayout->addWidget(line_4, 17, 0, 1, 2);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_6, 2, 0, 1, 2);

        circle = new QRadioButton(gridLayoutWidget);
        circle->setObjectName(QString::fromUtf8("circle"));
        circle->setChecked(true);

        gridLayout->addWidget(circle, 9, 0, 1, 1);

        label_10 = new QLabel(gridLayoutWidget);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        gridLayout->addWidget(label_10, 19, 0, 1, 1);

        pushButton_clear = new QPushButton(gridLayoutWidget);
        pushButton_clear->setObjectName(QString::fromUtf8("pushButton_clear"));

        gridLayout->addWidget(pushButton_clear, 25, 0, 1, 2);

        spinBox_n = new QSpinBox(gridLayoutWidget);
        spinBox_n->setObjectName(QString::fromUtf8("spinBox_n"));
        spinBox_n->setMaximum(650);
        spinBox_n->setValue(10);

        gridLayout->addWidget(spinBox_n, 20, 1, 1, 1);

        color = new QComboBox(gridLayoutWidget);
        color->addItem(QString());
        color->addItem(QString());
        color->addItem(QString());
        color->addItem(QString());
        color->setObjectName(QString::fromUtf8("color"));

        gridLayout->addWidget(color, 15, 0, 1, 1);

        label_8 = new QLabel(gridLayoutWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout->addWidget(label_8, 10, 1, 1, 1);

        verticalSpacer_7 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_7, 22, 0, 1, 2);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 5, 0, 1, 2);

        spinBox_h = new QSpinBox(gridLayoutWidget);
        spinBox_h->setObjectName(QString::fromUtf8("spinBox_h"));
        spinBox_h->setMaximum(650);
        spinBox_h->setValue(20);

        gridLayout->addWidget(spinBox_h, 20, 0, 1, 1);

        line = new QFrame(gridLayoutWidget);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout->addWidget(line, 3, 0, 1, 2);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_4, 16, 0, 1, 2);

        label_11 = new QLabel(gridLayoutWidget);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        gridLayout->addWidget(label_11, 19, 1, 1, 1);

        spinBox_cy = new QSpinBox(gridLayoutWidget);
        spinBox_cy->setObjectName(QString::fromUtf8("spinBox_cy"));
        spinBox_cy->setMaximum(650);
        spinBox_cy->setValue(325);

        gridLayout->addWidget(spinBox_cy, 6, 1, 1, 1);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_5, 4, 0, 1, 2);

        pushButton_draw = new QPushButton(gridLayoutWidget);
        pushButton_draw->setObjectName(QString::fromUtf8("pushButton_draw"));

        gridLayout->addWidget(pushButton_draw, 15, 1, 1, 1);

        spinBox_b = new QSpinBox(gridLayoutWidget);
        spinBox_b->setObjectName(QString::fromUtf8("spinBox_b"));
        spinBox_b->setMaximum(650);
        spinBox_b->setValue(50);

        gridLayout->addWidget(spinBox_b, 13, 1, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 24, 0, 1, 2);

        ellipse = new QRadioButton(gridLayoutWidget);
        ellipse->setObjectName(QString::fromUtf8("ellipse"));

        gridLayout->addWidget(ellipse, 9, 1, 1, 1);

        pushButton_spectrum = new QPushButton(gridLayoutWidget);
        pushButton_spectrum->setObjectName(QString::fromUtf8("pushButton_spectrum"));

        gridLayout->addWidget(pushButton_spectrum, 21, 0, 1, 2);

        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "\320\220\320\273\320\263\320\276\321\200\320\270\321\202\320\274\321\213 \320\277\320\276\321\201\321\202\321\200\320\276\320\265\320\275\320\270\321\217 \320\276\320\272\321\200\321\203\320\266\320\275\320\276\321\201\321\202\320\265\320\271 \320\270 \321\215\320\273\320\273\320\270\320\277\321\201\320\276\320\262", nullptr));
        algorithm->setItemText(0, QApplication::translate("MainWindow", "\320\221\321\200\320\265\320\267\320\265\320\275\321\205\320\265\320\274", nullptr));
        algorithm->setItemText(1, QApplication::translate("MainWindow", "\320\241\321\200\320\265\320\264\320\275\321\217\321\217 \321\202\320\276\321\207\320\272\320\260", nullptr));
        algorithm->setItemText(2, QApplication::translate("MainWindow", "\320\232\320\260\320\275\320\276\320\275\320\270\321\207\320\265\321\201\320\272\320\276\320\265 \321\203\321\200\320\260\320\262\320\275\320\265\320\275\320\270\320\265", nullptr));
        algorithm->setItemText(3, QApplication::translate("MainWindow", "\320\237\320\260\321\200\320\260\320\274\320\265\321\202\321\200\320\270\321\207\320\265\321\201\320\272\320\276\320\265 \321\203\321\200\320\260\320\262\320\275\320\265\320\275\320\270\320\265", nullptr));
        algorithm->setItemText(4, QApplication::translate("MainWindow", "\320\220\320\273\320\263\320\276\321\200\320\270\321\202\320\274 \320\270\320\267 \320\261\320\270\320\261\320\273\320\270\320\276\321\202\320\265\320\272\320\270", nullptr));

        label_9->setText(QApplication::translate("MainWindow", "B", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "R", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "\320\222\321\213\320\261\320\276\321\200 \320\260\320\273\320\263\320\276\321\200\320\270\321\202\320\274\320\260", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "\320\246\320\262\320\265\321\202", nullptr));
        circle->setText(QApplication::translate("MainWindow", "\320\236\320\272\321\200\321\203\320\266\320\275\320\276\321\201\321\202\321\214", nullptr));
        label_10->setText(QApplication::translate("MainWindow", "\320\250\320\260\320\263", nullptr));
        pushButton_clear->setText(QApplication::translate("MainWindow", "\320\236\321\207\320\270\321\201\321\202\320\270\321\202\321\214 \321\205\320\276\320\273\321\201\321\202", nullptr));
        color->setItemText(0, QApplication::translate("MainWindow", "\320\232\321\200\320\260\321\201\320\275\321\213\320\271", nullptr));
        color->setItemText(1, QApplication::translate("MainWindow", "\320\227\320\265\320\273\320\265\320\275\321\213\320\271", nullptr));
        color->setItemText(2, QApplication::translate("MainWindow", "\320\241\320\270\320\275\320\270\320\271", nullptr));
        color->setItemText(3, QApplication::translate("MainWindow", "\320\246\320\262\320\265\321\202 \321\204\320\276\320\275\320\260", nullptr));

        label_8->setText(QApplication::translate("MainWindow", "A", nullptr));
        label->setText(QApplication::translate("MainWindow", "\320\246\320\265\320\275\321\202\321\200", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "\320\232\320\276\320\273\320\270\321\207\320\265\321\201\321\202\320\262\320\276", nullptr));
        pushButton_draw->setText(QApplication::translate("MainWindow", "\320\237\320\276\321\201\321\202\321\200\320\276\320\270\321\202\321\214", nullptr));
        ellipse->setText(QApplication::translate("MainWindow", "\320\255\320\273\320\273\320\270\320\277\321\201", nullptr));
        pushButton_spectrum->setText(QApplication::translate("MainWindow", "\320\237\320\276\321\201\321\202\321\200\320\276\320\270\321\202\321\214 \321\201\320\277\320\265\320\272\321\202\321\200", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
