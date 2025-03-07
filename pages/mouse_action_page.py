from pages.base import Base


class MouseActionPage(Base):
    def __init__(self, loc):
        self.bx = self.base_find_element(loc)
        
    def get_click_color(self, loc):
        self.actions.click_and_hold(self.bx).perform()
        color = self.bx.value_of_css_property('background-color')
        self.actions.release().perform()
        return color
    
    def move_pointer_by_offset(self, x_index, y_index):
        self.actions.move_by_offset(self.bx, x_index, y_index)
        

        