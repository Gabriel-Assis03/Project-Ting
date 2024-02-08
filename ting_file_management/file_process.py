from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for ins in instance.queue:
        if path_file == ins:
            return None
    text = txt_importer(path_file)
    if text is None:
        return None
    ret = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }
    instance.enqueue(path_file)
    print(ret)
    

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
