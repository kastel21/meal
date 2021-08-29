import inout
import common

str1 = inout.infilelines[0].strip()
str2 = inout.infilelines[1].strip()

scoring_matrix = common.parse_scoring_matrix(inout.readlines('BLOSUM62.txt'))
indel_penalty = -5

from_row, from_col, to_row, to_col = common.alignment_middle_edge(scoring_matrix, indel_penalty, str1, str2)
inout.output('({}, {}) ({}, {})'.format(from_row, from_col, to_row, to_col))