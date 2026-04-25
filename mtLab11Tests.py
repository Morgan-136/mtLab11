# Testing MindMapLeaf:
#from mindmap_leaf import MindMapLeaf
#leaf = MindMapLeaf("Hexagon Test", "hexagon") # Create a MindMapLeaf object
#print(str(leaf)) #tests the __str__ method
#leaf.display(2) # the display method
#print("MindMapLeaf tests completed!")

# Testing MindMapComposite
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite
root = MindMapComposite("Root", "circle")
branch = MindMapComposite("Branch 1", "square") # adding a composite node
root.add(branch)
leaf1 = MindMapLeaf("Child 1", "square")
leaf2 = MindMapLeaf("Child 2", "cloud")
branch.add(leaf1) #composite node
root.add(leaf2)
print(str(root))  # Should display "((Root))"
root.display()    # Should display root and its children
print("MindMapComposite tests completed!")

