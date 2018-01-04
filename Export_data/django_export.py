# coding=utf-8
import os

import sys

import datetime
from import_export import resources
import pandas as pd


class Modelnameresources(resources.ModelResource):
    class Meta:
        model = 'Model in your project'


dataset = Modelnameresources().export(queryset='queryset')
df = pd.DataFrame(data=list(dataset), columns=list(dataset._Dataset_headers))
name_csv = 'name.csv'


def _save(csv, df):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    path = sys.path.__getitem__(2) + '/foldername/'
    if not os.path.isdir(path):
        os.mkdir(path)
    cv_path = path + csv
    df.to_csv(cv_path, index=True)
    return cv_path
