import re

translations = {
    "1N/2D": "1N/2D",
    "2N/3D": "2N/3D",
    "Coorg 1N/2D & 2N/3D": "ಕೊಡಗು 1N/2D & 2N/3D",
    "Coorg - Chikkamagalur 2N/3D & 3N/4D": "ಕೊಡಗು - ಚಿಕ್ಕಮಗಳೂರು 2N/3D & 3N/4D",
    "Mysore - Ooty 1N/2D": "ಮೈಸೂರು - ಊಟಿ 1N/2D",
    "Mysore Ooty Coonoor 2N/3D": "ಮೈಸೂರು ಊಟಿ ಕೂನೂರು 2N/3D",
    "Mysore - Ooty Coonoor Filmy Chakkar 3N/4D & 4N/5D": "ಮೈಸೂರು - ಊಟಿ ಕೂನೂರು ಫಿಲ್ಮಿ ಚಕ್ಕರ್ 3N/4D & 4N/5D",
    "Mysore Ooty Wayanad 5N/6D, 2N/3D & 3N/4D": "ಮೈಸೂರು ಊಟಿ ವಯನಾಡ್ 5N/6D, 2N/3D & 3N/4D",
    "Mysore - Coorg 2N/3D & 3N/4D": "ಮೈಸೂರು - ಕೊಡಗು 2N/3D & 3N/4D",
    "Mysore - Coorg - Wayanad 5N/6D": "ಮೈಸೂರು - ಕೊಡಗು - ವಯನಾಡ್ 5N/6D",
    "Mysore Wayanad 2N/3D & 3N/4D": "ಮೈಸೂರು ವಯನಾಡ್ 2N/3D & 3N/4D",
    "Mysore Ooty Kodai Madurai Rameswaram Kanyakumari 6N/7D & 7N/8D": "ಮೈಸೂರು ಊಟಿ ಕೊಡೈ ಮಧುರೈ ರಾಮೇಶ್ವರಂ ಕನ್ಯಾಕುಮಾರಿ 6N/7D & 7N/8D",
    "Munnar 2N/3D": "ಮುನ್ನಾರ್ 2N/3D",
    "Wayanad 1N/2D & 2N/3D": "ವಯನಾಡ್ 1N/2D & 2N/3D",
    "Munnar - Thekkady 2N/3D": "ಮುನ್ನಾರ್ - ತೇಕ್ಕಡಿ 2N/3D",
    "Munnar Thekkady Alleppey 3N/4D & 4N/5D": "ಮುನ್ನಾರ್ ತೇಕ್ಕಡಿ ಅಲೆಪ್ಪಿ 3N/4D & 4N/5D",
    "Munnar - Alleppey 2N/3D & 3N/4D": "ಮುನ್ನಾರ್ - ಅಲೆಪ್ಪಿ 2N/3D & 3N/4D",
    "Munnar Alleppey Kovalam 4N/5D": "ಮುನ್ನಾರ್ ಅಲೆಪ್ಪಿ ಕೋವಲಂ 4N/5D",
    "Munnar Thekkady Alleppey Trivandrum 5N/6D": "ಮುನ್ನಾರ್ ತೇಕ್ಕಡಿ ಅಲೆಪ್ಪಿ ತಿರುವನಂತಪುರಂ 5N/6D",
    "Trivandrum 1N/2D": "ತಿರುವನಂತಪುರಂ 1N/2D",
    "Trivandrum - Kanyakumari 2N/3D": "ತಿರುವನಂತಪುರಂ - ಕನ್ಯಾಕುಮಾರಿ 2N/3D",
    "Ooty 1N/2D, 2N/3D, 3N/4D": "ಊಟಿ 1N/2D, 2N/3D, 3N/4D",
    "Ooty - Kodaikanal 2N/3D, 3N/4D, 4N/5D": "ಊಟಿ - ಕೊಡೈಕೆನಾಲ್ 2N/3D, 3N/4D, 4N/5D",
    "Ooty - Kodaikanal - Munnar 6N/7D": "ಊಟಿ - ಕೊಡೈಕೆನಾಲ್ - ಮುನ್ನಾರ್ 6N/7D",
    "Kodaikanal 1N/2D & 2N/3D": "ಕೊಡೈಕೆನಾಲ್ 1N/2D & 2N/3D",
    "Kodaikanal - Munnar 4N/5D": "ಕೊಡೈಕೆನಾಲ್ - ಮುನ್ನಾರ್ 4N/5D",
    "Goa Package 3N/4D": "ಗೋವಾ ಪ್ಯಾಕೇಜ್ 3N/4D",
    "Alleppey Houseboat - Cochin 1N/2D": "ಅಲೆಪ್ಪಿ ಹೌಸ್‌ಬೋಟ್ - ಕೊಚ್ಚಿ 1N/2D",
    "Deluxe Hotel": "ಡೀಲಕ್ಸ್ ಹೋಟೆಲ್",
    "Super Deluxe Hotel": "ಸೂಪರ್ ಡೀಲಕ್ಸ್ ಹೋಟೆಲ್",
    "Star Hotel": "ಸ್ಟಾರ್ ಹೋಟೆಲ್"
}

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

for eng, kan in translations.items():
    if eng == "1N/2D" or eng == "2N/3D":
        # These appear in Chikkamagaluru
        # Avoid replacing inside existing replacements by using a strict match for <strong>
        content = re.sub(
            r'<strong>' + re.escape(eng) + r'</strong>',
            r'<strong>' + eng + r'<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">' + kan + r'</span></strong>',
            content
        )
    else:
        # Avoid replacing if it already has <br>
        content = re.sub(
            r'<strong>' + re.escape(eng) + r'</strong>',
            r'<strong>' + eng + r'<br><span style="font-size:0.85em;color:#FFD580;font-weight:500;">' + kan + r'</span></strong>',
            content
        )

# Fix CSS:
# 1. Reduce h2 font-size by 30%: 32px -> 22px
content = re.sub(
    r'\.tex-panel-hero-content h2 \{\s*font-family:\s*\'Playfair Display\',\s*serif;\s*font-size:\s*32px;',
    r'.tex-panel-hero-content h2 {\n  font-family: \'Playfair Display\', serif;\n  font-size: 22px;',
    content
)

# 2. Add padding to mobile .tex-panel-hero to not hide the title under the close button,
# and move the close button on mobile so it does not hide under the status bar.
# The mobile block .tex-panel-hero padding:
content = re.sub(
    r'padding: 32px 16px 12px !important;',
    r'padding: 70px 16px 12px !important;',
    content
)

# Also let\'s add the close button override in the mobile media block.
# We will inject it right after .tex-panel { ... } in mobile css.
content = re.sub(
    r'(\.tex-panel \{[^}]+\})',
    r'\1\n  .tex-panel > button { top: 40px !important; right: 20px !important; z-index: 100000 !important; background: rgba(0,0,0,0.9) !important; width: 36px !important; height: 36px !important; }',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Replacement done.")
