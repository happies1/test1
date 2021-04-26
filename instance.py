# 
# @author: Allan
#
from common.sentence import Sentence
class Instance:

    def __init__(self, input: Sentence, output):#输出就是标签
        self.input = input
        self.output = output
        self.elmo_vec = None
        self.word_ids = None
        self.char_ids = None
        self.dep_label_ids = None#代表的具体的依存关系
        self.dep_head_ids = None#存的就是每个词的head
        self.output_ids = None

    def __len__(self):
        return len(self.input)
