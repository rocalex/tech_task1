# Task 1 Open Images class hierarchy

- Find all siblings class of a class name
- Find the parent class of a class name
- Find the ancestor class of a class name

```shell
python main.py "Class name"
```

for example:

```shell
$ python main.py "Ladle"
Sibling classes:  ['Chopsticks', 'Ladle', 'Spatula', 'Can opener', 'Cutting board', 'Whisk', 'Drinking straw', 'Knife', 'Bottle opener', 'Measuring cup', 'Pizza cutter', 'Spoon', 'Fork']
Parent class:  Kitchen utensil
Ancestor class:  Kitchenware
$ python main.py "Pochas"
Sibling classes:  []
Parent class: No
Ancestor class: No
```

- Find if both class 1 and class 2 belong to the same ancestor class

```shell
$ python main.py "Ladle" "Capellini"
Not same
$ python main.py "Chopsticks" "Drinking straw"
Same
```