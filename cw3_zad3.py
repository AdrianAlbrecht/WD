pdk={"jajka": "sztuki","maka": "kg","olej":"litry","jablka": "sztuki"}
print(pdk)
new_pdk={key for key in pdk if pdk[key]=="sztuki"}
print(new_pdk)