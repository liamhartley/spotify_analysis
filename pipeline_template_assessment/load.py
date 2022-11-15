import pandas as pd


def load_data(df_trans: pd.DataFrame) -> None:
    '''
    This function should load the transformed DataFrame into a local or remote location
    :param df_trans: the transformed DataFrame
    :return: None
    '''

    df_trans.to_csv()

    # bonus question: load the file into an S3 bucket on AWS
    # resources: https://stackoverflow.com/questions/38154040/save-dataframe-to-csv-directly-to-s3-python

    return
