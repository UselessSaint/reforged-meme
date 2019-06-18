/****************************************************************************
** Meta object code from reading C++ file 'cabin.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.12.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../lab_3/cabin.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'cabin.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.12.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_Lift_cabin_t {
    QByteArrayData data[14];
    char stringdata0[152];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_Lift_cabin_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_Lift_cabin_t qt_meta_stringdata_Lift_cabin = {
    {
QT_MOC_LITERAL(0, 0, 10), // "Lift_cabin"
QT_MOC_LITERAL(1, 11, 10), // "pre_moving"
QT_MOC_LITERAL(2, 22, 0), // ""
QT_MOC_LITERAL(3, 23, 14), // "crossing_floor"
QT_MOC_LITERAL(4, 38, 5), // "floor"
QT_MOC_LITERAL(5, 44, 9), // "direction"
QT_MOC_LITERAL(6, 54, 1), // "d"
QT_MOC_LITERAL(7, 56, 14), // "reached_target"
QT_MOC_LITERAL(8, 71, 13), // "cabin_stopped"
QT_MOC_LITERAL(9, 85, 16), // "change_note_text"
QT_MOC_LITERAL(10, 102, 4), // "text"
QT_MOC_LITERAL(11, 107, 12), // "cabin_moving"
QT_MOC_LITERAL(12, 120, 14), // "cabin_stopping"
QT_MOC_LITERAL(13, 135, 16) // "cabin_set_target"

    },
    "Lift_cabin\0pre_moving\0\0crossing_floor\0"
    "floor\0direction\0d\0reached_target\0"
    "cabin_stopped\0change_note_text\0text\0"
    "cabin_moving\0cabin_stopping\0"
    "cabin_set_target"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_Lift_cabin[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       5,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   54,    2, 0x06 /* Public */,
       3,    2,   55,    2, 0x06 /* Public */,
       7,    1,   60,    2, 0x06 /* Public */,
       8,    1,   63,    2, 0x06 /* Public */,
       9,    1,   66,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      11,    0,   69,    2, 0x0a /* Public */,
      12,    0,   70,    2, 0x0a /* Public */,
      13,    1,   71,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int, 0x80000000 | 5,    4,    6,
    QMetaType::Void, QMetaType::Int,    4,
    QMetaType::Void, QMetaType::Int,    4,
    QMetaType::Void, QMetaType::QString,   10,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    4,

       0        // eod
};

void Lift_cabin::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<Lift_cabin *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->pre_moving(); break;
        case 1: _t->crossing_floor((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< direction(*)>(_a[2]))); break;
        case 2: _t->reached_target((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->cabin_stopped((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->change_note_text((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 5: _t->cabin_moving(); break;
        case 6: _t->cabin_stopping(); break;
        case 7: _t->cabin_set_target((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (Lift_cabin::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Lift_cabin::pre_moving)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (Lift_cabin::*)(int , direction );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Lift_cabin::crossing_floor)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (Lift_cabin::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Lift_cabin::reached_target)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (Lift_cabin::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Lift_cabin::cabin_stopped)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (Lift_cabin::*)(QString );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Lift_cabin::change_note_text)) {
                *result = 4;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject Lift_cabin::staticMetaObject = { {
    &QObject::staticMetaObject,
    qt_meta_stringdata_Lift_cabin.data,
    qt_meta_data_Lift_cabin,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *Lift_cabin::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Lift_cabin::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_Lift_cabin.stringdata0))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Lift_cabin::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 8)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 8;
    }
    return _id;
}

// SIGNAL 0
void Lift_cabin::pre_moving()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void Lift_cabin::crossing_floor(int _t1, direction _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void Lift_cabin::reached_target(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void Lift_cabin::cabin_stopped(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}

// SIGNAL 4
void Lift_cabin::change_note_text(QString _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
