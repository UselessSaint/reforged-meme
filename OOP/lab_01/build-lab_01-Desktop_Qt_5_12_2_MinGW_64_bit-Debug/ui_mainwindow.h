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
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QHBoxLayout *horizontalLayout;
    QWidget *widget_2;
    QVBoxLayout *verticalLayout;
    QWidget *widget_6;
    QGridLayout *gridLayout_4;
    QLabel *label_7;
    QLabel *label_9;
    QLabel *label_8;
    QDoubleSpinBox *move_x;
    QPushButton *move_button;
    QDoubleSpinBox *move_y;
    QDoubleSpinBox *move_z;
    QWidget *rotate_container;
    QGridLayout *gridLayout_3;
    QLabel *label_6;
    QLabel *label_5;
    QDoubleSpinBox *rotate_x;
    QLabel *label_4;
    QPushButton *rotate_button;
    QDoubleSpinBox *rotate_y;
    QDoubleSpinBox *rotate_z;
    QWidget *scale_container;
    QGridLayout *gridLayout_2;
    QLabel *label;
    QDoubleSpinBox *scale_x;
    QLabel *label_3;
    QDoubleSpinBox *scale_y;
    QPushButton *scale_button;
    QDoubleSpinBox *scale_z;
    QLabel *label_2;
    QWidget *save_load_container;
    QVBoxLayout *verticalLayout_2;
    QPushButton *load_button;
    QPushButton *save_button;
    QWidget *widget;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(950, 650);
        MainWindow->setMinimumSize(QSize(950, 650));
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.489, y2:0.517045, stop:0.235955 rgba(122, 88, 158, 255), stop:1 rgba(136, 163, 255, 255));"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy);
        centralWidget->setStyleSheet(QString::fromUtf8(""));
        horizontalLayout = new QHBoxLayout(centralWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        widget_2 = new QWidget(centralWidget);
        widget_2->setObjectName(QString::fromUtf8("widget_2"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(3);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(widget_2->sizePolicy().hasHeightForWidth());
        widget_2->setSizePolicy(sizePolicy1);
        widget_2->setStyleSheet(QString::fromUtf8("QWidget {\n"
"	background-color: rgba(85, 85, 127, 0);\n"
"	border-width: 1px;\n"
"	\n"
"	border-color: rgb(39, 39, 39);\n"
"	border-style: solid;\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
""));
        verticalLayout = new QVBoxLayout(widget_2);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        widget_6 = new QWidget(widget_2);
        widget_6->setObjectName(QString::fromUtf8("widget_6"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(2);
        sizePolicy2.setHeightForWidth(widget_6->sizePolicy().hasHeightForWidth());
        widget_6->setSizePolicy(sizePolicy2);
        widget_6->setStyleSheet(QString::fromUtf8(""));
        gridLayout_4 = new QGridLayout(widget_6);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        label_7 = new QLabel(widget_6);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout_4->addWidget(label_7, 0, 0, 1, 1);

        label_9 = new QLabel(widget_6);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout_4->addWidget(label_9, 2, 0, 1, 1);

        label_8 = new QLabel(widget_6);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout_4->addWidget(label_8, 1, 0, 1, 1);

        move_x = new QDoubleSpinBox(widget_6);
        move_x->setObjectName(QString::fromUtf8("move_x"));
        QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(2);
        sizePolicy3.setVerticalStretch(2);
        sizePolicy3.setHeightForWidth(move_x->sizePolicy().hasHeightForWidth());
        move_x->setSizePolicy(sizePolicy3);
        move_x->setMaximum(1000.000000000000000);

        gridLayout_4->addWidget(move_x, 0, 1, 1, 1);

        move_button = new QPushButton(widget_6);
        move_button->setObjectName(QString::fromUtf8("move_button"));
        move_button->setCursor(QCursor(Qt::PointingHandCursor));
        move_button->setStyleSheet(QString::fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.235955 rgba(106, 85, 167, 255), stop:1 rgba(136, 183, 255, 255));"));

        gridLayout_4->addWidget(move_button, 3, 0, 1, 2);

        move_y = new QDoubleSpinBox(widget_6);
        move_y->setObjectName(QString::fromUtf8("move_y"));
        sizePolicy3.setHeightForWidth(move_y->sizePolicy().hasHeightForWidth());
        move_y->setSizePolicy(sizePolicy3);
        move_y->setMaximum(1000.000000000000000);

        gridLayout_4->addWidget(move_y, 1, 1, 1, 1);

        move_z = new QDoubleSpinBox(widget_6);
        move_z->setObjectName(QString::fromUtf8("move_z"));
        sizePolicy3.setHeightForWidth(move_z->sizePolicy().hasHeightForWidth());
        move_z->setSizePolicy(sizePolicy3);
        move_z->setMaximum(1000.000000000000000);

        gridLayout_4->addWidget(move_z, 2, 1, 1, 1);


        verticalLayout->addWidget(widget_6);

        rotate_container = new QWidget(widget_2);
        rotate_container->setObjectName(QString::fromUtf8("rotate_container"));
        sizePolicy2.setHeightForWidth(rotate_container->sizePolicy().hasHeightForWidth());
        rotate_container->setSizePolicy(sizePolicy2);
        rotate_container->setStyleSheet(QString::fromUtf8(""));
        gridLayout_3 = new QGridLayout(rotate_container);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        label_6 = new QLabel(rotate_container);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout_3->addWidget(label_6, 0, 0, 1, 1);

        label_5 = new QLabel(rotate_container);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setStyleSheet(QString::fromUtf8(""));

        gridLayout_3->addWidget(label_5, 2, 0, 1, 1);

        rotate_x = new QDoubleSpinBox(rotate_container);
        rotate_x->setObjectName(QString::fromUtf8("rotate_x"));
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy4.setHorizontalStretch(2);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(rotate_x->sizePolicy().hasHeightForWidth());
        rotate_x->setSizePolicy(sizePolicy4);
        rotate_x->setMaximum(1000.000000000000000);

        gridLayout_3->addWidget(rotate_x, 0, 1, 1, 1);

        label_4 = new QLabel(rotate_container);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_3->addWidget(label_4, 1, 0, 1, 1);

        rotate_button = new QPushButton(rotate_container);
        rotate_button->setObjectName(QString::fromUtf8("rotate_button"));
        rotate_button->setCursor(QCursor(Qt::PointingHandCursor));
        rotate_button->setStyleSheet(QString::fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.235955 rgba(106, 85, 167, 255), stop:1 rgba(136, 183, 255, 255));"));

        gridLayout_3->addWidget(rotate_button, 3, 0, 1, 2);

        rotate_y = new QDoubleSpinBox(rotate_container);
        rotate_y->setObjectName(QString::fromUtf8("rotate_y"));
        sizePolicy4.setHeightForWidth(rotate_y->sizePolicy().hasHeightForWidth());
        rotate_y->setSizePolicy(sizePolicy4);
        rotate_y->setMaximum(1000.000000000000000);

        gridLayout_3->addWidget(rotate_y, 1, 1, 1, 1);

        rotate_z = new QDoubleSpinBox(rotate_container);
        rotate_z->setObjectName(QString::fromUtf8("rotate_z"));
        sizePolicy4.setHeightForWidth(rotate_z->sizePolicy().hasHeightForWidth());
        rotate_z->setSizePolicy(sizePolicy4);
        rotate_z->setMaximum(1000.000000000000000);

        gridLayout_3->addWidget(rotate_z, 2, 1, 1, 1);


        verticalLayout->addWidget(rotate_container);

        scale_container = new QWidget(widget_2);
        scale_container->setObjectName(QString::fromUtf8("scale_container"));
        sizePolicy2.setHeightForWidth(scale_container->sizePolicy().hasHeightForWidth());
        scale_container->setSizePolicy(sizePolicy2);
        scale_container->setStyleSheet(QString::fromUtf8(""));
        gridLayout_2 = new QGridLayout(scale_container);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label = new QLabel(scale_container);
        label->setObjectName(QString::fromUtf8("label"));
        label->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(label, 0, 1, 1, 1);

        scale_x = new QDoubleSpinBox(scale_container);
        scale_x->setObjectName(QString::fromUtf8("scale_x"));
        sizePolicy4.setHeightForWidth(scale_x->sizePolicy().hasHeightForWidth());
        scale_x->setSizePolicy(sizePolicy4);
        scale_x->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        scale_x->setMaximum(1000.000000000000000);

        gridLayout_2->addWidget(scale_x, 0, 2, 1, 1);

        label_3 = new QLabel(scale_container);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(label_3, 2, 1, 1, 1);

        scale_y = new QDoubleSpinBox(scale_container);
        scale_y->setObjectName(QString::fromUtf8("scale_y"));
        sizePolicy4.setHeightForWidth(scale_y->sizePolicy().hasHeightForWidth());
        scale_y->setSizePolicy(sizePolicy4);
        scale_y->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        scale_y->setMaximum(1000.000000000000000);

        gridLayout_2->addWidget(scale_y, 1, 2, 1, 1);

        scale_button = new QPushButton(scale_container);
        scale_button->setObjectName(QString::fromUtf8("scale_button"));
        scale_button->setCursor(QCursor(Qt::PointingHandCursor));
        scale_button->setStyleSheet(QString::fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.235955 rgba(106, 85, 167, 255), stop:1 rgba(136, 183, 255, 255));"));

        gridLayout_2->addWidget(scale_button, 3, 1, 1, 2);

        scale_z = new QDoubleSpinBox(scale_container);
        scale_z->setObjectName(QString::fromUtf8("scale_z"));
        sizePolicy4.setHeightForWidth(scale_z->sizePolicy().hasHeightForWidth());
        scale_z->setSizePolicy(sizePolicy4);
        scale_z->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        scale_z->setMaximum(1000.000000000000000);

        gridLayout_2->addWidget(scale_z, 2, 2, 1, 1);

        label_2 = new QLabel(scale_container);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(label_2, 1, 1, 1, 1);


        verticalLayout->addWidget(scale_container);

        save_load_container = new QWidget(widget_2);
        save_load_container->setObjectName(QString::fromUtf8("save_load_container"));
        QSizePolicy sizePolicy5(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(1);
        sizePolicy5.setHeightForWidth(save_load_container->sizePolicy().hasHeightForWidth());
        save_load_container->setSizePolicy(sizePolicy5);
        save_load_container->setStyleSheet(QString::fromUtf8(""));
        verticalLayout_2 = new QVBoxLayout(save_load_container);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        load_button = new QPushButton(save_load_container);
        load_button->setObjectName(QString::fromUtf8("load_button"));
        QFont font;
        font.setFamily(QString::fromUtf8("MS Shell Dlg 2"));
        font.setPointSize(8);
        font.setBold(false);
        font.setItalic(false);
        font.setUnderline(false);
        font.setWeight(50);
        font.setStrikeOut(false);
        font.setKerning(true);
        load_button->setFont(font);
        load_button->setCursor(QCursor(Qt::PointingHandCursor));
        load_button->setStyleSheet(QString::fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.235955 rgba(106, 85, 167, 255), stop:1 rgba(136, 183, 255, 255));"));

        verticalLayout_2->addWidget(load_button);

        save_button = new QPushButton(save_load_container);
        save_button->setObjectName(QString::fromUtf8("save_button"));
        save_button->setCursor(QCursor(Qt::PointingHandCursor));
        save_button->setStyleSheet(QString::fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.235955 rgba(106, 85, 167, 255), stop:1 rgba(136, 183, 255, 255));"));

        verticalLayout_2->addWidget(save_button);


        verticalLayout->addWidget(save_load_container);


        horizontalLayout->addWidget(widget_2);

        widget = new QWidget(centralWidget);
        widget->setObjectName(QString::fromUtf8("widget"));
        QSizePolicy sizePolicy6(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy6.setHorizontalStretch(8);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy6);
        widget->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));

        horizontalLayout->addWidget(widget);

        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label_7->setText(QApplication::translate("MainWindow", "dX: ", nullptr));
        label_9->setText(QApplication::translate("MainWindow", "dZ:", nullptr));
        label_8->setText(QApplication::translate("MainWindow", "dY:", nullptr));
        move_button->setText(QApplication::translate("MainWindow", "Move", nullptr));
        label_6->setText(QApplication::translate("MainWindow", "X:  ", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "Z:  ", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "Y:   ", nullptr));
        rotate_button->setText(QApplication::translate("MainWindow", "Rotate", nullptr));
        label->setText(QApplication::translate("MainWindow", "kX: ", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "kZ: ", nullptr));
        scale_button->setText(QApplication::translate("MainWindow", "Scale", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "kY:", nullptr));
        load_button->setText(QApplication::translate("MainWindow", "Load", nullptr));
        save_button->setText(QApplication::translate("MainWindow", "Save", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
