#include "converter.h"

converter::converter()
{

}

void converter::setColorRGB(int r, int g, int b) {
    base4.setRgb(r,g,b);
    base4ToOthers(base4);
}

void converter::setColorCMYK(float c, float m, float y, float k) {
    base4.setCmykF(c,m,y,k);
    base4ToOthers(base4);
}


void converter::setColorHLS(float h, float l, float s) {
    base4.setHslF(h,s,l);
    base4ToOthers(base4);
}



void converter::base4ToOthers(QColor a) {
    base4 = a;

}

QColor converter::getColor() const {
    return base4;
}
