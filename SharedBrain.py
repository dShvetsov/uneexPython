
class Overall:
    __count_click = 0
    def click(self):
        Overall.__count_click += 1
        return Overall.__count_click
