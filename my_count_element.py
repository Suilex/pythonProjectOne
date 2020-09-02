def start():
    input_file = open("C:\\Users\suchm\Desktop\moby_01.txt")
    lines = input_file.read().split('\n')
    lines_count = len(lines)
    word_count = [len(item.split()) for item in lines]
    char_count = [len(item) for item in lines]
    print("count lines : {0}\n"
          "count words : {1}\n"
          "count chars : {2}".format(lines_count, sum(word_count), sum(char_count)))