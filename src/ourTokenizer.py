import sys
import re


# Function to create an array of lines in a filename
#
# Args:
#     filename - name of the file to be read
#
# Returns:
#    lines - the array of lines
def readFile(filename):
    with open(filename) as f:
        lines = f.read().lower().splitlines()

    return lines


# Function to tokenize an array of lines in a file
#
# Args:
#    lines - array of lines in a file
#
# Returns:
#    None
def tokenize_file(lines):
    stripped_words = []
    filtered_words = []

    word_filter = ["br", "s", "t", "the", "it", "a", "of", "to", "is", "i", "in", "this", "that", "this", "that", "was", "and", "for", "on", "you", "he", "she", "are", "have", "be", "one", "at"]
    # re_words = "(?=\S*[\'-])([A-Za-z'-]+)|[A-Za-z]+|!|\?)" # Regex to match words, !, or ?
    re_words = re.compile(r'(?=\S*[\-])[A-Za-z\-]+[A-Za-z]+|!|\?')
    for line in lines:
        stripped_words += re.findall(re_words, line)
    filtered_words = [word for word in stripped_words if word not in word_filter]

    return filtered_words


def main():
    lines = readFile(sys.argv[1])
    tokenize_file(lines)


if __name__ == '__main__':
    main()
