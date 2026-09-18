# PLP Python Week 7

This repository contains my Week 7 Python list exercises.

'list_warmup.py'  Practices creating, accessing, and working with Python lists.
'shopping_list.py' Creates an interactive shopping list using list methods and a loop.
'list_report.py'  Prints a numbered list, counts items with more than four letters, and finds the longest item.
'screenshots/'  Contains screenshots showing each Python program running successfully.

This week's work helped me practice Python lists, loops, conditions, and list methods. I also learned how to organize my assignment files and document my work in a GitHub repository.

In shopping_list.py, the in membership check is used before calling .remove() to make sure the item exists in the list. Calling .remove() on an item that is not in the list raises a ValueError and can stop the program, while checking with in helps prevent the application from crashing. This makes the shopping list program safer and easier to use.