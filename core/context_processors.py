from django.utils.translation import get_language

def nyaya_i18n(request):
    """Context processor for robust multi-language support (Te/Hi)"""
    
    TRANSLATIONS = {
        "Home": {"hi": "होम", "te": "హోమ్"},
        "Rights": {"hi": "अधिकार", "te": "హక్కులు"},
        "Fundamental Rights": {"hi": "मौलिक अधिकार", "te": "ప్రాథమిక హక్కులు"},
        "Women Safety Laws": {"hi": "महिला सुरक्षा कानून", "te": "మహిళా భద్రతా చట్టాలు"},
        "Corporate & Workplace Laws": {"hi": "कार्यस्थल कानून", "te": "కార్యాలయ చట్టాలు"},
        "State/Regional Laws": {"hi": "क्षेत्रीय कानून", "te": "ప్రాంతీయ చట్టాలు"},
        "Violations & Consequences": {"hi": "उल्लंघन और परिणाम", "te": "ఉల్లంఘనలు & పరిణామాలు"},
        "Where to Complain Matrix": {"hi": "शिकायत मैट्रिक्स", "te": "ఫిర్యాదు మ్యాట్రిక్స్"},
        "Traffic Rules & e-Challan": {"hi": "यातायात नियम", "te": "ట్రాఫిక్ నియమ నిబంధనలు"},
        "Govt Services": {"hi": "सरकारी सेवाएं", "te": "ప్రభుత్వ సేవలు"},
        "Document Guides": {"hi": "दस्तावेज़ गाइड", "te": "డాక్యుమెంట్ గైడ్‌లు"},
        "Apply Online": {"hi": "ऑनलाइन आवेदन", "te": "ఆన్‌లైన్ దరఖాస్తు"},
        "Complaints": {"hi": "शिकायतें", "te": "ఫిర్యాదులు"},
        "File Complaint": {"hi": "शिकायत दर्ज करें", "te": "ఫిర్యాదు చేయండి"},
        "Police": {"hi": "पुलिस", "te": "పోలీస్"},
        "Helplines": {"hi": "हेल्पलाइन", "te": "హెల్ప్‌లైన్‌లు"},
        "News": {"hi": "समाचार", "te": "వార్తలు"},
        "My Applications": {"hi": "मेरे आवेदन", "te": "నా దరఖాస్తులు"},
        "Track Status": {"hi": "स्थिति ट्रैक करें", "te": "స్టేటస్ ట్రాక్ చేయండి"},
        "Specialized Civil Matters": {"hi": "विशेष नागरिक मामले", "te": "ప్రత్యేక పౌర విషయాలు"},
        "Statutory Commissions": {"hi": "वैधानिक आयोग", "te": "చట్టబద్ధమైన కమిషన్లు"},
        "Commissions Description": {"hi": "उन उल्लंघनों के लिए जो जरूरी नहीं कि 'आपराधिक' हों लेकिन आपकी गरिमा को नुकसान पहुंचाते हैं।", "te": "నేరపూరితం కాని ఉల్లంఘనల కోసం, కానీ మీ గౌరవం లేదా హక్కులకు భంగం కలిగించేవి."},
        "Womens Commission": {"hi": "महिला आयोग", "te": "మహిళా కమిషన్"},
        "Consumer Forum": {"hi": "उपभोक्ता फोरम", "te": "వినియోగదారుల ఫోరమ్"},
        "NHRC Human Rights": {"hi": "एनएचआरसी (मानवाधिकार)", "te": "NHRC (మానవ హక్కులు)"},
    }
    
    lang = get_language()
    
    # Create a mapped dictionary for the current language
    translations = {}
    for key, values in TRANSLATIONS.items():
        # Aggressive cleaning for template variable compatibility
        clean_key = key.replace("&", "and").replace("/", "_").replace("-", "_").replace("(", "").replace(")", "").replace("'", "")
        clean_key = clean_key.replace(" ", "_")
        
        if lang in values:
            translations[clean_key] = values[lang]
        else:
            translations[clean_key] = key
            
    return {'nyaya_trans': translations}
