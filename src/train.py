import ourTokenizer
import os
import naiveBayes


# This function gets the full paths for each positive and negative review
#
# Args:
#     None
#
# Returns:
#     neg_paths - the full path to each negative review
#     pos_paths - the full path to each positive review
def get_training_filepaths():
    neg_paths = []
    pos_paths = []
    root_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(os.path.abspath(root_dir))
    neg_dir = os.path.join(parent_dir, "Datasets/aclImdb/train/neg/")
    pos_dir = os.path.join(parent_dir, "Datasets/aclImdb/train/pos/")

    for dirName, subdirList, fileList in os.walk(neg_dir):
        for fname in fileList:
            neg_paths.append(os.path.join(neg_dir, fname))

    for dirName, subdirList, fileList in os.walk(pos_dir):
        for fname in fileList:
            pos_paths.append(os.path.join(pos_dir, fname))

    return neg_paths, pos_paths


# This function tokenizes negative and positive files and returns the tokenized
# review with a "pos" or "neg" marker
#
# Args:
#     neg_fnames - the paths of the negative reviews
#     pos_fnames - the paths of the positive reviews
#
# Returns:
#     neg_reviews - the tokenized and marked negative reviews
#     pos_reviews - the tokenized and marked positive reviews
def process_files(neg_fnames, pos_fnames):
    neg_reviews = []
    for file in neg_fnames:
        lines = tokenize.readFile(file)
        review = tokenize.tokenize_file(lines)
        neg_reviews.append([review, "neg"])

    pos_reviews = []
    for file in pos_fnames:
        lines = tokenize.readFile(file)
        review = tokenize.tokenize_file(lines)
        pos_reviews.append([review, "pos"])

    return neg_reviews, pos_reviews


def main():
    # Retrieving and processing the training data
    neg_fnames, pos_fnames = get_training_filepaths()
    neg_reviews, pos_reviews = process_files(neg_fnames, pos_fnames)
    print("done processing files")


#    reviews = [neg_reviews, pos_reviews]

#    naiveBayes.naiveBayes(reviews)

#if __name__ == '__main__':
#    main()
