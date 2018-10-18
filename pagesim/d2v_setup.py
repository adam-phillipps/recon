import itertools
import logging
import os
import sys
import argparse
import pdb
import gensim.downloader as api
from numpy import seterr
# from gensim.utils import save_as_line_sentence
from gensim.corpora import MmCorpus, Dictionary
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.parsing.preprocessing import preprocess_string

"""
Class that sets up the script arguments parser


USAGE: %(program)s
            --corpus-file <path to corpus, either path to save to or path to load from>
            [--raw-file <path/to/documents>]
            [--raw-url <remote name of preprocessed corpus for gensim.downloader>]
            [--vec-size <int>]
            [--threads <int>]
            [--model <path>]
            [--workers <int>]
Trains a neural embedding model on text file CORPUS.
Parameters essentially reproduce those used by the original C tool
(see https://code.google.com/archive/p/word2vec/).

Parameters for training:
    --raw-file <file>
            Use text data from <file> to train the model
    --raw-url <file>
            Use <file> to save the resulting word vectors / word clusters
    --vec-size <int>
            Set size of word vectors; default is 500
    --corpus-file <file>
            processed corpus, ready for training
    --threads <int>
            Use <int> threads (default 3)
    --model <file>
            Path to serialize model at
    --epoch <int>
            Run more training iterations (default 5)
    --workers <int>
            Run in parallel.  Use 2 to 16 for regular machines (CPU)

"""
def gather_command_line_args(parser):
    parser.add_argument(
        "--raw-file",
        help="Use text data from file TRAIN to train the model"
             " This will be your raw-ish corpus")
    parser.add_argument(
        "--raw-url",
        default=RAW_CORPUS_URL,
        help="Get the raw-ish corpus, using the `gensim.downloader`"
             " API this will be your raw-ish corpus")
    parser.add_argument(
        "--corpus-file",
        required=True,
        help="This is the file that will be used to interact"
             " with models.  It is the file that is created from"
             " the processing steps used on a raw-ish corpus."
             " These files are typically used in training.")
    parser.add_argument(
        "--model",
        required=True,
        help="The path to save or load your model")
    parser.add_argument(
        "--vec-size",
        type=int,
        default=DEFAULT_VEC_SIZE,
        help="Set size of document vectors; default is:"
             " {}".format(DEFAULT_VEC_SIZE))
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of workers to distribute jobs to.  This number has a lot"
             " to do with the number of CPUs you're running.")
    parser.add_argument(
        "--dictionary",
        help="Mapping between words and word ids and/or documents with doc ids")
    parser.add_argument(
        "--threads",
        type=int,
        default=3,
        help="Use THREADS threads (default 3)")
    parser.add_argument(
        "--epoch",
        type=int,
        default=5,
        help="Run more training iterations (default 5)")

    return parser.parse_args()

"""
From a raw corpus, iterate through each article, do some basic preprocessing and
yield each sentence.
"""
class TaggedDocs():
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        for i, doc in enumerate(api.load(self.file)):
            yield TaggedDocument(preprocess_string(doc), [i])

def save_as_tagged_docs(corpus_path, docs):
    corpus = MmCorpus(docs)
    MmCorpus.serialize(corpus_path, corpus)
"""
Example of the meat of this file

       raw_corpus = api.load(args.raw_url)
       save_as_line_sentence(create_iterable_corpus(raw_corpus), args.corpus_file)
       model = Doc2Vec(corpus_file=args.corpus_file,
                       workers=args.workers,
                       epoch=args.epoch,
                       vector_size=args.vec_size)
       model.save(args.model)
       model.infer(["some", "text", "from", "the", "body", "of", "some", "page", "from", "the", "internet"])
"""
if __name__ == "__main__":
    DEFAULT_VEC_SIZE = 500
    # RAW_CORPUS_URL = 'text8'
    RAW_CORPUS_URL = 'wiki-english-20171001'
    # RAW_CORPUS_URL = 'wiki-en-20171001.txt'
    RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "results"))
    # RESULTS_DIR = "s3://recon-artifacts"
    _curr_path = os.path.abspath(os.path.dirname(__file__))
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
    logger.info("running %s", " ".join(sys.argv))

    args = gather_command_line_args(argparse.ArgumentParser())
    seterr(all='raise') # don't ignore numpy errors

    if not os.path.exists(os.path.join(_curr_path, args.corpus_file)):
        if args.raw_url:
            logger.info("Downloading raw corpus file for: {}".format(args.raw_url))
            raw_corpus = args.raw_url
            logger.info("Download complete")
        elif args.raw_file:
            logger.info("Loading corpus from: {}".format(args.raw_file))
            raw_corpus = args.raw_file
            logger.info("Load complete")

        logger.info("Saving corpus to disk")
    else:
        raw_corpus = args.corpus_file

    if os.path.exists(os.path.join(os.path.dirname(__file__), args.model)):
        logger.info("Loading existing model from: {}".format(args.model))
        model = Doc2Vec.load(args.model)
    else:
        logger.info("Creating new Doc2Vec model from corpus_file: {}".format(args.corpus_file))
        model = Doc2Vec(corpus_file=raw_corpus,
                        workers=args.workers,
                        epoch=args.epoch,
                        vector_size=args.vec_size)
        # dictionary=Dictionary.load_from_text(args.dictionary),
        # model.save(args.model)
        model.save(args.model)

    pdb.set_trace()
    vocab = model.build_vocab(documents=TaggedDocs(raw_corpus))
    pdb.set_trace()
    model.train(corpus_file=args.corpus_file)

    print(model)

