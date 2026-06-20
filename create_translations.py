import os

def create_po_file(lang_code, translations):
    path = f'locale/{lang_code}/LC_MESSAGES'
    os.makedirs(path, exist_ok=True)
    
    with open(f'{path}/django.po', 'w', encoding='utf-8') as f:
        f.write('msgid ""\n')
        f.write('msgstr ""\n')
        f.write('"Content-Type: text/plain; charset=UTF-8\\n"\n')
        f.write('"Content-Transfer-Encoding: 8bit\\n"\n')
        f.write('"Project-Id-Version: \\n"\n')
        f.write(f'"Language: {lang_code}\\n"\n\n')
        
        for msgid, msgstr in translations.items():
            f.write(f'msgid "{msgid}"\n')
            f.write(f'msgstr "{msgstr}"\n\n')

# Translations for Navbar/Core UI
common_trans = {
    "Home": {
        "hi": "होम",
        "te": "హోమ్"
    },
    "Rights": {
        "hi": "अधिकार",
        "te": "హక్కులు"
    },
    "Fundamental Rights": {
        "hi": "मौलिक अधिकार",
        "te": "ప్రాథమిక హక్కులు"
    },
    "Women Safety Laws": {
        "hi": "महिला सुरक्षा कानून",
        "te": "మహిళా భద్రతా చట్టాలు"
    },
    "Corporate & Workplace Laws": {
        "hi": "कॉर्पोरेट और कार्यस्थल कानून",
        "te": "కార్పొరేట్ & కార్యాలయ చట్టాలు"
    },
    "State/Regional Laws": {
        "hi": "राज्य/क्षेत्रीय कानून",
        "te": "రాష్ట్ర/ప్రాంతీయ చట్టాలు"
    },
    "Violations & Consequences": {
        "hi": "उल्लंघन और परिणाम",
        "te": "ఉల్లంఘనలు & పరిణామాలు"
    },
    "Where to Complain Matrix": {
        "hi": "शिकायत कहाँ करें मैट्रिक्स",
        "te": "ఫిర్యాదు ఎక్కడ చేయాలో మ్యాట్రిక్స్"
    },
    "Traffic Rules & e-Challan": {
        "hi": "यातायात नियम और ई-चालान",
        "te": "ట్రాఫిక్ నియమ నిబంధనలు & ఇ-చలాన్"
    },
    "Govt Services": {
        "hi": "सरकारी सेवाएं",
        "te": "ప్రభుత్వ సేవలు"
    },
    "Document Guides": {
        "hi": "दस्तावेज़ गाइड",
        "te": "డాక్యుమెంట్ గైడ్‌లు"
    },
    "Apply Online": {
        "hi": "ऑनलाइन आवेदन करें",
        "te": "ఆన్‌లైన్‌లో దరఖాస్తు చేసుకోండి"
    },
    "Complaints": {
        "hi": "शिकायतें",
        "te": "ఫిర్యాదులు"
    },
    "File Complaint": {
        "hi": "शिकायत दर्ज करें",
        "te": "ఫిర్యాదు చేయండి"
    },
    "Police": {
        "hi": "पुलिस",
        "te": "పోలీస్"
    },
    "Helplines": {
        "hi": "हेल्पलाइन",
        "te": "హెల్ప్‌లైన్‌లు"
    }
}

hi_trans = {k: v['hi'] for k, v in common_trans.items()}
te_trans = {k: v['te'] for k, v in common_trans.items()}

create_po_file('hi', hi_trans)
create_po_file('te', te_trans)

print("Translation files created successfully for HI and TE.")
