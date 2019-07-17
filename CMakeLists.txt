cmake_minimum_required(VERSION 3.10)
project(gym)

set(CMAKE_CXX_STANDARD 14)

include(scripts/AddProblem.cmake)

# add contest folder
add_subdirectory(101)
