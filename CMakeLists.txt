cmake_minimum_required(VERSION 3.16)
project(robotont_navigation)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config launch
  DESTINATION share/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.yaml" PATTERN "*.py" PATTERN "*.xml"
)

ament_package()
