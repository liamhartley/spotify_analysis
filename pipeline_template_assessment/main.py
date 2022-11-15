from pipeline_template_assessment import extract, transform, load

if __name__ == '__main__':
    df_raw = extract.extract_data_from_source(filepath='pipeline_template/data/rapcaviar_raw.csv')
    df_trans = transform.transform_data(df=df_raw)
    load.load_data(df_trans=df_trans)
