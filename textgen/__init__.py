# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

__version__ = '0.1.3'

from textgen.augment.text_augment import TextAugment

from textgen.config.model_args import LanguageGenerationArgs
from textgen.language_generation.language_generation_model import LanguageGenerationModel

from textgen.config.model_args import LanguageModelingArgs
from textgen.language_modeling.language_modeling_model import LanguageModelingModel

from textgen.config.model_args import QuestionAnsweringArgs
from textgen.question_answering.question_answering_model import QuestionAnsweringModel

from textgen.config.model_args import Seq2SeqArgs
from textgen.seq2seq.bart_seq2seq_model import BartSeq2SeqModel
from textgen.seq2seq.seq2seq_model import Seq2SeqModel
from textgen.seq2seq.conv_seq2seq_model import ConvSeq2SeqModel

from textgen.config.model_args import T5Args
from textgen.t5.t5_model import T5Model

from textgen.unsup_generation.tgls_model import TglsModel
