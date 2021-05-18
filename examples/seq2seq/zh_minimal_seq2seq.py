# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""

import sys

import pandas as pd
import torch

sys.path.append('../..')
from textgen.seq2seq import Seq2SeqModel

use_cuda = torch.cuda.is_available()
train_data = [
    ["one", "1"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["five", "5"],
    ["six", "6"],
    ["seven", "7"],
    ["eight", "8"],
]

train_df = pd.DataFrame(train_data, columns=["input_text", "target_text"])

eval_data = [
    ["nine", "9"],
    ["zero", "0"],
]

eval_df = pd.DataFrame(eval_data, columns=["input_text", "target_text"])

model_args = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "max_seq_length": 10,
    "train_batch_size": 2,
    "num_train_epochs": 10,
    "save_eval_checkpoints": False,
    "save_model_every_epoch": False,
    "silent": False,
    "evaluate_generated_text": True,
    "evaluate_during_training": False,
    "evaluate_during_training_verbose": False,
    "use_multiprocessing": False,
    "save_best_model": True,
    "max_length": 15,
}

# encoder_type=None, encoder_name=None, decoder_name=None, encoder_decoder_type=None, encoder_decoder_name=None,
model = Seq2SeqModel("bert", "bert-base-chinese", "bert-base-chinese", args=model_args, use_cuda=use_cuda, )


def count_matches(labels, preds):
    print(labels)
    print(preds)
    return sum([1 if label == pred else 0 for label, pred in zip(labels, preds)])


model.train_model(train_df, eval_data=eval_df, matches=count_matches)

print(model.eval_model(eval_df, matches=count_matches))

print(model.predict(["four", "five"]))
