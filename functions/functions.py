
def sort_list(lst: list, reverse_value):
    # lst1 = [float(i.replace("$", "")) for i in lst]
    # return sorted(lst1, reverse=reverse_value)
    return sorted(lst, key=lambda i: float(i.replace("$", "")), reverse=reverse_value)
