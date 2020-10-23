import pandas

#nacte si csv soubor
tabulka_cela=pandas.read_csv("dataset_sreality_2020-10-11_01-35-55-716.csv", encoding="utf-8", low_memory=False)

#vygeneruje informace o tabulce jako n sloupcu,radku, datove typy...
tabulka_cela.info()

#vyberu pouze sloupce co potrebuje pro dalsi ucely
tabulka_export= tabulka_cela.loc[:, ["pageFunctionResult/address","pageFunctionResult/contractId","pageFunctionResult/countryCode", "pageFunctionResult/gpsCoord/lat", "pageFunctionResult/gpsCoord/lon", "pageFunctionResult/gpsCoordType","pageFunctionResult/livingArea", "pageFunctionResult/localUniqueId", "pageFunctionResult/price", "pageFunctionResult/priceCurrency", "pageFunctionResult/title", "pageFunctionResult/type", "pageFunctionResult/offerType", "pageFunctionResult/url"]]

# prejmenuju si headery vsech sloupcu
tabulka_export.rename(columns={"pageFunctionResult/address":"address","pageFunctionResult/contractId":"contract_id","pageFunctionResult/countryCode":"Country", "pageFunctionResult/gpsCoord/lat":"latitude", "pageFunctionResult/gpsCoord/lon":"longitude", "pageFunctionResult/gpsCoordType":"coordinate_type","pageFunctionResult/livingArea":"living_area", "pageFunctionResult/localUniqueId":"local_unique_id", "pageFunctionResult/price":"price", "pageFunctionResult/priceCurrency":"currency", "pageFunctionResult/title":"title", "pageFunctionResult/type":"type", "pageFunctionResult/offerType":"offer_type","pageFunctionResult/url":"url"}, inplace=True)

#vyexportuju finalni tabulku
tabulka_export.to_csv("realitky1_v3.csv")

#overim si, ze mi nezmizela zadna data
tabulka_export.info()
