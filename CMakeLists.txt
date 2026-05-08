cmake_minimum_required(VERSION 3.10)
project(RayTracer VERSION 0.1.0 LANGUAGES C CXX)

include(Ctest)
enable_testing()

add_executable(RayTracer 
    src/main.cpp
    src/vec3.h
    src/color.h
    src/ray.h)

set_property(TARGET RayTracer PROPERTY CXX_STANDARD 17)