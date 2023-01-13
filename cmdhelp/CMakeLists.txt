cmake_minimum_required(VERSION 3.13)
project(cmdhelp)
set(CMAKE_CXX_STANDARD 14)

set(SOURCE_FILES cmdhelp.cpp)

add_executable(cmdhelp ${SOURCE_FILES})
