import csv
import json
import sys


def find_siblings(label_name, nested_list):
    for item in nested_list:
        for key, value in item.items():
            if key == "LabelName" and value == label_name:
                return nested_list
            elif key == "Subcategory" or key == "Part":
                a = find_siblings(label_name, value)
                if len(a) == 0:
                    continue
                else:
                    return a
    return []


def find_parent(label_name, nested_dict, parent):
    for key, value in nested_dict.items():
        if key == 'LabelName' and value == label_name:
            return parent
        elif key == 'Subcategory' or key == 'Part':
            for item in value:
                p = find_parent(label_name, item, nested_dict)
                if p:
                    return p
    return None


def find_ancestor(label_name, nested_dict, parent, ancestor):
    for key, value in nested_dict.items():
        if key == 'LabelName' and value == label_name:
            return ancestor
        elif key == 'Subcategory' or key == 'Part':
            for item in value:
                p = find_ancestor(label_name, item, nested_dict, parent)
                if p:
                    return p
    return None


def main(args):
    label_names = []
    class_names = []

    with open('oidv6-class-descriptions.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        idx = 0
        for row in reader:
            if idx == 0:
                idx = idx + 1
                continue

            label_name = row[0]
            display_name = row[1]
            label_names.append(label_name)
            class_names.append(display_name)
            idx = idx + 1

    with open('bbox_labels_600_hierarchy.json') as json_file:
        hierarchy = json.load(json_file)

    if len(args) == 1:
        class_name = args[0]
        if class_name not in class_names:
            print("Class name is not present")
            return

        idx = class_names.index(class_name)
        label_name = label_names[idx]

        siblings = find_siblings(label_name, [hierarchy])

        sibling_classes = []
        for sibling in siblings:
            try:
                idx = label_names.index(sibling['LabelName'])
                sibling_classes.append(class_names[idx])
            except ValueError:
                continue

        print("Sibling classes: ", sibling_classes)

        parent = find_parent(label_name, hierarchy, {})
        try:
            idx = label_names.index(parent['LabelName'])
            print("Parent class: ", class_names[idx])
        except (ValueError, TypeError):
            print("Parent class: No")

        ancestor = find_ancestor(label_name, hierarchy, {}, {})
        try:
            idx = label_names.index(ancestor['LabelName'])
            print("Ancestor class: ", class_names[idx])
        except (ValueError, TypeError):
            print("Ancestor class: No")

    elif len(args) > 1:
        class_name1 = args[0]
        class_name2 = args[1]

        idx = class_names.index(class_name1)
        label_name1 = label_names[idx]

        idx = class_names.index(class_name2)
        label_name2 = label_names[idx]

        ancestor1 = find_ancestor(label_name1, hierarchy, {}, {})
        ancestor2 = find_ancestor(label_name2, hierarchy, {}, {})

        try:
            if ancestor1['LabelName'] == ancestor2['LabelName']:
                print("Same")
            else:
                print("Not same")
        except (ValueError, TypeError):
            print("Not same")


if __name__ == '__main__':
    main(sys.argv[1:])
