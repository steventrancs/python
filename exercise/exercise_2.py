# use command python "$@" to input parmeter is string
import sys

def sort_sentence(sentence):
    words = sentence.split(' ')
    print sorted(words)
sort_sentence(sys.argv[1:])