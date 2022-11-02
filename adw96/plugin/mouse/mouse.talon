podo:
	mouse_click()
	# close the mouse grid
	user.grid_close()
dubbo:
	mouse_click()
	mouse_click()
	# close the mouse grid
	user.grid_close()
trippo:
	mouse_click()
	mouse_click()
	mouse_click()
	# close the mouse grid
	user.grid_close()
righty:
	mouse_click(1)
	# close the mouse grid if open
	user.grid_close()

control mouse: user.mouse_toggle_control_mouse()
