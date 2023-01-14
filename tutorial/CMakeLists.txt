cmake_minimum_required(VERSION 3.13)
project(tutorial)
set(CMAKE_CXX_STANDARD 14)

set(SOURCE_FILES tut.cpp)

add_executable(tutorial ${SOURCE_FILES})
