from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    arq = instance.queue
    ret = list()
    for path in arq:
        line = list()
        text = txt_importer(path)
        for i in range(len(text)):
            if word.lower() in text[i].lower():
                line.append({"linha": i + 1})
        if len(line) == 0:
            return line
        ret.append(
            {
                'palavra': word,
                'arquivo': path,
                'ocorrencias': line
            }
        )
    return ret



def search_by_word(word, instance):
    """Aqui irá sua implementação"""
