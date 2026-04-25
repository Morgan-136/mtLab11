# Part 2: Creating the MindMapComposite Class
# Define the MindMapComposite Class
import os
class MindMapComposite:
    #   Write the __init__ method
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = [] #composition (objects of objects)

     # Write the add method
    def add(self, child):
        self.children.append(child)

    # Write the remove method
    def remove(self, child):
        self.children.remove(child)

    # get_shape_representation taken from mindmap_leaf.py
    def get_shape_representation(self):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{}}}",
            "bang": ")){}(("
        }
        return shapes.get(self.shape, '{}')

    # Display method modified from mindmap_leaf.py
    def display(self, indent=0):
        if indent == 0:
            print('mindmap'+os.linesep+'  root', end='')
            print(' ' * indent + str(self))
            indent += 2
        else:
            print(' ' * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    # String method taken from mindmap_leaf.py
    def __str__(self):
        return self.get_shape_representation().format(self.name)




