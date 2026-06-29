def sort_colors(color_string):
    colors_list = color_string.split('-')
    colors_list.sort()
    return '-'.join(colors_list)
