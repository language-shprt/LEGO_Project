import json
import re

with open('mapping_scheme.json', encoding='utf-8') as file_to_read:
    answers_direct_mapping = json.load(file_to_read)

column_names = [
'Respondent_ID',
'LangKey',
'Timestamp',
'1. V jakém městě bydlíte?',
'2. V jakém státu bydlíte?',
'3. Vaše pohlaví',
'4. Váš věk',
'5. Jak často si kupujete / dostáváte nové sety LEGO?',
'6. Pro koho byste koupil/a LEGO?',
'7. Myslíte si, že LEGO je dobrý dárek k Vánocům?',
'8. Co Vás omezuje / brání při nákupu LEGO (max. 3)?',
'9. Maximální cenová hranice za set pro vás je…',
'10. Co nejvíc ovlivňuje výběr setu (max. 3)?',
'11. Vyberte 3 nejoblíbenější témata (max. 3)',
'12. Kolikrát v průměru rozebíráte a poskládáte jeden set LEGO?',
'13. Zkusil jste aspoň jednou z koustek LEGO postavit něco svého?',
'14. Co děláte pokud se nějaká kostka ztratí?',
'15. Využíval/a jste někdy standardní “spare parts” (náhradní kostky), které LEGO dává do nového setu?',
'16. Přemýšlel/a jste někdy o nákupu LEGO setu za účelem investice?']

# https://www.fileformat.info/info/charset/UTF-8/list.htm
# ěščřžýáíéóúůďťňĎŇŤŠČŘŽÝÁÍÉÚŮĚÓ
other_letters_to_latin = {
        #Russian
        u"\u0401": u'YO',
        u"\u0410": u'A',
        u"\u0411": u'B',
        u"\u0412": u'V',
        u"\u0413": u'G',
        u"\u0414": u'D',
        u"\u0415": u'E',
        u"\u0416": u'ZH',
        u"\u0417": u'Z',
        u"\u0418": u'I',
        u"\u0419": u'I',
        u"\u041a": u'K',
        u"\u041b": u'L',
        u"\u041c": u'M',
        u"\u041d": u'N',
        u"\u041e": u'O',
        u"\u041f": u'P',
        u"\u0420": u'R',
        u"\u0421": u'S',
        u"\u0422": u'T',
        u"\u0423": u'U',
        u"\u0424": u'F',
        u"\u0425": u'H',
        u"\u0426": u'TS',
        u"\u0427": u'CH',
        u"\u0428": u'SH',
        u"\u0429": u'SCH',
        #u"\u042a": u"'",
        u"\u042a": '',
        u"\u042b": u'I',
        #u"\u042c": u"'",
        u"\u042c": '',
        u"\u042d": u'E',
        u"\u042e": u'YU',
        u"\u042f": u'YA',

        u"\u0430": u'a',
        u"\u0431": u'b',
        u"\u0432": u'v',
        u"\u0433": u'g',
        u"\u0434": u'd',
        u"\u0435": u'e',
        u"\u0436": u'zh',
        u"\u0437": u'z',
        u"\u0438": u'i',
        u"\u0439": u'i',
        u"\u043a": u'k',
        u"\u043b": u'l',
        u"\u043c": u'm',
        u"\u043d": u'n',
        u"\u043e": u'o',
        u"\u043f": u'p',
        u"\u0440": u'r',
        u"\u0441": u's',
        u"\u0442": u't',
        u"\u0443": u'u',
        u"\u0444": u'f',
        u"\u0445": u'h',
        u"\u0446": u'ts',
        u"\u0447": u'ch',
        u"\u0448": u'sh',
        u"\u0449": u'sch',
        #u"\u044a": u"'",
        u"\u044a": '',
        u"\u044b": u'i',
        #u"\u044c": u"'",
        u"\u044c": '',
        u"\u044d": u'e',
        u"\u044e": u'yu',
        u"\u044f": u'ya',
        u"\u0451": u'yo',

        #Czech
        u"\u00C1": u'A', #Á
        u"\u00C9": u'E', #É
        u"\u011A": u'E', #Ě
        u"\u00D3": u'O', #Ó
        u"\u00CD": u'I', #Í
        u"\u010E": u'D', #Ď
        u"\u0147": u'N', #Ň
        u"\u0164": u'T', #Ť
        u"\u0160": u'SH',#Š
        u"\u010C": u'CH',#Č
        u"\u0158": u'R', #Ř
        u"\u017D": u'ZH',#Ž
        u"\u00DD": u'Y', #Ý
        u"\u00DA": u'U', #Ú
        u"\u016E": u'U', #Ů

        u"\u011B": u'e', #ě
        u"\u0161": u'sh', #š
        u"\u010D": u'ch', #č
        u"\u0159": u'r', #ř
        u"\u017E": u'zh', #ž
        u"\u00FD": u'y', #ý
        u"\u00E1": u'a', #á
        u"\u00ED": u'i', #í
        u"\u00E9": u'e', #é
        u"\u00F3": u'o', #ó
        u"\u00FA": u'u', #ú
        u"\u016F": u'u', #ů
        u"\u010F": u'd', #ď
        u"\u0165": u't', #ť
        u"\u0148": u'n', #ň
        
        # Polish
        u"\u015B": u's', #ś
        u"\u015A": u'S', #ś
        u"\u0107": u'c', #ć
        u"\u0106": u'C', #ć
        u"\u0144": u'n', #ń
        u"\u0143": u'N'  #Ń
    }

cities_groups = {
    'prague': 'Praha',
    'praga': 'Praha',
    'moscow': 'Moskva'}

def multiple_choice_to_numbers(respondent, column_names):
    language_key = respondent[1]
    mapped_answers = []
    for i in range(len(respondent)):
        respondent[i] = respondent[i].split(';')
        answer = respondent[i]
        mapped_answers_for_the_question = []
        for j in range(len(answer)):

            if i == column_names.index('1. V jakém městě bydlíte?'): # index 3
                pattern_regex = re.compile(r"[ ńśćěščřžýáíéóúůďťňĎŇŤŠČŘŽÝÁÍÉÚŮĚÓA-Za-zА-Яа-я-]+")
                if re.fullmatch(pattern_regex, answer[j]):
                    print(answer[j])
                    city_to_latin = ''
                    for letter in answer[j]:
                        if letter in other_letters_to_latin:
                            letter = other_letters_to_latin[letter]
                            city_to_latin = city_to_latin + letter
                        else:
                            city_to_latin = city_to_latin + letter
                    answer[j] = city_to_latin
                    print(answer[j])
                else:
                    answer[j] = 'NULL'

                if answer[j].lower() in cities_groups:
                    answer[j] = cities_groups[answer[j].lower()]
                    print(answer[j])

            try:
                answer_to_number = answers_direct_mapping[language_key][column_names[i]][answer[j]]
                mapped_answers_for_the_question.append(str(answer_to_number))
            except:
                try:
                    written_answers = {}
                    written_answer = answers_direct_mapping[language_key][column_names[i]]['Jiné']
                    mapped_answers_for_the_question.append(str(written_answer))
                    written_answers[column_names[i]] = answer[j]
                    with open('LEGO_free_answers.csv', mode='a', encoding='utf-8') as output_csv_other_answers:
                        json.dump(written_answers, output_csv_other_answers, indent=2, ensure_ascii=False)
                except:
                    mapped_answers_for_the_question.append(answer[j])
        respondent[i] = ';'.join(mapped_answers_for_the_question)

    return respondent