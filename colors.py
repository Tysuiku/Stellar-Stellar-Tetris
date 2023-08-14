class Colors:
    dark_gray = (57,61,71)
    green = (47,249,36)
    red = (197,70,68)
    orange = (252,143,50)
    yellow = (255,233,0)
    purple = (199,36,177)
    cyan = (89,203,232)
    blue = (65,105,225)
    white = (255,255,255)
    dark_blue = (44, 44, 127)
    light_blue = (59,85,162)

    #@classmethod is a python decorator that allows you to define a method that 
    #can be called on a class rather than an instance of the class
    @classmethod
    #cls is a reference to the class itself and allows us access to the class-level
    #attributes and methods/ similiar to using self to access instance-level 
    #attributes and methods but cls is used for the class-level
    def get_cell_colors(cls):
        return [cls.dark_gray, cls.blue, cls.orange, cls.cyan, cls.yellow, cls.red, cls.purple, cls.green]