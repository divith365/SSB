import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'Cochin - Munnar - Thekkady - Alleppey 4N/5D', r'Cochin - Munnar - Thekkady - Alleppey 4 Nights / 5 Days Package'),
    (r'ಕೊಚ್ಚಿ - ಮೂನ್ನಾರ್ - ತೆಕ್ಕಡಿ - ಅಲೆಪ್ಪಿ 4N/5D', r'ಕೊಚ್ಚಿ - ಮೂನ್ನಾರ್ - ತೆಕ್ಕಡಿ - ಅಲೆಪ್ಪಿ 4 ರಾತ್ರಿ / 5 ದಿನದ ಪ್ಯಾಕೇಜ್'),
    
    (r'Cochin - Munnar - Thekkady - Alleppey - Kovalam 5N/6D & 6N/7D', r'Cochin - Munnar - Thekkady - Alleppey - Kovalam 5 Nights / 6 Days & 6 Nights / 7 Days Package'),
    (r'ಕೊಚ್ಚಿ - ಮೂನ್ನಾರ್ - ತೆಕ್ಕಡಿ - ಅಲೆಪ್ಪಿ - ಕೋವಲಂ 5N/6D & 6N/7D', r'ಕೊಚ್ಚಿ - ಮೂನ್ನಾರ್ - ತೆಕ್ಕಡಿ - ಅಲೆಪ್ಪಿ - ಕೋವಲಂ 5 ರಾತ್ರಿ / 6 ದಿನ & 6 ರಾತ್ರಿ / 7 ದಿನದ ಪ್ಯಾಕೇಜ್'),
    
    (r'Cochin - Munnar - Thekkady - Alleppey - Kanyakumari - Trivandrum 6N/7D & 7N/8D', r'Cochin - Munnar - Thekkady - Alleppey - Kanyakumari - Trivandrum 6 Nights / 7 Days & 7 Nights / 8 Days Package'),
    (r'ಕೊಚ್ಚಿ - ಮೂನ್ನಾರ್ - ತೆಕ್ಕಡಿ - ಅಲೆಪ್ಪಿ - ಕನ್ಯಾಕುಮಾರಿ - ತ್ರಿವೆಂಡ್ರಂ 6N/7D & 7N/8D', r'ಕೊಚ್ಚಿ - ಮೂನ್ನಾರ್ - ತೆಕ್ಕಡಿ - ಅಲೆಪ್ಪಿ - ಕನ್ಯಾಕುಮಾರಿ - ತ್ರಿವೆಂಡ್ರಂ 6 ರಾತ್ರಿ / 7 ದಿನ & 7 ರಾತ್ರಿ / 8 ದಿನದ ಪ್ಯಾಕೇಜ್'),
    
    (r'Kodaikanal 2N/3D & 3N/4D', r'Kodaikanal 2 Nights / 3 Days & 3 Nights / 4 Days Package'),
    (r'ಕೊಡೆಕಾನಲ್ 2N/3D & 3N/4D', r'ಕೊಡೆಕಾನಲ್ 2 ರಾತ್ರಿ / 3 ದಿನ & 3 ರಾತ್ರಿ / 4 ದಿನದ ಪ್ಯಾಕೇಜ್'),
    
    (r'Goa 2N/3D & 3N/4D & 4N/5D', r'Goa 2 Nights / 3 Days & 3 Nights / 4 Days & 4 Nights / 5 Days Package'),
    (r'ಗೋವಾ 2N/3D & 3N/4D & 4N/5D', r'ಗೋವಾ 2 ರಾತ್ರಿ / 3 ದಿನ & 3 ರಾತ್ರಿ / 4 ದಿನ & 4 ರಾತ್ರಿ / 5 ದಿನದ ಪ್ಯಾಕೇಜ್'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacements!")
