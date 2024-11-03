#include "widget.h"
#include "QDebug"
#include <QRegularExpression>

Widget::Widget(QWidget *parent)
    : QWidget(parent) {
    RGB_Grad->installEventFilter(this);
    CreatingModels();
    DarkTheme();
    sliderR->setMaximum(255);
    sliderR->setMinimum(0);
    sliderG->setMaximum(255);
    sliderG->setMinimum(0);
    sliderB->setMaximum(255);
    sliderB->setMinimum(0);
    chosenColorl = new QVBoxLayout;
    RightL = new QHBoxLayout;
    zone3 = new QGridLayout;
    zone2 = new QGridLayout;
    zone1 = new QGridLayout;
    labels_ = new QHBoxLayout;
    color_switch1 = new QLabel("RGB");
    color_switch2 = new QLabel("CMYK");
    color_switch3 = new QLabel("HLS");


    zones =  new QHBoxLayout;
    main = new QVBoxLayout;
    main_ = new QHBoxLayout;

    labels_->addWidget(color_switch1);
    labels_->addWidget(color_switch2);
    labels_->addWidget(color_switch3);

    zone1->addWidget(RGB,2,0);
    zone2->addWidget(CMYK,2,0);
    zone3->addWidget(HLS,2,0);

    zones->addLayout(zone1);
    zones->addLayout(zone2);
    zones->addLayout(zone3);

    exit->setText("=EXIT=");

    RGB_Grad->setCursor(Qt::CrossCursor);

    sliderR->setCursor(Qt::PointingHandCursor);
    sliderG->setCursor(Qt::PointingHandCursor);
    sliderB->setCursor(Qt::PointingHandCursor);


    main->addWidget(new QLabel{"Gradient Choosing:"});
    main_->addWidget(RGB_Grad);
    main_->addLayout(RightL);
    chosenColorl->setAlignment(Qt::AlignmentFlag::AlignVCenter);
    chosenColorl->addWidget(new QLabel{"Choosen color:"});
    chosenColorl->addWidget(currentColorLabel);
    chosenColorl->addWidget(exit);
    main_->addLayout(chosenColorl);
    main_->setAlignment(Qt::AlignmentFlag::AlignLeft);
    main->addLayout(main_);
    main->addSpacing(15);
    main->addLayout(labels_);
    main->addLayout(zones);


    this->setLayout(main);
    connect(exit,SIGNAL(clicked(bool)),SLOT(ExitButtonPressed()));

    connect(R,SIGNAL(editingFinished()),SLOT(set_RGB()));
    connect(G,SIGNAL(editingFinished()),SLOT(set_RGB()));
    connect(B,SIGNAL(editingFinished()),SLOT(set_RGB()));

    connect(C,SIGNAL(editingFinished()),SLOT(set_CMYK()));
    connect(M,SIGNAL(editingFinished()),SLOT(set_CMYK()));
    connect(Y,SIGNAL(editingFinished()),SLOT(set_CMYK()));
    connect(K,SIGNAL(editingFinished()),SLOT(set_CMYK()));

    connect(HLS_H,SIGNAL(editingFinished()),SLOT(set_HLS()));
    connect(HLS_L,SIGNAL(editingFinished()),SLOT(set_HLS()));
    connect(HLS_S,SIGNAL(editingFinished()),SLOT(set_HLS()));


    //sliders connect
    connect(Rs,SIGNAL(sliderReleased()),SLOT(set_Slider_RGB()));
    connect(Gs,SIGNAL(sliderReleased()),SLOT(set_Slider_RGB()));
    connect(Bs,SIGNAL(sliderReleased()),SLOT(set_Slider_RGB()));

    connect(Cs,SIGNAL(sliderReleased()),SLOT(set_Slider_CMYK()));
    connect(Ms,SIGNAL(sliderReleased()),SLOT(set_Slider_CMYK()));
    connect(Ys,SIGNAL(sliderReleased()),SLOT(set_Slider_CMYK()));
    connect(Ks,SIGNAL(sliderReleased()),SLOT(set_Slider_CMYK()));

    connect(Hs1,SIGNAL(sliderReleased()),SLOT(set_Slider_HLS()));
    connect(Ls1,SIGNAL(sliderReleased()),SLOT(set_Slider_HLS()));
    connect(Ss1,SIGNAL(sliderReleased()),SLOT(set_Slider_HLS()));

    installALLinfo();
}

void Widget::CreatingModels() {
    RGB = new QGroupBox;
    CMYK = new QGroupBox;
    HLS = new QGroupBox;

    RGB_l = new QGridLayout;
    CMYK_l = new QGridLayout;
    HLS_l = new QGridLayout;

    QRegularExpression rgx1("[0-9]|[1-9][0-9]|0[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]");
    QValidator *comValidator1 = new  QRegularExpressionValidator(rgx1, this);
    R->setValidator(comValidator1);
    G->setValidator(comValidator1);
    B->setValidator(comValidator1);
    QRegularExpression rgx2("[0-9]|[1-9][0-9]|0[0-9][0-9]|100");
    QValidator *comValidator2 = new  QRegularExpressionValidator(rgx2, this);
    C->setValidator(comValidator2);
    M->setValidator(comValidator2);
    Y->setValidator(comValidator2);
    K->setValidator(comValidator2);

    QRegularExpression rgx3("[0-9]|[1-9][0-9]|0[0-9][0-9]|1[0-9][0-9]|2[0-9][0-9]|3[0-5][0-9]|360");
    QValidator *comValidator3 = new QRegularExpressionValidator(rgx3,this);
    HLS_H->setValidator(comValidator3);
    HLS_L->setValidator(comValidator2);
    HLS_S->setValidator(comValidator2);
    RGB_Grad->setFixedSize(this->width()/3,this->width()/6);
    currentColorLabel->setFixedSize(this->width()/12,this->width()/12);

    Rs->setOrientation(Qt::Horizontal);
    Gs->setOrientation(Qt::Horizontal);
    Bs->setOrientation(Qt::Horizontal);
    Rs->setMaximum(255);
    Rs->setMinimum(0);
    Gs->setMaximum(255);
    Gs->setMinimum(0);
    Bs->setMaximum(255);
    Bs->setMinimum(0);
    RGB_l->addWidget(new QLabel{"R:"},1,0);
    RGB_l->addWidget(R,1,1);
    RGB_l->addWidget(new QLabel{"G:"},2,0);
    RGB_l->addWidget(G,2,1);
    RGB_l->addWidget(new QLabel{"B:"},3,0);
    RGB_l->addWidget(B,3,1);
    RGB_l->addWidget(Rs,1,2);
    RGB_l->addWidget(Gs,2,2);
    RGB_l->addWidget(Bs,3,2);
    RGB->setLayout(RGB_l);


    Cs->setOrientation(Qt::Horizontal);
    Ms->setOrientation(Qt::Horizontal);
    Ys->setOrientation(Qt::Horizontal);
    Ks->setOrientation(Qt::Horizontal);
    Cs->setRange(0,100);
    Ms->setRange(0,100);
    Ys->setRange(0,100);
    Ks->setRange(0,100);
    CMYK_l->addWidget(new QLabel{"C:"},1,0);
    CMYK_l->addWidget(C,1,1);
    CMYK_l->addWidget(new QLabel{"M:"},2,0);
    CMYK_l->addWidget(M,2,1);
    CMYK_l->addWidget(new QLabel{"Y:"},3,0);
    CMYK_l->addWidget(Y,3,1);
    CMYK_l->addWidget(new QLabel{"K:"},4,0);
    CMYK_l->addWidget(K,4,1);
    CMYK_l->addWidget(Cs,1,2);
    CMYK_l->addWidget(Ms,2,2);
    CMYK_l->addWidget(Ys,3,2);
    CMYK_l->addWidget(Ks,4,2);
    CMYK->setLayout(CMYK_l);


    Hs1->setOrientation(Qt::Horizontal);
    Ls1->setOrientation(Qt::Horizontal);
    Ss1->setOrientation(Qt::Horizontal);
    Hs1->setRange(0,360);
    Ls1->setRange(0,100);
    Ss1->setRange(0,100);
    HLS_l->addWidget(new QLabel{"H:"},1,0);
    HLS_l->addWidget(HLS_H,1,1);
    HLS_l->addWidget(new QLabel{"L:"},2,0);
    HLS_l->addWidget(HLS_L,2,1);
    HLS_l->addWidget(new QLabel{"S:"},3,0);
    HLS_l->addWidget(HLS_S,3,1);
    HLS_l->addWidget(Hs1,1,2);
    HLS_l->addWidget(Ls1,2,2);
    HLS_l->addWidget(Ss1,3,2);
    HLS->setLayout(HLS_l);

}

void Widget::paintEvent(QPaintEvent*) {
    QPixmap pix(RGB_Grad->width(),RGB_Grad->height());
    QPixmap pix2(currentColorLabel->width(),currentColorLabel->height());
    QPainter painter(&pix);
    QPainter painter2(&pix2);
    QLinearGradient gradient(0,0,pix.width(),0);
    for (int i = 0; i < 360; i++) {
        QColor color = QColor::fromHsl(i, 255, 128);
        gradient.setColorAt(i / 360.0, color);
    }

    painter.setBrush(gradient);
    painter.drawRect(0,0,RGB_Grad->width(),RGB_Grad->height());
    RGB_Grad->setPixmap(pix);
    painter2.setBrush(color.getColor());
    painter2.drawRect(0, 0, currentColorLabel->width(), currentColorLabel->height());
    currentColorLabel->setPixmap(pix2);
}


void Widget::DarkTheme() {
    QPalette darkPalette;
    darkPalette.setColor(QPalette::Window, QColor(53, 53, 53));
    darkPalette.setColor(QPalette::WindowText, Qt::white);
    darkPalette.setColor(QPalette::Base, QColor(25, 25, 25));
    darkPalette.setColor(QPalette::AlternateBase, QColor(53, 53, 53));
    darkPalette.setColor(QPalette::ToolTipBase, Qt::white);
    darkPalette.setColor(QPalette::ToolTipText, Qt::white);
    darkPalette.setColor(QPalette::Text, Qt::white);
    darkPalette.setColor(QPalette::Button, QColor(53, 53, 53));
    darkPalette.setColor(QPalette::ButtonText, Qt::white);
    darkPalette.setColor(QPalette::BrightText, Qt::red);
    darkPalette.setColor(QPalette::Link, QColor(42, 130, 218));
    darkPalette.setColor(QPalette::Highlight, QColor(42, 130, 218));
    darkPalette.setColor(QPalette::HighlightedText, Qt::black);
    qApp->setPalette(darkPalette);
}

void Widget::GradientColor() {
    update();
}

void Widget::ExitButtonPressed() {
    this->close();
}

void Widget::set_RGB() {
    color.setColorRGB(R->text().toInt(),G->text().toInt(),B->text().toInt());
    installALLinfo();
}

void Widget::set_CMYK() {
    color.setColorCMYK(C->text().toFloat()/100,M->text().toFloat()/100,Y->text().toFloat()/100,K->text().toFloat()/100);
    installALLinfo();
}


void Widget::set_HLS() {
    color.setColorHLS(HLS_H->text().toFloat()/360,HLS_L->text().toFloat()/100,HLS_S->text().toFloat()/100);
    installALLinfo();
}


void Widget::set_Slider_RGB() {
    color.setColorRGB(Rs->value(),Gs->value(),Bs->value());
    installALLinfo();
}

void Widget::set_Slider_CMYK()
{
    color.setColorCMYK((float)Cs->value()/100,(float)Ms->value()/100,(float)Ys->value()/100,(float)Ks->value()/100);
    installALLinfo();
}

void Widget::set_Slider_HLS() {
    color.setColorHLS((float)Hs1->value()/360,(float)Ls1->value()/100,(float)Ss1->value()/100);
    installALLinfo();
}


Widget::~Widget() {}

void Widget::installALLinfo() {
    currentColor = color.getColor();

    R->setText(QString::number(color.getColor().red()));
    G->setText(QString::number(color.getColor().green()));
    B->setText(QString::number(color.getColor().blue()));

    Rs->setSliderPosition(color.getColor().red());
    Gs->setSliderPosition(color.getColor().green());
    Bs->setSliderPosition(color.getColor().blue());

    C->setText(QString::number(color.getColor().cyanF()*100));
    M->setText(QString::number(color.getColor().magentaF()*100));
    Y->setText(QString::number(color.getColor().yellowF()*100));
    K->setText(QString::number(color.getColor().blackF()*100));

    Cs->setSliderPosition(color.getColor().cyanF()*100);
    Ms->setSliderPosition(color.getColor().magentaF()*100);
    Ys->setSliderPosition(color.getColor().yellowF()*100);
    Ks->setSliderPosition(color.getColor().blackF()*100);

    float h = color.getColor().hslHueF()*360;
    if(h < 0) h = 0;
    HLS_H->setText(QString::number(h));
    HLS_L->setText(QString::number(color.getColor().lightnessF()*100));
    HLS_S->setText(QString::number(color.getColor().hslSaturationF()*100));

    Hs1->setSliderPosition(color.getColor().hslHueF()*360);
    Ls1->setSliderPosition(color.getColor().lightnessF()*100);
    Ss1->setSliderPosition(color.getColor().hslSaturationF()*100);

}

bool Widget::eventFilter(QObject *obj, QEvent *event) {
    if(event->type() == QEvent::MouseButtonPress && obj == RGB_Grad) {
        QMouseEvent* cur = dynamic_cast<QMouseEvent*>(event);
        int x = cur->pos().x()+RGB_Grad->x();
        int y = cur->pos().y()+RGB_Grad->y();
        color.base4ToOthers(QWidget::grab(QRect(x, y, 1, 1)).toImage().pixelColor(0, 0));
        installALLinfo();
    }
    return false;
}
