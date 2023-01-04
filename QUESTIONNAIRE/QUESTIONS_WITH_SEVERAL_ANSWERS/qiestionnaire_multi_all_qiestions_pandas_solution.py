import pandas
import json

INPUT_FILE = 'LEGO_all_languages.csv'

QUESTIONS_LIST = [
"6. Pro koho byste koupil/a LEGO?",
"8. Co Vás omezuje / brání při nákupu LEGO (max. 3)?",
"10. Co nejvíc ovlivňuje výběr setu (max. 3)?",
"11. Vyberte 3 nejoblíbenější témata (max. 3)"]

with open('mapping_scheme.json', encoding='utf-8') as file_to_read:
    answers_direct_mapping = json.load(file_to_read)

def creating_reverse_mapping_to_text(question):
    possible_answers_list = answers_direct_mapping['CZ'][question]
    possible_answers_list_swapped = dict((value,key) for key,value in possible_answers_list.items())
    return possible_answers_list_swapped

def creating_dataframe_pandas():
    responses_df = pandas.read_csv(INPUT_FILE)
    responses_df = responses_df.set_index("Respondent_ID")
    return responses_df

def stacking_answers(question, responses_df):
    answers_split = responses_df[question].str.split(';', expand=True)
    total_answers_count = answers_split.stack().value_counts()
    total_answers_count = total_answers_count.reset_index()
    return total_answers_count

def creating_pandas_answers_count_dataframe(total_answers_count):
    total_answers_count_df = pandas.DataFrame(total_answers_count)
    total_answers_count_df.columns = ['answer_number','total_count']
    total_answers_count_df['answer_number'] = total_answers_count_df['answer_number'].astype(int)
    print( total_answers_count_df)
    return total_answers_count_df

def adding_text_answer_to_number(count_of_answers_total, possible_answers_list_swapped):
    count_of_answers_total['answer_text'] = count_of_answers_total['answer_number'].map(possible_answers_list_swapped)
    column_names_swap = ['answer_number', 'answer_text', 'total_count']
    count_of_answers_final = count_of_answers_total.reindex(columns=column_names_swap)
    print(count_of_answers_final)
    return count_of_answers_final

def write_full_data_to_csv(question_number, answers_with_text_count_final):
    answers_with_text_count_final.to_csv(question_number + '_total_count_with_text.csv', index= False)

responses_df = creating_dataframe_pandas()

for i in range(len(QUESTIONS_LIST)):
    question = QUESTIONS_LIST[i]
    print(question)
    question_number = question.split('.')[0]
    print(responses_df[question])
    reverse_mapping_for_question = creating_reverse_mapping_to_text(question)
    stacked_answers = stacking_answers(question, responses_df)
    number_and_count = creating_pandas_answers_count_dataframe(stacked_answers)
    data_with_new_text_column = adding_text_answer_to_number(number_and_count, reverse_mapping_for_question)
    write_full_data_to_csv(question_number, data_with_new_text_column)