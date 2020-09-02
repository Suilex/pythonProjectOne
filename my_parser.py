def edit(arr):
    arr = arr.lower()
    ed = arr.maketrans(".,?!", "    ")
    arr = arr.translate(ed)
    arr = arr.split(" ")
    new_txt = []
    for item in arr:
        if item != '':
            new_txt.append(item)
    return new_txt


def calculate(text):
    set_unique = set(text)
    output = {}
    for item in set_unique:
        output[item] = text.count(item)
    return output


def start():
    input = open("C:\\Users\suchm\Desktop\moby_01.txt")
    output = open("C:\\Users\suchm\Desktop\output.txt", "w")
    text = input.read().split('\n')
    text = ' '.join(text)
    text = edit(text)
    text = calculate(text)
    output_list = []
    for item in text:
        output_list.append("{0} : {1}\n".format(item, text[item]))
    output.write(''.join(output_list))
