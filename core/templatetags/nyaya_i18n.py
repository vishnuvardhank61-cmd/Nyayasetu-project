from django import template
from django.utils.translation import get_language

register = template.Library()

# Deep translation dictionary for core UI elements
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
}

@register.simple_tag(takes_context=True)
def ntrans(context, text):
    lang = get_language()
    if lang in ['hi', 'te'] and text in TRANSLATIONS:
        return TRANSLATIONS[text].get(lang, text)
    return text
