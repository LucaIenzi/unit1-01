import ui

def hello_world_mt_touch_up_inside(sender):
	view['hello_world_lable'].text = ("St Mother Teresa")
	view['name_lable'].text = ("titans")
def hello_world_joe_touch_up_inside(sender):
	view['hello_world_lable'].text = ("St Joes")
	view['name_lable'].text = ("jagwars")
def hello_world_mark_touch_up_inside(sender):
	view['hello_world_lable'].text = ("St marks")
	view['name_lable'].text = ("lions")
view = ui.load_view()
view.present('sheet')
