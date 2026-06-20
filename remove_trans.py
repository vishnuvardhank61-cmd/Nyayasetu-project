import os
import re

directory = r'c:\Users\Vishnu vardhan\OneDrive\Desktop\NyayaSetu_Project\nyayasetu\templates'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace {% trans "Text" %} or {% trans 'Text' %} with Text
            new_content = re.sub(r'\{%\s*trans\s+[\'"](.*?)[\'"]\s*%\}', r'\1', content)
            
            # Remove {% load i18n %} completely
            new_content = new_content.replace('{% load i18n %}', '')
            
            if content != new_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Fixed {file}')
