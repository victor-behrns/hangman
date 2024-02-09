def anonymiserer(ord:str, ritikge_bokstaver:list[str]):
# Loop igjennom bokstaver i hvert ord
# Hvis bokstaven finnes i riktige_bokstaver så skal vi returner bokstaven, hvis ikke. _
    return_ord = ""
    for bokstav in ord:
        if bokstav in ritikge_bokstaver:
            return_ord = return_ord + bokstav 
        else:
            return_ord = return_ord + "_"
    return return_ord