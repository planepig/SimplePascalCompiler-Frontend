# SimplePascalCompiler-Frontend
This is a course project for NEU 2023 Compiler Principles class

## Getting Started
### Prerequisites
This compiler is written in C++ and the GUI panel is implemented in Python, so you will need to have both languages installed on your system.

You will also need to have CMake installed to build the program's executable beforehand.

### Installing
After cloning or downloading this repository, navigate to the repository folder and run:
```
mkdir build
cd build
cmake -G"MinGW Makefiles" ..
cmake --build .
```
This should create a .exe file  in the build directory.

## Running the Program
To start the program, first compile the executable using the instructions from the previous sections. Then, run the following command in the repository folder:
```
python run.py
```
This should open the GUI panel and allow you to use the compiler.

## Acknowledgments
This compiler was mainly developed by lyy, so thank you @Lyydtc for your contributions to this project.