# -*- coding: utf-8 -*-

import os


def traverse(f, iterate):
    fs = os.listdir(f)
    file_list = []
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            if f1.endswith('@3x.png'):
                new_file = f1.replace('@3x', '')
                os.rename(tmp_path, os.path.join(f, new_file))
                file_list.append(f1)
        else:
            if iterate:
                traverse(tmp_path)

    return file_list


path = '/Users/salvador/GitLab/govlan_rn/src/assets/images'
print(traverse(path, False))
