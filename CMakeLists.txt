cmake_minimum_required(VERSION 3.25)
project(compiler)

set(CMAKE_CXX_STANDARD 17)

add_executable(compiler main.cpp Compiler107.cpp lexAna.cpp)
