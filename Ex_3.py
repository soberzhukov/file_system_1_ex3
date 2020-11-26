def main(list):
    new_content_doc(list, 'new_doc.txt')


def lines_sum(document):
    with open(document, encoding='utf8') as f:
        sum = 0
        for line in f:
            sum += 1
        return sum


def dict_doc(list_doc):
    dict = {}
    for document in list_doc:
        dict[document] = lines_sum(document)
    return dict



def length_comparison(list): # возвращает список файлов в правильном порядке
    dict = dict_doc(list)
    list_doc = []
    list_lines_sum = [lines_sum for lines_sum in dict.values()]
    list_lines_sum.sort()
    for line_sum in list_lines_sum:
        for document in dict:
            if dict[document] == line_sum and document not in list_doc:
                list_doc.append(document)
    return list_doc


length_comparison(dict_doc(['1.txt','2.txt','3.txt'])) # список в правильном порядке

def new_content_doc(list, new_doc):
    fix_list = length_comparison(list)
    number = 0
    content_new = ''
    for document in fix_list:
        with open(document, encoding='utf8') as f:
            number += 1
            content = f'{document}\n{number}\n{f.read()}\n'
        content_new += content
    with open(new_doc,'w', encoding='utf8') as f:
        f.write(content_new)




main(['1.txt','2.txt','3.txt'])