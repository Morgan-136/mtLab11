# Part 3: Creating the Main Program
#!/usr/bin/env python3
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    if __name__ == "__main__":
        # Root of the mindmap
        root = MindMapComposite("Coraline Discovers the Other World", "circle")

        characters = MindMapComposite("Characters", "oval")
        characters.add(MindMapLeaf("Coraline Jones", "plain"))
        characters.add(MindMapLeaf("Other Mother/the Beldam", "plain"))
        characters.add(MindMapLeaf("Other Father", "plain"))
        characters.add(MindMapLeaf("The Cat (mysterious guide)", "plain"))
        root.add(characters)

        plot_points = MindMapComposite("Plot Points", "square")
        plot_points.add(MindMapLeaf("Coraline unlocks the small door", "plain"))
        plot_points.add(MindMapLeaf("She crawls through the tunnel", "plain"))
        plot_points.add(MindMapLeaf("She enters a vibrant version of her home", "plain"))
        plot_points.add(MindMapLeaf("She meets the Other Mother and Other Father", "plain"))
        root.add(plot_points)

        themes = MindMapComposite("Themes", "cloud")
        themes.add(MindMapLeaf("Appearance vs. reality", "plain"))
        themes.add(MindMapLeaf("Control and deceit", "plain"))
        themes.add(MindMapLeaf("The danger of perfection", "plain"))
        themes.add(MindMapLeaf("Curiosity and consequences", "plain"))
        root.add(themes)

        setting = MindMapComposite("Setting", "hexagon")
        setting.add(MindMapLeaf("The Pink Palace apartment complex, Apt 22990", "plain"))
        setting.add(MindMapLeaf("The small hidden door", "plain"))
        setting.add(MindMapLeaf("The tunnel between worlds", "plain"))
        setting.add(MindMapLeaf("The Other World (bright and magical)", "plain"))
        root.add(setting)

        conflicts = MindMapComposite("Major Conflicts", "bang")
        conflicts.add(MindMapLeaf("Coraline’s curiosity vs. hidden danger", "plain"))
        conflicts.add(MindMapLeaf("Real world dullness vs. Other World excitement", "plain"))
        conflicts.add(MindMapLeaf("The Other Mother vs. Everyone", "plain"))
        root.add(conflicts)

        dialogue = MindMapComposite("Dialogue Highlights", "oval")
        dialogue.add(MindMapLeaf("\"Welcome home, Coraline.\"", "plain"))
        dialogue.add(MindMapLeaf("We’ve been waiting for you, Coraline", "plain"))
        dialogue.add(MindMapLeaf("Our eyes will be on Coraline!", "plain"))
        root.add(dialogue)

        stage_directions = MindMapComposite("Significant Stage Directions", "square")
        stage_directions.add(MindMapLeaf("Coraline opens the tiny door to reveal a tunnel", "plain"))
        stage_directions.add(MindMapLeaf("Camera follows her crawling through the tunnel", "plain"))
        stage_directions.add(MindMapLeaf("Lighting shifts from dull to vibrant colors", "plain"))
        stage_directions.add(MindMapLeaf("Reveal of the Other Mother with button eyes", "plain"))
        root.add(stage_directions)

        root.display()


if __name__ == "__main__":
    main()