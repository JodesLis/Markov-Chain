
import random

#create a dictionary that maps from prefix -> all found words after


def read_file(filename):
    """
    reads in a prject gutenberg text file
    and ignores header/footer
    """
    text_as_list = []
    with open(filename, "r") as file_in:
        for line_temp in file_in:
            if line_temp.startswith("*** START OF"):
                break
        for line in file_in:
            if line.startswith("*** END OF"):
                break
            else:
                for word in line.split():
                    text_as_list.append(word)
    return text_as_list


def build_prefix_dict(text_list):
    """
    uses the text in list form to gen dictionary
    of form {prefix : suffix]
    output is dictionary
    """
    prefix_dict = {}
    i = 0
    while i + 1 < len(text_list):
        prefix = text_list[i]
        suffix = text_list[i + 1]
        if prefix not in prefix_dict:
            prefix_dict[prefix] = []
            prefix_dict[prefix].append(suffix)
        else:
            prefix_dict[prefix].append(suffix)
        i += 1
    return prefix_dict


def build_4_prefix(text_list):
    """
    uses the text in list form to gen dictionary
    of form {prefix : [suffix, suffix2, suffix3]
    output is dictionary
    """
    prefix_dict = {}
    i = 0
    while i + 4 < len(text_list):
        prefix = text_list[i]
        suffix_1 = text_list[i + 1]
        suffix_2 = text_list[i + 2]
        suffix_3 = text_list[i + 3]
        suffix_4 = text_list[i + 4]
        if prefix not in prefix_dict:
            prefix_dict[prefix] = []
            prefix_dict[prefix].append([suffix_1, suffix_2, suffix_3, suffix_4])
        else:
            prefix_dict[prefix].append([suffix_1, suffix_2, suffix_3, suffix_4])
        i += 1
    return prefix_dict


def gen_random_word(prefix, prefix_dict):
    """
    returns a random suffix when given
    prefix and prefix dictionary
    """
    return random.choice(prefix_dict[prefix])


def gen_sentence(prefix_dict, sentence_length):
    """
    generates a random sentance using the prefix
    dictionary

    sentence_length : an integer to determine
                      how many words to add
    """
    string = ""
    string += random.choice(prefix_dict.keys())
    prefix = string
    for i in range(sentence_length):
        suffix = gen_random_word(prefix, prefix_dict)
        string += " " + suffix
        prefix = suffix
    return string


# needs changing:
# so structure becomes {prefix : [s1,
#                   [s2,
#                       [s3, [s4, s4-1]],
#                       [s3-1, [s4, s4-1]]   ],
#                   [s2-1,
#                       [s3, [s4, s4-1]],
#                       [s3-1, [s4, s4-1]]   ],
#     etc!!!!


def gen_4_sentence(prefix_dict, sentence_length):
    """
    generates a random sentence using the prefix
    dictionary

    sentence_length : an integer to determine
                      how many prefixes to use
    """
    string = ""
    string += random.choice(prefix_dict.keys())
    prefix = string
    for i in range(sentence_length):
        suffix = gen_random_word(prefix, prefix_dict)
        prefix = suffix[3]
        for word in suffix:
            string += " " + word
    return string


def main():
    """
    main loop
    """
    filename = "2350.txt"
    text_as_list = read_file(filename)
    #prefix_dict = build_prefix_dict(text_as_list)
    #print gen_sentence(prefix_dict, 100)
    prefix_dict_4 = build_4_prefix(text_as_list)
    print gen_4_sentence(prefix_dict_4, 100)

if __name__ == '__main__':
    main()