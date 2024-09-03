#!/usr/bin/python

import math
import random
from collections import defaultdict
from util import *
from typing import Any, Dict, Tuple, List, Callable

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]


def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """

    dict_x = defaultdict(int)
    for word in x.split():
        dict_x[word] += 1
    return dict_x


def learnPredictor(trainExamples: List[Tuple[Any, int]], validationExamples: List[Tuple[Any, int]],
                   featureExtractor: Callable[[str], FeatureVector], numEpochs: int, alpha: float) -> WeightVector:
    """
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numEpochs|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement gradient descent.
    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and validationExamples
    to see how you're doing as you learn after each epoch. Note also that the 
    identity function may be used as the featureExtractor function during testing.
    """
    weights = {}  # the weight vector

    def predictor(str_in_examples):
        feature_vector_predictor = featureExtractor(str_in_examples)
        k_predictor = dotProduct(weights, feature_vector_predictor)
        return 1 if k_predictor >= 0 else -1

    for epoch in range(numEpochs):
        cost = 0
        for x, y in trainExamples:
            feature_vector = featureExtractor(x)
            y = 1 if y == 1 else 0
            k = dotProduct(weights, feature_vector)
            h = 1 / (1 + math.exp(-k))
            loss = -(y * math.log(h) + (1 - y) * math.log(1 - h))
            cost += loss
            increment(weights, -alpha * (h - y), feature_vector)

        print('Training Error: (' + str(epoch) + ' epoch): ' + str(evaluatePredictor(trainExamples, predictor)))
        print('Validation Error: (' + str(epoch) + ' epoch): ' + str(evaluatePredictor(validationExamples, predictor)))

    return weights


def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    """
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    """
    random.seed(42)

    def generateExample() -> Tuple[Dict[str, int], int]:
        """
        Return a single example (phi(x), y).
        phi(x) should be a dict whose keys are a subset of the keys in weights
        and values are their word occurrence.
        y should be 1 or -1 as classified by the weight vector.
        Note that the weight vector can be arbitrary during testing.
        """

        len_phi = random.randint(1, len(weights))
        keys = random.choices(list(weights.keys()), k=len_phi)
        phi = extractWordFeatures(' '.join(keys))
        y = 1 if dotProduct(phi, weights) >= 0 else -1

        return phi, y

    return [generateExample() for _ in range(numExamples)]


def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    """
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    """

    def extract(x: str) -> Dict[str, int]:
        dict_Character = defaultdict(int)
        x = ''.join(x.split())
        for i in range(len(x) - n + 1):
            dict_Character[x[i:i + n]] += 1
        return dict_Character

    return extract


def testValuesOfN(n: int):
    """
    Use this code to test different values of n for extractCharacterFeatures
    This code is exclusively for testing.
    Your full written solution for this problem must be in sentiment.pdf.
    """
    trainExamples = readExamples('polarity.train')
    validationExamples = readExamples('polarity.dev')
    featureExtractor = extractCharacterFeatures(n)
    weights = learnPredictor(trainExamples, validationExamples, featureExtractor, numEpochs=20, alpha=0.01)
    outputWeights(weights, 'weights')
    outputErrorAnalysis(validationExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
    trainError = evaluatePredictor(trainExamples,
                                   lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    validationError = evaluatePredictor(validationExamples,
                                        lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    print(("Official: train error = %s, validation error = %s" % (trainError, validationError)))
