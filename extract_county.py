# Create county column based on location data
def extract_county(location):
    location = str(location).lower()

    # Normalize some Unicode/apostrophes issues
    location = location.replace('`', '\'')  # replace backticks with apostrophe

    # Nairobi
    if any(x in location for x in ['nairobi', 'westlands', 'lang\'ata', 'embakasi', 
                                   'kasarani', 'starehe', 'makadara', 'dagoretti',
                                   'kibra', 'kamukunji', 'roysambu', 'kayole',
                                   'mathare', 'dandora', 'njiru', 'kariobangi']):
        return 'Nairobi'

    # Kiambu
    elif any(x in location for x in ['kiambu', 'thika', 'juja', 'ruiru', 'kikuyu',
                                     'limuru', 'kabete', 'lari', 'githunguri',
                                     'kihara', 'tigoni', 'ngecha', 'kijabe']):
        return 'Kiambu'

    # Machakos
    elif any(x in location for x in ['machakos', 'konza', 'mlolongo', 'mavoko',
                                     'athi river', 'kinanie', 'kangundo']):
        return 'Machakos'

    # Murang'a (expanded and cleaned)
    elif any(x in location for x in [
        'murang\'a', 'muranga', 'kandara', 'mathioya', 'kangema',
        'gatanga', 'kiharu', 'makuyu', 'kenol', 'kigumo', 'kirimiri',
        'gacharage-ini', 'murang\'a south', 'maragua', 'kambiti', 'saba saba'
    ]):
        return 'Murang\'a'

    # Kirinyaga
    elif any(x in location for x in ['kirinyaga', 'sagana', 'karima']):
        return 'Kirinyaga'

    # Nyeri
    elif any(x in location for x in ['nyeri', 'mukurweini']):
        return 'Nyeri'

    # Nakuru
    elif any(x in location for x in ['nakuru', 'naivasha', 'gilgil', 'mai mahiu', 'suswa']):
        return 'Nakuru'

    # Kajiado
    elif any(x in location for x in ['kajiado', 'ongata rongai', 'ngong', 'kiserian']):
        return 'Kajiado'

    # Narok
    elif any(x in location for x in ['narok', 'loitokitok', 'rombo']):
        return 'Narok'

    # Makueni
    elif any(x in location for x in ['mbooni', 'makueni', 'kibwezi', 'emali']):
        return 'Makueni'

    # Embu
    elif 'embu' in location:
        return 'Embu'

    # Mombasa
    elif any(x in location for x in ['mombasa', 'jomvu', 'mikindani', 'mvita', 'nyali']):
        return 'Mombasa'

    # Kilifi
    elif any(x in location for x in ['kilifi', 'malindi', 'marereni', 'magarini', 'kaloleni', 'msabaha']):
        return 'Kilifi'

    # Kitui
    elif any(x in location for x in ['kitui', 'mwingi']):
        return 'Kitui'

    # Busia
    elif any(x in location for x in ['busia', 'matayos']):
        return 'Busia'

    # Kakamega
    elif any(x in location for x in ['kakamega', 'mumias', 'khwisero', 'likuyani']):
        return 'Kakamega'

    # West Pokot
    elif any(x in location for x in ['west pokot', 'kwanza']):
        return 'West Pokot'

    # Nandi
    elif any(x in location for x in ['nandi', 'kapsabet', 'chesumei']):
        return 'Nandi'

    # Nyamira
    elif any(x in location for x in ['nyamira', 'borabu', 'kijauri']):
        return 'Nyamira'

    # Kisii (from new update)
    elif any(x in location for x in ['kisii', 'masaba south', 'keroka']):
        return 'Kisii'

    # Kisumu
    elif any(x in location for x in ['kisumu', 'kolwa', 'kibos']):
        return 'Kisumu'

    # Samburu
    elif any(x in location for x in ['samburu', 'baawa']):
        return 'Samburu'

    # Taita Taveta
    elif any(x in location for x in ['taita', 'voi', 'wundanyi']):
        return 'Taita Taveta'

    # Kwale
    elif any(x in location for x in ['kwale', 'kinango', 'mackinon']):
        return 'Kwale'

    # Special cases
    elif 'syokimau-mulolongo' in location:
        return 'Machakos'
    elif 'karen' in location and 'nairobi' not in location:
        return 'Kajiado'

    else:
        return 'Other'