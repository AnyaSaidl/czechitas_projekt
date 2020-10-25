import pandas as pd
realitky=pd.read_csv("Realitni_data_sregiony.csv",encoding="utf-8", low_memory=False)
zsjd=pd.read_csv("zsj_d_dwh.csv",encoding="utf-8", low_memory=False)
obce=pd.read_csv("cast_obec_dwh.csv",encoding="utf-8", low_memory=False)

#osekani sloupcu zdrojovych tabulek
zsjd_kod= zsjd.loc[:, ["kod_zsj_d","kod_cast_obec"]]
obce_kod=obce.loc[:, ["kod_cast_obec","upper_name"]]

#inner join reaitek kodu zsjd
realitky_zsjd=pd.merge(realitky,zsjd_kod,on='kod_zsj_d')
#realitky_zsjd.to_csv("realitky_zsjd.csv")

#inner join s obcemi
realitky_uj=pd.merge(realitky_zsjd,obce_kod,on='kod_cast_obec' )
#realitky_uj.to_csv("realitky_uj.csv")

#vyfiltrujeme pouze Prahu
realitky_praha = realitky_uj[realitky_uj.apply(lambda row: row['upper_name'].lower() == 'praha', axis=1)]

#změna datového typu
realitky_praha['kod_zsj_d'] = realitky_praha['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
realitky_praha['kod_zsj_d'] = realitky_praha['kod_zsj_d'].apply(lambda x: x.zfill(7))

#změna datového typu u ceny
realitky_praha['price'] = realitky_praha['price'].astype(int)

realitky_praha.to_csv("realitky_praha.csv")
realitky_praha.info()