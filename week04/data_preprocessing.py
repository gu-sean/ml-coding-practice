# -*- coding: utf-8 -*-

# 데이터 준비
from pathlib import Path
import numpy as np
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarball_path = Path("datasets/housing.tpz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()

# 테스트 세트 만들기
from sklearn.model_selection import train_test_split

housing["income_cat"] = pd.cut(housing["median_income"], 
                            bins=[0., 1.5, 3.0, 4.5, 6., np.inf], 
                            labels=[1,2,3,4,5])

strat_train_set, strat_tast_set = train_test_split(
    housing, test_size=0.2, stratify=housing["income_cat"], random_state=42)

for set_ in (strat_train_set, strat_tast_set):
    set_.drop("income_cat", axis=1, inplace=True)
    
"""
* 원본 훈련 세트로 복원하고 타깃을 분리
* 'strat_train_set.drop()'은 지정한 열을 제외한 'strat_train_srt'의 복사복을 만듦
* 'inplace=True'로 지정하지 않은 한 'strat_train_set' 자체를 수정하지 않음
"""

housing = strat_train_set("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

# 데이터 정제
# null 값이 있는 행 확인하기
null_rows_idx = housing.isnull().any(axis=1)
housing.
