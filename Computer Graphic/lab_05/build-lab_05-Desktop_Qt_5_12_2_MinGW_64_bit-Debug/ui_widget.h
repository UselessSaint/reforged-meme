/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QHBoxLayout *horizontalLayout;
    QFrame *frame_2;
    QVBoxLayout *verticalLayout;
    QFrame *frame;
    QGridLayout *gridLayout;
    QPushButton *paint;
    QPushButton *erase;
    QSpinBox *r;
    QLabel *label_2;
    QTableWidget *table;
    QSpinBox *g;
    QPushButton *addpoint;
    QCheckBox *delay;
    QLabel *label_4;
    QLabel *label_5;
    QFrame *line;
    QLabel *label_6;
    QLabel *label_3;
    QLabel *label;
    QPushButton *lock;
    QSpinBox *b;
    QSpinBox *y;
    QSpinBox *x;
    QLabel *label_7;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QString::fromUtf8("Widget"));
        Widget->resize(1920, 974);
        Widget->setMinimumSize(QSize(1920, 974));
        QFont font;
        font.setPointSize(14);
        Widget->setFont(font);
        horizontalLayout = new QHBoxLayout(Widget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        frame_2 = new QFrame(Widget);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setMaximumSize(QSize(310, 16777215));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frame_2);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        frame = new QFrame(frame_2);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setMinimumSize(QSize(0, 590));
        frame->setMaximumSize(QSize(292, 590));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        gridLayout = new QGridLayout(frame);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        paint = new QPushButton(frame);
        paint->setObjectName(QString::fromUtf8("paint"));

        gridLayout->addWidget(paint, 7, 5, 1, 1);

        erase = new QPushButton(frame);
        erase->setObjectName(QString::fromUtf8("erase"));

        gridLayout->addWidget(erase, 6, 5, 1, 1);

        r = new QSpinBox(frame);
        r->setObjectName(QString::fromUtf8("r"));
        r->setMinimum(1);
        r->setMaximum(561);

        gridLayout->addWidget(r, 5, 1, 1, 3);

        label_2 = new QLabel(frame);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 2, 0, 1, 2);

        table = new QTableWidget(frame);
        if (table->columnCount() < 2)
            table->setColumnCount(2);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        table->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        table->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        table->setObjectName(QString::fromUtf8("table"));
        table->setMinimumSize(QSize(217, 350));
        table->setMaximumSize(QSize(217, 350));

        gridLayout->addWidget(table, 3, 1, 1, 5);

        g = new QSpinBox(frame);
        g->setObjectName(QString::fromUtf8("g"));
        g->setMinimum(1);
        g->setMaximum(561);

        gridLayout->addWidget(g, 6, 1, 1, 3);

        addpoint = new QPushButton(frame);
        addpoint->setObjectName(QString::fromUtf8("addpoint"));

        gridLayout->addWidget(addpoint, 1, 4, 2, 2);

        delay = new QCheckBox(frame);
        delay->setObjectName(QString::fromUtf8("delay"));
        QFont font1;
        font1.setPointSize(13);
        delay->setFont(font1);

        gridLayout->addWidget(delay, 4, 5, 1, 1);

        label_4 = new QLabel(frame);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 5, 0, 1, 1);

        label_5 = new QLabel(frame);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 6, 0, 1, 1);

        line = new QFrame(frame);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout->addWidget(line, 4, 4, 4, 1);

        label_6 = new QLabel(frame);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout->addWidget(label_6, 7, 0, 1, 1);

        label_3 = new QLabel(frame);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 4, 0, 1, 4);

        label = new QLabel(frame);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 1, 0, 1, 1);

        lock = new QPushButton(frame);
        lock->setObjectName(QString::fromUtf8("lock"));

        gridLayout->addWidget(lock, 5, 5, 1, 1);

        b = new QSpinBox(frame);
        b->setObjectName(QString::fromUtf8("b"));
        b->setMinimum(1);
        b->setMaximum(561);

        gridLayout->addWidget(b, 7, 1, 1, 3);

        y = new QSpinBox(frame);
        y->setObjectName(QString::fromUtf8("y"));
        y->setMinimum(1);
        y->setMaximum(581);

        gridLayout->addWidget(y, 2, 2, 1, 1);

        x = new QSpinBox(frame);
        x->setObjectName(QString::fromUtf8("x"));
        x->setMinimum(1);
        x->setMaximum(561);

        gridLayout->addWidget(x, 1, 2, 1, 1);


        verticalLayout->addWidget(frame);

        label_7 = new QLabel(frame_2);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setMinimumSize(QSize(292, 354));
        label_7->setMaximumSize(QSize(292, 384));

        verticalLayout->addWidget(label_7);


        horizontalLayout->addWidget(frame_2);


        retranslateUi(Widget);
        QObject::connect(addpoint, SIGNAL(clicked()), Widget, SLOT(addDot()));
        QObject::connect(erase, SIGNAL(clicked()), Widget, SLOT(clear()));
        QObject::connect(paint, SIGNAL(clicked()), Widget, SLOT(fill()));
        QObject::connect(lock, SIGNAL(clicked()), Widget, SLOT(closeEdges()));

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QApplication::translate("Widget", "\320\227\320\260\320\277\320\276\320\273\320\275\320\265\320\275\320\270\320\265 \320\276\320\261\320\273\320\260\321\201\321\202\320\265\320\271", nullptr));
        paint->setText(QApplication::translate("Widget", "\320\227\320\260\320\272\321\200\320\260\321\201\320\270\321\202\321\214", nullptr));
        erase->setText(QApplication::translate("Widget", "\320\236\321\207\320\270\321\201\321\202\320\270\321\202\321\214", nullptr));
        label_2->setText(QApplication::translate("Widget", "Y", nullptr));
        QTableWidgetItem *___qtablewidgetitem = table->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("Widget", "X", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = table->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("Widget", "Y", nullptr));
        addpoint->setText(QApplication::translate("Widget", "\320\224\320\276\320\261\320\260\320\262\320\270\321\202\321\214 \321\202\320\276\321\207\320\272\321\203", nullptr));
        delay->setText(QApplication::translate("Widget", "\320\241 \320\267\320\260\320\264\320\265\321\200\320\266\320\272\320\276\320\271", nullptr));
        label_4->setText(QApplication::translate("Widget", "R", nullptr));
        label_5->setText(QApplication::translate("Widget", "G", nullptr));
        label_6->setText(QApplication::translate("Widget", "B", nullptr));
        label_3->setText(QApplication::translate("Widget", "\320\222\321\213\320\261\320\276\321\200 \321\206\320\262\320\265\321\202\320\260", nullptr));
        label->setText(QApplication::translate("Widget", "X", nullptr));
        lock->setText(QApplication::translate("Widget", "\320\227\320\260\320\274\320\272\320\275\321\203\321\202\321\214", nullptr));
        label_7->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
