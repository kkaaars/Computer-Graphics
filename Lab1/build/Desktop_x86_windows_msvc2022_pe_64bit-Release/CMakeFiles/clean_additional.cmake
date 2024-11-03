# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Release")
  file(REMOVE_RECURSE
  "CMakeFiles\\Colors_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Colors_autogen.dir\\ParseCache.txt"
  "Colors_autogen"
  )
endif()
