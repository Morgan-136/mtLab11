# Part 1: Creating the MindMapLeaf Class
# Define the MindMapLeaf class:
class MindMapLeaf:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

# Defining shapes from Mermaid's mindmap feature
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

# Write the display method for indentation
    def display(self, indent=0):
        print(' ' * indent + str(self))

# Define the string method:
    def __str__(self):
        return self.get_shape_representation().format(self.name)



