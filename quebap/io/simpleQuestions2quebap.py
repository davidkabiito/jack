import json
import io

def convert_simpleQuestions_to_quebap(simpleQuestionFile):

    instances = []

    f = io.open(simpleQuestionFile, "r")

    for l in f:
        l = l.strip().split("\t")
        subj, rel, obj, qu  = l

        support = [" ".join([subj, rel])]

        qdict = {
            'question': qu,
            'answers': [obj]
        }
        qset_dict = {
            'support': [{'text': supp} for supp in support],
            'questions': [qdict]
        }

        instances.append(qset_dict)

    corpus_dict = {
        'meta': "simpleQuestions.json",
        'instances': instances
    }

    f.close()

    return corpus_dict


def main():
    # some tests:
    # raw_data = load_cbt_file(path=None, part='valid', mode='NE')
    # instances = split_cbt(raw_data)
    # = parse_cbt_example(instances[0])
    corpus = convert_simpleQuestions_to_quebap("../../quebap/data/SimpleQuestions_v2/annotated_fb_data_train.txt")
    with open("../../quebap/data/simpleQuestions/simpleQuestions_train.json", 'w') as outfile:
        json.dump(corpus, outfile, indent=2)

    outfile.close()

if __name__ == "__main__":
    main()