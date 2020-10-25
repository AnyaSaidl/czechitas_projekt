# nactu si zdrojovy soubor a odstranim duplikaty
import pandas

df = pandas.read_csv(
    "realitky1_v3.csv", index_col=0, encoding="utf-8", low_memory=False
)
bez_duplikatu = df.drop_duplicates(subset=['address','living_area', 'price'])

#dfnew= pandas.read_csv(
#    "bez_duplikatu1.csv", index_col=0, encoding="utf-8", low_memory=False)

#df1 = pd.read_csv (r"C:\Digitalni_akademie\projekt\sandbox\bez_duplikatu.csv", index_col=0, encoding="utf-8", low_memory=False
#)
bez_nul = bez_duplikatu.dropna(subset = ['price'])
bez_nul.to_csv("bez_nul.csv")

#nactu si soubor jenom s inzeraty v praze a s kody uj
realitky_praha=pandas.read_csv("realitky_praha.csv", encoding="utf-8", low_memory=False)

# ***************************************************

# vyfiltruju si inzeraty na prodej bytu pouze z cr 
prodej_bytu =  realitky_praha[
    #bez_nul["Country"].str.contains("cz", na=False, case=False)
    #& df["address"].str.contains("praha", na=False, case=False)
    realitky_praha["type"].str.contains("apartment", na=False, case=False)
    & realitky_praha["offer_type"].str.contains("sale", na=False, case=False)
]

# zjistim kolik nabidek na prodej bytu mame
prodej_bytu.info()

# vyexportuju si tabulku prodej bytu praha
prodej_bytu.to_csv("prodej_bytu.csv")

# overim si, ze localuniqeID je vazne PK
df_1 = pandas.read_csv(
    "prodej_bytu.csv", index_col=0, encoding="utf-8", low_memory=False
)
#pocet_1 = df_1.local_unique_id.nunique() #kolik unikátních hodnot je v local_unique_id
#pocet_1_2 = df_1.contract_id.nunique()  # kolik unikatnich hodnot je v contract_id
#print(pocet_1)  # 4856
#print(pocet_1_2)  # 4350 a non-null 4413

# vytisknu si 5 maximalnich a 5 minimalnich hodnot
price_1 = df_1.loc[:,["price"]]
prodej_max10 = price_1.nlargest(10,['price']) #max reálná cena je 79.000.000
prodej_min10 = price_1.nsmallest(10,['price']) #min reálná cena je 1.000.000
print(
    f"10 max hodnot prodeje jsou:{prodej_max10} a 10 min hodnot prodeje jsou: {prodej_min10}."
)

# vytvorim si novy df kde bude pouze cena, plocha,identifikatory a prumer prodej za m2
cena_plocha = df_1.loc[:, [ "local_unique_id", "price", "living_area","kod_zsj_d","lat","lng"]]
cena_plocha["prumer"] = cena_plocha.price / cena_plocha.living_area

#zmena nazvu index column
cena_plocha.index.names=['id']

#zmena datoveho typu
cena_plocha['kod_zsj_d'] = cena_plocha['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
cena_plocha['kod_zsj_d'] = cena_plocha['kod_zsj_d'].apply(lambda x: x.zfill(7))

cena_plocha.info()
cena_plocha.to_csv("prumer_prodej.csv")

print("**************************************************")

# vyfiltruju si inzeraty na pronajem bytu pouze z cr a prahy
pronajem_bytu = realitky_praha[
    #bez_nul["Country"].str.contains("cz", na=False, case=False)
    #& df["address"].str.contains("praha", na=False, case=False)
    realitky_praha["type"].str.contains("apartment", na=False, case=False)
    & realitky_praha["offer_type"].str.contains("rent", na=False, case=False)
]

# zjistim kolik nabidek na pronajem bytu v Praze mame
pronajem_bytu.info()

# vyexportuju si tabulku prodej bytu praha
pronajem_bytu.to_csv("pronajem_bytu.csv")

# overim si, ze localunieID je vazne PK
df_2 = pandas.read_csv(
    "pronajem_bytu.csv", index_col=0, encoding="utf-8", low_memory=False
)
#pocet_2 = df_2.local_unique_id.nunique()
#pocet_2_2 = df_2.contract_id.nunique()  # kolik unikatnich hodnot je v contract_id
#print(pocet_2)  # 8712
#print(pocet_2_2)  # 7591 a 7745 non-null

# vytisknu si 5 maximalnich a 5 minimalnich hodnot
price_2=df_2.loc[:,["price"]]
pronajem_max10 = price_2.nlargest(10, ['price']) #nejvyšší reálná nájem 500.000
pronajem_min10 = price_2.nsmallest(10, ['price']) #nejnižší reálný nájem 3.500 ale plus odstupné
print(
    f"10 max hodnot pronajmu jsou:{pronajem_max10} a 10 min hodnot pronajmu jsou:{pronajem_min10}."
)

# vytvorim si novy df kde bude pouze cena, plocha,identifikatory a prumer pronajmu za m2
cena_plocha_2 = df_2.loc[:, ["local_unique_id", "price", "living_area","kod_zsj_d","lat","lng"]]
cena_plocha_2["prumer"] = cena_plocha_2.price / cena_plocha_2.living_area

#zmena nazvu index column
cena_plocha_2.index.names=['id']

#změna datového typu
cena_plocha_2['kod_zsj_d'] = cena_plocha_2['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
cena_plocha_2['kod_zsj_d'] = cena_plocha_2['kod_zsj_d'].apply(lambda x: x.zfill(7))


cena_plocha_2.info()
cena_plocha_2.to_csv("prumer_pronajem.csv")


#nasteveni limitu pro zobrazovani inzeratu prodeje
prodej_bytu_df= pandas.read_csv(
    "prodej_bytu.csv", index_col=0, encoding="utf-8", low_memory=False
)
limity_prodej=prodej_bytu_df[prodej_bytu_df['price']>=1000000]
limity_prodej.to_csv("limity_prodej.csv")

#nastaveni limitu pro zobrazovani inzeratu pronajmu
pronajem_bytu_df= pandas.read_csv(
    "pronajem_bytu.csv", index_col=0, encoding="utf-8", low_memory=False
)
limity_pronajem=pronajem_bytu_df[(pronajem_bytu_df['price']>=3500) & (pronajem_bytu_df['price']<=500000)]
limity_pronajem.to_csv("limity_pronajem.csv")


#spojime si nabidku prodeje a pronajmu
realitni_trh_praha=[limity_prodej, limity_pronajem]
spojena = pandas.concat(realitni_trh_praha)
spojena = spojena.drop(spojena.columns[[0, 1, 4, 7, 8, 10, 12, 16, 17]], axis=1)
#print(spojena)
spojena.index.names=['id']

#změna datového typu
spojena['kod_zsj_d'] = spojena['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
spojena['kod_zsj_d'] = spojena['kod_zsj_d'].apply(lambda x: x.zfill(7))

spojena.to_csv("inzeraty_prodej_pronajem.csv")
spojena.info()

