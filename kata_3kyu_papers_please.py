class Inspector:

    # Class Variables are defined here. Only one occurrence of each of these
    # variables per class, no matter how many instances you have.
    # This allows us to retain data across calls to the different methods in the class.
    
    entrants_require_passport = False
    citizens_of_Arstotzka_require_ID_card = False
    foreigners_require_access_permit = False
    workers_require_work_pass = False
    allow_citizens_of = set() # keeps track of nations from which citizens are allowed enter. Any citizen from a nation not on this list is banned
    
    Arstotzka_required_vaccination_set = set()
    Antegria_required_vaccination_set = set()
    Impor_required_vaccination_set = set()
    Kolechia_required_vaccination_set = set()
    Obristan_required_vaccination_set = set()
    Republia_required_vaccination_set = set()
    UnitedFederation_required_vaccination_set = set()
    
    todays_wanted_criminal = ""


#####################
# RECEIVE BULLETIN METHOD:
#####################
    def receive_bulletin(self,bulletin):
        print("receive_bulletin method called...")
        print("bulletin:",bulletin)

        Inspector.todays_wanted_criminal = "" #re-initialise this on a daily basis
            
        daily_orders = bulletin.split("\n") # bulletin (input param) is a string. Consists of line-breaks to separate out daily orders. Split() the bulletin string
                                            # on line-break (\n) to create a LIST of individual orders that we can then iterate through
        for order in daily_orders:
        
            print("*** order: ***",order)
        
            if  order == "Entrants require passport":
                print("Entrants will require passport from today")
                Inspector.entrants_require_passport = True
                
            if  order == "Citizens of Arstotzka require ID card":
                Inspector.citizens_of_Arstotzka_require_ID_card = True
            
            if  "Allow citizens of " in order:                          # this order will be in format of "Allow citizens of country1, country2, country3" so isolate each country
                substr_order = order.replace("Allow citizens of ", "")  # ...by removing the first bit of the string...
                substr_order = substr_order.replace(" ","")             # ...remove inner spaces of any country as well as spaces after the commas...
                print("allowing citizens of...",substr_order)
                list_of_countries = substr_order.split(",")             # ...then create a list containing each country to be processed as elements of that list...
                for country in list_of_countries:
                    (Inspector.allow_citizens_of).add(country)          # ...and add the countries in this list to the SET of nations from which citizens may enter
                print(Inspector.allow_citizens_of)

            if  "Deny citizens of " in order:
                substr_order = order.replace("Deny citizens of ", "")   # Similar to Allow...
                substr_order = substr_order.replace(" ","")
                print("denying citizens of...",substr_order)
                list_of_countries = substr_order.split(",")
                for country in list_of_countries:
                    (Inspector.allow_citizens_of).remove(country)       # ...but instead nations are removed from the SET if citizens of those nations are to be denied entry
                print(Inspector.allow_citizens_of)

            
            if  "Wanted by the State" in order:
                substr_order = order.replace("Wanted by the State: ","")  # Order contains name of wanted person in "FirstName SecondName" format so we re-format
                space_char = substr_order.index(" ")                      # to "Secondname, Firstname" in order to match the format on incoming documents
                Inspector.todays_wanted_criminal = substr_order[space_char+1:] + ", " + substr_order[:space_char]
                print("Wanted by the state TODAY! = ", Inspector.todays_wanted_criminal)

            if  "Foreigners require access permit" in order:
                Inspector.foreigners_require_access_permit = True
                
            if  "Workers require work pass" in order:      # Workers are those who have a purpose of "work" on access_permit document, in form of: ["PURPOSE": "WORK"]
                Inspector.workers_require_work_pass = True
                
            if  "vaccination" in order: # this order will be in format of "Citizens of Kolechia, Republia require cowpox vaccination" or "...no longer require..."
                if  "measles" in order: disease = "measles"
                if  "HPV" in order: disease = "HPV"
                if  "cholera" in order: disease = "cholera"
                if  "typhus" in order: disease = "typhus"
                if  "yellow fever" in order: disease = "yellow fever"
                if  "hepatitis B" in order: disease = "hepatitis B"
                if  "tetanus" in order: disease = "tetanus"
                if  "tuberculosis" in order: disease = "tuberculosis"
                if  "rubella" in order: disease = "rubella"
                if  "polio" in order: disease = "polio"
                if  "cowpox" in order: disease = "cowpox"
                
                if  "Entrants" in order: #"Entrants" means citizens of ALL nations. So to be clever, add all countries to "order" string so test in next IF statement will catch them all!
                    order = order + "Arstotzka Antegria Impor Kolechia Obristan Republia United Federation"
                elif "Foreigners" in order: # "Foreigners" means citizens of ALL FOREIGN nations. Add all foreign countries to "order" string so test in next IF statement will catch them all!
                    order = order + "Antegria Impor Kolechia Obristan Republia United Federation"
                    
                if  "no longer require" in order: # remove required vaccination from nation-specific list (test "no longer require" first as "require" would also be found in this check
                    if  "Arstotzka" in order: Inspector.Arstotzka_required_vaccination_set.remove(disease)
                    if  "Antegria" in order: Inspector.Antegria_required_vaccination_set.remove(disease)
                    if  "Impor" in order: Inspector.Impor_required_vaccination_set.remove(disease)
                    if  "Kolechia" in order: Inspector.Kolechia_required_vaccination_set.remove(disease)
                    if  "Obristan" in order: Inspector.Obristan_required_vaccination_set.remove(disease)
                    if  "Republia" in order: Inspector.Republia_required_vaccination_set.remove(disease)
                    if  "United Federation" in order: Inspector.UnitedFederation_required_vaccination_set.remove(disease)
                else: # if we are not processing for "no longer require", we are processing for "require"
                    if  "Arstotzka" in order: Inspector.Arstotzka_required_vaccination_set.add(disease)
                    if  "Antegria" in order: Inspector.Antegria_required_vaccination_set.add(disease)
                    if  "Impor" in order: Inspector.Impor_required_vaccination_set.add(disease)
                    if  "Kolechia" in order: Inspector.Kolechia_required_vaccination_set.add(disease)
                    if  "Obristan" in order: Inspector.Obristan_required_vaccination_set.add(disease)
                    if  "Republia" in order: Inspector.Republia_required_vaccination_set.add(disease)
                    if  "United Federation" in order: Inspector.UnitedFederation_required_vaccination_set.add(disease)

#####################
# INSPECT METHOD:
#####################
    def inspect(self,entrant_documents):
    
        #print("inspect method called...")
        #print("entrants_require_passport",Inspector.entrants_require_passport)
        #print("allow_citizens_of",Inspector.allow_citizens_of)
    
        #print("entrant_documents",entrant_documents)
        #print("entrant_documents is of type:",type(entrant_documents))

        #### GENERAL INFO: ####
        # Incoming parameter "entrant_documents" is a DICT. Each document it contains is a KEY, and the VALUE is a string of info relevant to that document (i.e. KEY)
        # That's a bit inconvenient for us, because we want to be able to access individual bits of the string easily. So, we convert each KEY of the original 
        # entrant_documents DICT to be a separate dict, meaning we have one DICT per incoming DOCUMENT, up to a max of seven kinds of document.
        #
        #       josef = {
        #	"passport": 'ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15'
        #       }
        #
        # In the above, "josef" is the name of the dict passed in (which becomes entrant_documents), "passport" is the key and everything else is the value.
        # Other doccos would have been represented by other key:value pairs as per any python dict.
        # Note how in the string (which is the value of the dict entry) we have property:value pairs, where "property" is e.g. ID# or DOB and value is GC07D-FU8AR or 1933.11.28
        # So a ":" separates the property from its value, and a \n (newline escape sequence) separates each set of property:value pairs.
        # For the purpose of writing reasonably readable code below, we will restructure this data into up to seven new dicts, and each dict will have property:value as its
        # key:value entries. That way we can access e.g. the value of a DOB on a passport very easily.
        # passport_in = {
        #       "ID#": "GC07D-FU8AR"
        #       "NATION": "Arstotzka"
        #       "NAME": "Costanza, Josef"
        #       "DOB": "1933.11.28"
        #       "SEX": "M"
        #       "ISS": "East Grestin"
        #       "EXP": "1983.03.15"
        #    }

        # Note - It might have made for more efficient code to create these documents as a dict of dicts rather than separate because then we could have iterated through the doccos
        #   more efficiently in certain places. Not to worry, it all works as is and seems easily quick enough to avoid any timeouts.
        
        passport_in = {}    # first we create an empty dict for each potential docco
        ID_card_in = {}
        access_permit_in = {}
        work_pass_in = {}
        grant_of_asylum_in = {}
        certificate_of_vaccination_in = {}
        diplomatic_authorization_in = {}

        for curr_key in entrant_documents: # now we iterate through the KEYs in the original entrant_documents dict and build dictionaries from those keys/values
            if  curr_key == 'passport':
                full_string_value = entrant_documents["passport"]
                
                list_of_key_value_pairs = full_string_value.split("\n")
                for element in list_of_key_value_pairs:
                    element_as_list = element.split(":")
                    passport_in[element_as_list[0]]=element_as_list[1]
                print("passport_in=",passport_in)
                #print("NAME",passport_in['NAME'])
                
            if  curr_key == 'ID_card':
                full_string_value = entrant_documents["ID_card"]
                
                list_of_key_value_pairs = full_string_value.split("\n")
                for element in list_of_key_value_pairs:
                    element_as_list = element.split(":")
                    ID_card_in[element_as_list[0]]=element_as_list[1]
                print("ID_card_in=",ID_card_in)
                
            if  curr_key == 'access_permit':
                full_string_value = entrant_documents["access_permit"]
                
                list_of_key_value_pairs = full_string_value.split("\n")
                for element in list_of_key_value_pairs:
                    element_as_list = element.split(":")
                    access_permit_in[element_as_list[0]]=element_as_list[1]
                print("access_permit_in=",access_permit_in)
                
            if  curr_key == 'work_pass':
                full_string_value = entrant_documents["work_pass"]
                
                list_of_key_value_pairs = full_string_value.split("\n")
                for element in list_of_key_value_pairs:
                    element_as_list = element.split(":")
                    work_pass_in[element_as_list[0]]=element_as_list[1]
                print("work_pass_in=",work_pass_in)
                
            if  curr_key == 'grant_of_asylum':
                full_string_value = entrant_documents["grant_of_asylum"]
                
                list_of_key_value_pairs = full_string_value.split("\n")
                for element in list_of_key_value_pairs:
                    element_as_list = element.split(":")
                    grant_of_asylum_in[element_as_list[0]]=element_as_list[1]
                print("grant_of_asylum_in=",grant_of_asylum_in)
                
            if  curr_key == 'certificate_of_vaccination':
                full_string_value = entrant_documents["certificate_of_vaccination"]
                
                list_of_key_value_pairs = full_string_value.split("\n")
                for element in list_of_key_value_pairs:
                    element_as_list = element.split(":")
                    certificate_of_vaccination_in[element_as_list[0]]=element_as_list[1]
                print("certificate_of_vaccination_in=",certificate_of_vaccination_in)
                
            if  curr_key == 'diplomatic_authorization':
                full_string_value = entrant_documents["diplomatic_authorization"]
                
                list_of_key_value_pairs = full_string_value.split("\n")
                for element in list_of_key_value_pairs:
                    element_as_list = element.split(":")
                    diplomatic_authorization_in[element_as_list[0]]=element_as_list[1]
                print("diplomatic_authorization_in=",diplomatic_authorization_in)
        
        print("keys in entrant_documents dictionary:")
        for each_key in entrant_documents:
            print(each_key)
        
        ###################### RULES !!!! ##################

##### DETAINMENT RULES ######
# Wanted by the State (check all documents that contain NAME):
        if  "passport" in entrant_documents:
            if  passport_in["NAME"].strip() == Inspector.todays_wanted_criminal:
                print("Detainment: Entrant is a wanted criminal.")
                return "Detainment: Entrant is a wanted criminal."
                
        if  "ID_card" in entrant_documents:
            if  ID_card_in["NAME"].strip() == Inspector.todays_wanted_criminal:
                print("Detainment: Entrant is a wanted criminal.")
                return "Detainment: Entrant is a wanted criminal."
                
        if  "access_permit" in entrant_documents:
            if  access_permit_in["NAME"].strip() == Inspector.todays_wanted_criminal:
                print("Detainment: Entrant is a wanted criminal.")
                return "Detainment: Entrant is a wanted criminal."
                
        if  "work_pass" in entrant_documents:
            if  work_pass_in["NAME"].strip() == Inspector.todays_wanted_criminal:
                print("Detainment: Entrant is a wanted criminal.")
                return "Detainment: Entrant is a wanted criminal."
                
        if  "grant_of_asylum" in entrant_documents:
            if  grant_of_asylum_in["NAME"].strip() == Inspector.todays_wanted_criminal:
                print("Detainment: Entrant is a wanted criminal.")
                return "Detainment: Entrant is a wanted criminal."
                
        if  "certificate_of_vaccination" in entrant_documents:
            if  certificate_of_vaccination_in["NAME"].strip() == Inspector.todays_wanted_criminal:
                print("Detainment: Entrant is a wanted criminal.")
                return "Detainment: Entrant is a wanted criminal."
                
        if  "diplomatic_authorization" in entrant_documents:
            if  diplomatic_authorization_in["NAME"].strip() == Inspector.todays_wanted_criminal:
                print("Detainment: Entrant is a wanted criminal.")
                return "Detainment: Entrant is a wanted criminal."


# We don't actually care what mismatches with what, only that there is a mismatch.
# So, go through each document, add relevant properties to a particular SET.
# If any SET (eg set of NAMEs, set of ID#s, set of NATIONs etc). If any SET
# contains > 1 element, we have a mismatch on that SET. Return relevant message and DETAIN!!!

# mismatch check SETs initialised (only these 4 fields are relevant to mismatches):
        id_set = set()
        nation_set = set()
        name_set = set()
        dob_set = set()

        # (note - commented out fields do not appear on relevant document)            
        if  "passport" in entrant_documents:
            id_set.add(passport_in["ID#"].strip())
            nation_set.add(passport_in["NATION"].strip())
            name_set.add(passport_in["NAME"].strip())
            dob_set.add(passport_in["DOB"].strip())
                
        if  "ID_card" in entrant_documents:
            #id_set.add(ID_card_in["ID#"].strip())
            #nation_set.add(ID_card_in["NATION"].strip())
            name_set.add(ID_card_in["NAME"].strip())
            dob_set.add(ID_card_in["DOB"].strip())
                
        if  "access_permit" in entrant_documents:
            id_set.add(access_permit_in["ID#"].strip())
            nation_set.add(access_permit_in["NATION"].strip())
            name_set.add(access_permit_in["NAME"].strip())
            #dob_set.add(access_permit_in["DOB"].strip())
                
        if  "work_pass" in entrant_documents:
            #id_set.add(work_pass_in["ID#"].strip())
            #nation_set.add(work_pass_in["NATION"].strip())
            name_set.add(work_pass_in["NAME"].strip())
            #dob_set.add(work_pass_in["DOB"].strip())
                
        if  "grant_of_asylum" in entrant_documents:
            id_set.add(grant_of_asylum_in["ID#"].strip())
            nation_set.add(grant_of_asylum_in["NATION"].strip())
            name_set.add(grant_of_asylum_in["NAME"].strip())
            #dob_set.add(grant_of_asylum_in["DOB"].strip())

        if  "certificate_of_vaccination" in entrant_documents:
            id_set.add(certificate_of_vaccination_in["ID#"].strip())
            #nation_set.add(certificate_of_vaccination_in["NATION"].strip())
            name_set.add(certificate_of_vaccination_in["NAME"].strip())
            #dob_set.add(certificate_of_vaccination_in["DOB"].strip())

        if  "diplomatic_authorization" in entrant_documents:
            id_set.add(diplomatic_authorization_in["ID#"].strip())
            nation_set.add(diplomatic_authorization_in["NATION"].strip())
            name_set.add(diplomatic_authorization_in["NAME"].strip())
            #dob_set.add(diplomatic_authorization_in["DOB"].strip())

        if  len(id_set) > 1:
            print("Detainment: ID number mismatch.")
            return "Detainment: ID number mismatch."
              
        if  len(nation_set) > 1:
            print("Detainment: nationality mismatch.")
            return "Detainment: nationality mismatch."
                
        if  len(name_set) > 1:
            print("Detainment: name mismatch.")
            return "Detainment: name mismatch."
                
        if  len(dob_set) > 1:
            print("Detainment: date of birth mismatch.")
            return "Detainment: date of birth mismatch."


##### ENTRY REFUSED RULES: ######

    ### PASSPORT ###

        # Is a passport required?
        if  "passport" not in entrant_documents \
        and Inspector.entrants_require_passport:
            print("Entry denied: missing required passport.")
            return "Entry denied: missing required passport."
        
        # Has the passport expired?
        if  "passport" in entrant_documents \
        and Inspector.entrants_require_passport:
            if  passport_in["EXP"].strip() < "1982.11.22":
                print("Entry denied: passport expired.")
                return "Entry denied: passport expired."
                
        # Is the country of origin on Passport on the permitted list?
            if  passport_in["NATION"].replace(" ","") not in Inspector.allow_citizens_of: # remove inner space so "United Federaton" becomes "UnitedFederaton" (easier to process) as
                print("Entry denied: citizen of banned nation.")                          # space was causing United and Federation to be treated as 2 countries in some parts of code
                return "Entry denied: citizen of banned nation."

        # If diplomatic autorisation in docs provided, ACCESS must include Arstotzka
            if  "diplomatic_authorization" in entrant_documents:
                if  "Arstotzka" not in diplomatic_authorization_in["ACCESS"]:
                    print("Entry denied: invalid diplomatic authorization.")
                    return "Entry denied: invalid diplomatic authorization."
        
        # *********** RELEVANT TO CITIZENS OF OUR GREAT NATION OF ARSTOTZKA ONLY: ***********
        # If citizens of Arstotzka require an ID_card make sure they have one
            if  passport_in["NATION"].strip() == "Arstotzka":
                if  Inspector.citizens_of_Arstotzka_require_ID_card:
                    if  "ID_card" not in entrant_documents:
                        print("Entry denied: missing required ID card.")
                        return "Entry denied: missing required ID card."
                        
        # *********** RELEVANT TO FOREIGNERS ONLY: ***********                
        # If Foreigners require access permit make sure they have one...                
            elif  Inspector.foreigners_require_access_permit: #can accept diplomatic_authorization or grant_of_asylum instead of access_permit
                if  "access_permit" not in entrant_documents \
                and "diplomatic_authorization" not in entrant_documents \
                and "grant_of_asylum" not in entrant_documents:
                    print("Entry denied: missing required access permit.")
                    return "Entry denied: missing required access permit."
        # check access permit isn't out of date...
                if  "access_permit" in entrant_documents:
                    if  access_permit_in["EXP"].strip() < "1982.11.22":
                        print("Entry denied: access permit expired.")
                        return "Entry denied: access permit expired."
                # workers need a work pass
                    if  access_permit_in["PURPOSE"].strip() == "WORK" \
                    and Inspector.workers_require_work_pass:
                        if  "work_pass" not in entrant_documents:
                            print("Entry denied: missing required work pass.")
                            return "Entry denied: missing required work pass."
                # if grant of asylum docco presented, make sure it hasn't expired
                if  "grant_of_asylum" in entrant_documents:
                    if  grant_of_asylum_in["EXP"].strip() < "1982.11.22":
                        print("Entry denied: grant of asylum expired.")
                        return "Entry denied: grant of asylum expired."

    ### VACCINATIONS ###
    
        # Using NATION on passport, check if the person is from a nation which is currently subject to vaccinaton control
        # If they are, they must have the relevant document (certificate_of_vaccination) and this document must specify 
        # all diseases currently requiring vaccination
        
            disease_set = set() # set up disease_set as an empty set first (it MAY be reassigned as a pointer to an existing set in following IF statements)
            # NB!! These assignments set up new POINTERS (disease_set) to the existing set (whatever country we're testing for). They don't create new sets
            if  passport_in["NATION"].strip() == "Arstotzka": disease_set = Inspector.Arstotzka_required_vaccination_set
            if  passport_in["NATION"].strip() == "Antegria": disease_set = Inspector.Antegria_required_vaccination_set
            if  passport_in["NATION"].strip() == "Impor": disease_set = Inspector.Impor_required_vaccination_set
            if  passport_in["NATION"].strip() == "Kolechia": disease_set = Inspector.Kolechia_required_vaccination_set
            if  passport_in["NATION"].strip() == "Obristan": disease_set = Inspector.Obristan_required_vaccination_set
            if  passport_in["NATION"].strip() == "Republia": disease_set = Inspector.Republia_required_vaccination_set
            if  passport_in["NATION"].strip() == "United Federation": disease_set = Inspector.UnitedFederation_required_vaccination_set
            
            if  len(disease_set) > 0: # if vaccinations are required for the nation of the person trying to enter...
                if  "certificate_of_vaccination" in entrant_documents: # ...make sure they have the docco
                    disease_list = list(disease_set) # convert to set to a list so we can iterate
                    for disease in disease_list:
                        if  disease not in certificate_of_vaccination_in["VACCINES"]: # VACCINES key of certificate_of_vaccination_in dict contains string of vaccinations
                            print("Entry denied: missing required vaccination.")      #  so if a required vaccination isn't mentioned there, return the bad news!
                            return "Entry denied: missing required vaccination."
                else: # no docco (but vaccinations ARE required), means no entry!
                    print("Entry denied: missing required certificate of vaccination.")
                    return "Entry denied: missing required certificate of vaccination."
            
 # If we get this far, we're allowing the person in. Return message depends on where they're from
        if  passport_in["NATION"].strip() == "Arstotzka":
            print("Glory to Arstotzka.")
            return "Glory to Arstotzka."
        else:
            print("Cause no trouble.")
            return "Cause no trouble."


inspector = Inspector()
send_bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector.receive_bulletin(send_bulletin)

josef = {
	"passport": 'ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15'
}
guyovich = {
	"access_permit": 'NAME: Guyovich, Russian\nNATION: Obristan\nID#: TE8M1-V3N7R\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 159cm\nWEIGHT: 60kg\nEXP: 1983.07.13'
}
roman = {
	"passport": 'ID#: WK9XA-LKM0Q\nNATION: United Federation\nNAME: Dolanski, Roman\nDOB: 1933.01.01\nSEX: M\nISS: Shingleton\nEXP: 1983.05.12',
	"grant_of_asylum": 'NAME: Dolanski, Roman\nNATION: United Federation\nID#: Y3MNC-TPWQ2\nDOB: 1933.01.01\nHEIGHT: 176cm\nWEIGHT: 71kg\nEXP: 1983.09.20'
}
"""
Test.describe('Preliminary training')

test.assert_equals(inspector.inspect(josef), 'Glory to Arstotzka.');
test.assert_equals(inspector.inspect(guyovich), 'Entry denied: missing required passport.');
test.assert_equals(inspector.inspect(roman), 'Detainment: ID number mismatch.');

"""
