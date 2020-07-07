from os.path import join
from codecs import open

#自己完成的
def build_c(split, make_vocab=True, data_dir="./ResumeNER"):
    assert split in ['train', 'dev', 'test']

    with open(join(data_dir, split + ".txt"), 'r', encoding="utf8") as f1:
        f1 = f1.readlines()
    with open(join(data_dir, split + "-lable.txt"), 'r', encoding="utf8") as f2:
        f2 = f2.readlines()
    word_lists = [i.strip('\n').split(' ') for i in f1]
    tag_lists = [j.strip('\n').split(' ') for j in f2]

    for n in range(len(word_lists)):
        if '' in word_lists[n]:
            word_lists[n].remove("")

    if make_vocab:
        word2id = build_map(word_lists)
        tag2id = build_map(tag_lists)
        return word_lists, tag_lists, word2id, tag2id
    else:
        return word_lists, tag_lists


def build_corpus(split, make_vocab=True, data_dir="./ResumeNER"):
    """读取数据"""
    assert split in ['train', 'dev', 'test']

    word_lists = []
    tag_lists = []
    with open(join(data_dir, split + ".char.bmes"), 'r', encoding='utf-8') as f:
        word_list = []
        tag_list = []
        for line in f:
            if line != '\n':
                word, tag = line.strip('\n').split()
                word_list.append(word)
                tag_list.append(tag)
            else:
                word_lists.append(word_list)
                tag_lists.append(tag_list)
                word_list = []
                tag_list = []

    # 如果make_vocab为True，还需要返回word2id和tag2id
    if make_vocab:
        word2id = build_map(word_lists)
        tag2id = build_map(tag_lists)
        return word_lists, tag_lists, word2id, tag2id
    else:
        return word_lists, tag_lists


def build_map(lists):
    maps = {}
    for list_ in lists:
        for e in list_:
            if e not in maps:
                maps[e] = len(maps)

    return maps
