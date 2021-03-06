IF (goocanvasmm_INCLUDE_DIRS)

SET( SOURCE_FILES_VISUALSTATES
	iceinterface.cpp
	point.cpp
	node.cpp
	transition.cpp
	guinode.cpp
	subautomata.cpp
	guitransition.cpp
	guisubautomata.cpp
	generate.cpp
	popups/configfiledialog.cpp
	popups/editnodedialog.cpp
	popups/edittransitiondialog.cpp
    popups/edittransitioncodedialog.cpp
	popups/funvardialog.cpp
	popups/librariesdialog.cpp
	popups/loadfiledialog.cpp
	popups/renamedialog.cpp
	popups/renametransitiondialog.cpp
	popups/savefiledialog.cpp
	popups/timerdialog.cpp
	savefile.cpp
	xmlparser.cpp
	visualStates.cpp
	main.cpp
)


SET( SOURCE_FILES_RUNTIMEGUI
		automatagui.cpp
		point.cpp
		node.cpp
		transition.cpp
		subautomata.cpp
		guinode.cpp
		guitransition.cpp
		guisubautomata.cpp
		popups/editnodedialog.cpp
		popups/edittransitiondialog.cpp
		popups/edittransitioncodedialog.cpp
		popups/renamedialog.cpp
		popups/renametransitiondialog.cpp
)

link_directories(
	${resourcelocator_LIBRARY_DIRS}
)

include_directories (
	${CMAKE_CURRENT_BINARY_DIR}
    ${INTERFACES_CPP_DIR}
    ${LIBS_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${gtkmm3_INCLUDE_DIRS}
    ${goocanvasmm_INCLUDE_DIRS}
    ${gtk3_INCLUDE_DIRS}
    ${libxmlpp_INCLUDE_DIRS}
    ${resourcelocator_INCLUDE_DIRS}
)

add_executable (visualStates ${SOURCE_FILES_VISUALSTATES})
add_library(visualStateslib ${SOURCE_FILES_RUNTIMEGUI})

TARGET_LINK_LIBRARIES ( visualStates
    ${gtkmm3_LIBRARIES}
    ${goocanvasmm_LIBRARIES}
    ${gtk3_LIBRARIES}
    ${libxmlpp_LIBRARIES}
    ${resourcelocator_LIBRARIES}
		${GLOG_LIBRARIES}

		)

TARGET_LINK_LIBRARIES ( visualStateslib
		${gtkmm3_LIBRARIES}
		${goocanvasmm_LIBRARIES}
		${gtk3_LIBRARIES}
		${libxmlpp_LIBRARIES}
		${resourcelocator_LIBRARIES}
		${GLOG_LIBRARIES}
		)

configure_file(
		cmakevars.hpp.in
		cmakevars.hpp
		@ONLY
)

add_custom_command(TARGET visualStates POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR}/gui $<TARGET_FILE_DIR:visualStates>/gui)

    install(TARGETS visualStates
    DESTINATION ${CMAKE_INSTALL_PREFIX}/bin/
    COMPONENT tools)

	install(TARGETS visualStateslib
		DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/
		COMPONENT tools)

	install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/getinterfaces.sh 
      PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_EXECUTE GROUP_READ WORLD_EXECUTE WORLD_READ
	  DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)

    # Install Glade
	FILE(GLOB_RECURSE GLADE_FILES ${CMAKE_CURRENT_SOURCE_DIR}/gui/*.glade)
	INSTALL (FILES ${GLADE_FILES} DESTINATION ${CMAKE_INSTALL_PREFIX}/share/jderobot/glade)

	# install resources (jderobot logo)
	INSTALL (FILES ${CMAKE_CURRENT_SOURCE_DIR}/resources/jderobot.png DESTINATION ${CMAKE_INSTALL_PREFIX}/share/jderobot/resources)

	# Install C++ Headers
	FILE(GLOB h_files "${CMAKE_CURRENT_SOURCE_DIR}/*.h")
	INSTALL(FILES ${h_files} DESTINATION ${CMAKE_INSTALL_PREFIX}/include/jderobot/visualStates)

	FILE(GLOB h_files "${CMAKE_CURRENT_SOURCE_DIR}/popups/*.h")
	INSTALL(FILES ${h_files} DESTINATION ${CMAKE_INSTALL_PREFIX}/include/jderobot/visualStates/popups)

	# Install Python Files
	FILE(GLOB p_files "${CMAKE_CURRENT_SOURCE_DIR}/*.py")
	INSTALL(FILES ${p_files} DESTINATION ${CMAKE_INSTALL_PREFIX}/share/jderobot/python/visualStates_py)

ENDIF()