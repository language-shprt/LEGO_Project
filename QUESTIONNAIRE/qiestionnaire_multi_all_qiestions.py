import pandas
import json

INPUT_FILE = 'LEGO_all_languages.csv'

QUESTIONS_LIST = [
"6. Pro koho byste koupil/a LEGO?",
"8. Co Vás omezuje / brání při nákupu LEGO (max. 3)?",
"10. Co nejvíc ovlivňuje výběr setu (max. 3)?",
"11. Vyberte 3 nejoblíbenější témata (max. 3)"]

# Preparing keys to do reverse mapping
with open('mapping_scheme.json', encoding='utf-8') as file_to_read:
    answers_direct_mapping = json.load(file_to_read)

def creating_reverse_mapping_to_text(question):
    possible_answers_list = answers_direct_mapping['CZ'][question]
    possible_answers_list_swapped = dict((value,key) for key,value in possible_answers_list.items())
    return possible_answers_list_swapped

def creating_dataframe_pandas():
    responses_df = pandas.read_csv(INPUT_FILE)
    responses_df = responses_df.set_index("Respondent_ID") # nastaveni indexu jako Respondent_ID
    return responses_df

def stacking_answers(question, responses_df):
    answers_split = responses_df[question].str.split(';', expand=True)
    total_answers_count = answers_split.stack().value_counts()
    return total_answers_count

def creating_pandas_series(total_answers_count):
    total_answers_count_series = pandas.Series(total_answers_count)
    print(total_answers_count_series)
    return total_answers_count_series

# number of the answer and total count
def converting_series_to_csv_and_reading_back(subject, total_answers_count_series): 
    total_answers_count_series.to_csv(subject +'.csv')
    with open(subject +'.csv', encoding='utf-8') as input_data:
        count_of_answers_total = input_data.readlines()
    return count_of_answers_total 

#based on the mapping scheme
def adding_text_answer_to_number(count_of_answers_total,possible_answers_list_swapped):
    count_of_answers_total = [answer_count_combination.split(',') for answer_count_combination in count_of_answers_total]
    count_of_answers_total = count_of_answers_total[1:]
    answers_with_text_count_final = ['mapping_number\t', 'text_answer\t', 'total_count\n']
    for i in range(len(count_of_answers_total)):
        answer_number = int(count_of_answers_total[i][0])
        if int(answer_number) in possible_answers_list_swapped:
            count_of_answers_total[i].append(possible_answers_list_swapped[answer_number])
            answer = count_of_answers_total[i]
            mapping_number = answer[0]
            total_count = answer[1]
            name = answer[2]
            answer = '\t'.join([mapping_number, name, total_count])
            answers_with_text_count_final.append(answer)

    print(answers_with_text_count_final)
    return answers_with_text_count_final

def write_full_data_to_csv(question_number, answers_with_text_count_final): #mapping number, text of the anwer, total count
    with open(question_number + '_total_count_with_text.csv', mode='w', encoding='utf-8') as output:
        output.writelines(answers_with_text_count_final)

responses_df = creating_dataframe_pandas()

for i in range(len(QUESTIONS_LIST)):
    question = QUESTIONS_LIST[i]
    print(question)
    question_number = question.split('.')[0]
    print(responses_df[question])
    reverse_mapping_for_question = creating_reverse_mapping_to_text(question)
    stacked_answers = stacking_answers(question, responses_df)
    question_series = creating_pandas_series(stacked_answers)
    number_and_count = converting_series_to_csv_and_reading_back(question_number, question_series)
    data_with_new_text_column = adding_text_answer_to_number(number_and_count, reverse_mapping_for_question)
    write_full_data_to_csv(question_number, data_with_new_text_column)