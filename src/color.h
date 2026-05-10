#ifndef COLOR_H
#define COLOR_H

#include "interval.h"
#include "vec3.h"

using color = vec3;

void write_color(std::ostream &out, const color& pixel_color) {
    auto r = pixel_color.x();
    auto g = pixel_color.y();
    auto b = pixel_color.z();

    // Converting [0, 1] component values to byte range [0, 255]
    static const interval intensity(0.0, 0.999);
    int rbyte = static_cast<int>(256 * intensity.clamp(r));
    int gbyte = static_cast<int>(256 * intensity.clamp(g));
    int bbyte = static_cast<int>(256 * intensity.clamp(b));

    // Displaying Pixel Color Components
    out << rbyte << ' ' << gbyte << ' ' << bbyte << '\n';
}

#endif