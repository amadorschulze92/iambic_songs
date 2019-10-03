from functions import *
import pandas as pd
import sys

my_file = sys.argv[1]
author = sys.argv[2]

df_ts = pd.read_csv(my_file, encoding='latin1')

text_list, meter_list = text_line_parser(df_ts["lyric"])
syllable_inflection_columns, word_list_column, sonnet_num_list, author_list, polarity_list, subjectivity_list = text_to_df(text_list, meter_list, author)
austen_text_df = create_dataframe(syllable_inflection_columns, word_list_column, sonnet_num_list, author_list, polarity_list, subjectivity_list)

print(austen_text_df.head())
