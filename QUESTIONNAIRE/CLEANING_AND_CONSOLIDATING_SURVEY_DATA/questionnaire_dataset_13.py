from mapping_scheme_13 import multiple_choice_to_numbers
from mapping_scheme_13 import column_names

def open_and_read_source_file(file_name):
    with open(file_name, encoding='utf-8') as google_form_data:
        answers_source_language = google_form_data.readlines()
    return answers_source_language

def get_and_add_language_key(file_name, answers_source_language):
    language_key = file_name.split('_')[1].split('.')[0]
    answers_source_language = ['"' + language_key + '",' + line for line in answers_source_language]
    return answers_source_language

def create_respondent_ids(dataset, file_name):
    language_key = file_name.split('_')[1].split('.')[0]
    id_counter = 1
    answers_with_id = []
    for line in dataset:
        line = '"' + str(id_counter) + '_' + str(language_key) + '",' + line
        answers_with_id.append(line)
        id_counter += 1
    return answers_with_id

def clean_dataset(dataset):
    clean_answers = ''
    for i in range(len(dataset)):
        respondent = dataset[i].split('",')
        respondent = [answer.replace('"', '').rstrip().lstrip().replace('  ', ' ') for answer in respondent]
        respondent = multiple_choice_to_numbers(respondent, column_names)
        respondent = [answer.lower() for answer in respondent]
        respondent = ['"' + answer + '"' for answer in respondent]
        answers_to_one_string = ','.join(respondent)
        clean_answers = clean_answers + answers_to_one_string + '\n'
    return clean_answers

def compile_multilingual_csv(file_names, table_head):
    table_head = ['"' + name + '"' for name in table_head]
    table_head_one_string = ','.join(table_head)
    with open('LEGO_all_languages.csv', mode='a', encoding='utf-8') as output_csv:
        output_csv.writelines(table_head_one_string + '\n')
    for i in range(len(file_names)):
        print(f'Reading, writing language key, cleaning and adding {file_names[i]} to a compiled dataset.')
        original_answers = open_and_read_source_file(file_names[i])
        answers_with_language_key = get_and_add_language_key(file_names[i], original_answers)
        answers_with_ids = create_respondent_ids(answers_with_language_key, file_names[i])
        clean_data = clean_dataset(answers_with_ids)
        with open('LEGO_all_languages.csv', mode='a', encoding='utf-8') as output_csv:
            output_csv.writelines(clean_data)


questionnaires = ['LEGO_CZ.csv', 'LEGO_ENG.csv', 'LEGO_RU.csv', 'LEGO_ESP.csv']
compile_multilingual_csv(questionnaires, column_names)