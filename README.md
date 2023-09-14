# Text Improvement Engine

## Overview:

The Text Improvement Engine is designed to analyze a given text and suggest improvements based on its similarity to a list of standardized phrases. These standardized phrases represent the ideal way certain concepts should be articulated. The goal is to align the input text closer to these standards, ensuring clarity and adherence to specific terminologies or jargons.

## Problem Statement:

Given a text, the challenge was to identify phrases or sentences that could be better articulated using a set of predefined standardized phrases. The objective was not just to find exact matches but to identify semantic similarities, ensuring that the context and meaning of the original text are preserved while making the suggested improvements.

## Solution:

To address this challenge, we employed the following approach:

1. **Semantic Analysis with spaCy**: We utilized the `spaCy` library, which offers pre-trained models for semantic analysis. This allowed us to convert sentences and phrases into vector representations, facilitating the comparison of semantic similarities.

2. **Cosine Similarity**: For each sentence in the input text, we computed its cosine similarity with each standardized phrase. This metric helped us determine how close the meaning of a given sentence is to any of the standardized phrases.

3. **Threshold-based Suggestions**: Based on a predefined similarity threshold, we suggested replacements for sentences or phrases in the input text. If the similarity score exceeded this threshold, the standardized phrase was recommended as a replacement.

## Installation:

1. Install Python 3.
2. Install the required libraries: `pip install spacy`
3. Download the spaCy model: `python -m spacy download en_core_web_md`
4. Run `main.py` to analyze the text.

## Usage:

1. Run `main.py`.
2. Input the text you want to analyze when prompted.
3. The program will display the original text, the suggested replacement, and the similarity score for each suggestion.
4. Review the suggestions and decide which ones to incorporate into your text.

By using the Text Improvement Engine, users can ensure that their text aligns with standardized terminologies, enhancing clarity and professionalism.
