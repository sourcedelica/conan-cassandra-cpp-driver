project(CassReusePackage)
cmake_minimum_required(VERSION 3.5.1)

if(NOT APPLE AND NOT WIN32)
  set(EXTRA_FLAGS "-pthread")
endif()

set(CMAKE_CXX_FLAGS "-std=c++11 ${EXTRA_FLAGS}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ".")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

#include_directories(
#    ${CONAN_INCLUDE_DIRS_CASSANDRA-CPP-DRIVER}
#    ${CONAN_INCLUDE_DIRS_LIBUV})

#link_libraries(
#    ${CONAN_LIB_DIRS_CASSANDRA-CPP-DRIVER}/libcassandra_static.a
#    ${CONAN_LIB_DIRS_LIBUV}/libuv.a)

add_executable(test_compile test_compile.cpp)
