import copy 


class Prototype:
    def __init__(self):
        self._objects = {}
    
    def regisger(self, name, obj):
        self._objects[name] = obj
    
    def unregister(self, name):
        if name in self._objects:
            del self._objects[name]

    def clone(self, name, **attrs):
        if name not in self._objects:
            raise ValueError(f"{name} doesn't exist.")
        
        obj_copy = copy.deepcopy(self._objects[name])
        obj_copy.__dict__.update(attrs)      
        return obj_copy


class Button:
    def __init__(self, color, text, x_pos, y_pos):
        self.color = color
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def __str__(self):
        return f"Button: {self.color}, {self.text}, {self.x_pos}, {self.y_pos}"


base_button = Button("red", "Click me", 100, 100)
prototype = Prototype()
prototype.regisger("base_button", base_button)

button1 = prototype.clone("base_button", color="blue", x_pos=200, y_pos=200)
print(button1)
button2 = prototype.clone("base_button", color="green", x_pos=300, y_pos=300)
print(button2)
