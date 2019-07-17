get_filename_component(contest_name ${CMAKE_CURRENT_SOURCE_DIR} NAME)

project(${contest_name} CXX)

file(GLOB SOURCES */main.cpp)

foreach(source IN ITEMS ${SOURCES})
    add_problem(${source})
endforeach()


