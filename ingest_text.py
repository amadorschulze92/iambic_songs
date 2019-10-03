from functions import *
import pandas as pd
import sys

author="taylor swift"
# df_ts = pd.read_csv("taylor_swift_lyrics.csv", encoding='latin1')
# for dev work use the smaller data set below:
df_ts = pd.read_csv("small_taylor_swift_lyrics.csv", encoding='latin1')


text_list, meter_list = text_line_parser(df_ts["lyric"])
syllable_inflection_columns, word_list_column, sonnet_num_list, author_list, polarity_list, subjectivity_list = text_to_df(text_list, meter_list, author)
austen_text_df = create_dataframe(syllable_inflection_columns, word_list_column, sonnet_num_list, author_list, polarity_list, subjectivity_list)

print(austen_text_df.head())
