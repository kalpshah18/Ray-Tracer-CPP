#ifndef CONSTANTS_AND_IMPORTS_H
#define CONSTANTS_AND_IMPORTS_H

#include <cmath>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <memory>
#include <random>

using std::make_shared;
using std::shared_ptr;

const double infinity = std::numeric_limits<double>::infinity();
const double pi = 3.1415926535897932385;

// Convert degrees to radians
inline double degrees_to_radians(double degrees) {
    return degrees * pi / 180.0;
}

// Returns a random real in [0,1).
inline double random_double() {
    static std::uniform_real_distribution<double> distribution(0.0, 1.0);
    static std::mt19937 generator;
    return distribution(generator);
}

// Returns a random real in [min,max)
inline double random_double(double min, double max) {
    return min + (max - min) * random_double();
}   

#include "color.h"
#include "interval.h"
#include "ray.h"
#include "vec3.h"

#endif