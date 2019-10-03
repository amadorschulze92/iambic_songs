from functions import PoetryParser
import pandas as pd

pp = PoetryParser()

author="taylor swift"
df_ts = pd.read_csv("./Archive/taylor_swift_lyrics.csv")


text_list, meter_list = pp.text_line_parser(df_ts["lyrics"])
syllable_inflection_columns, word_list_column, sonnet_num_list, author_list, polarity_list, subjectivity_list = pp.text_to_df(text_list, meter_list, author)
austen_text_df = pp.create_dataframe(syllable_inflection_columns, word_list_column, sonnet_num_list, author_list, polarity_list, subjectivity_list)

print(austen_text_df.head())
