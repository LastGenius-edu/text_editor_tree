Basic text editor built using curses library in Python. A playground to implement tree of changes.

Tree of changes records all the changes to the text and allows for more than linear undo-redo relationship, instead opting for a tree of changes starting with a root (empty file).

# Example of functionality:

```bash
git clone https://github.com/LastGenius-edu/text_editor_tree.git
cd text_editor_tree
python3 main.py
```

Example file went from empty in four different ways:

![](https://raw.githubusercontent.com/LastGenius-edu/text_editor_tree/master/img1.png)

We can choose the third branch (full of 'l's):

![](https://raw.githubusercontent.com/LastGenius-edu/text_editor_tree/master/img2.png)

And then redo the whole file by going further in that branch:

![](https://raw.githubusercontent.com/LastGenius-edu/text_editor_tree/master/img3.png) 

Works on Linux, shouldn't probably work on Windows.