set(PATH_TO_SCRIPTS ${CMAKE_CURRENT_LIST_DIR})

find_package(Python3 REQUIRED COMPONENTS Interpreter)

function(add_problem_tests problem_dir contest_name)

    get_filename_component(problem_name ${problem_dir} NAME)

    message("${contest_name}.${problem_name}.compare_tests")

    add_custom_target("${contest_name}.${problem_name}.run_tests"
            COMMAND Python3::Interpreter ${PATH_TO_SCRIPTS}/run_tests.py $<TARGET_FILE:${contest_name}.${problem_name}>
            COMMAND Python3::Interpreter ${PATH_TO_SCRIPTS}/compare_tests.py
            WORKING_DIRECTORY ${problem_dir}
            DEPENDS "${contest_name}.${problem_name}"
            )

endfunction()

function(add_problem main_cpp)
    get_filename_component(problem_dir ${source} DIRECTORY)
    get_filename_component(problem_name ${problem_dir} NAME)
    add_executable("${contest_name}.${problem_name}" ${source})
    add_problem_tests(${problem_dir} ${contest_name})
endfunction()
