import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS
css_to_add = '''
  /* Mobile Floating Actions */
  .mobile-floating-actions {
    position: fixed; bottom: 20px; left: 16px; display: none;
    flex-direction: column; gap: 12px; z-index: 999;
  }
  .float-btn {
    width: 50px; height: 50px; border-radius: 50%; display: flex;
    align-items: center; justify-content: center; color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3); text-decoration: none;
    transition: transform 0.2s ease;
  }
  .float-btn:active { transform: scale(0.9); }
  .float-call { background-color: #2e6ff2; font-size: 20px; }
  .float-wa { background-color: #25D366; }
  
  @media(max-width: 900px) {
    .mobile-floating-actions { display: flex; }
  }
</style>'''

html = html.replace('</style>', css_to_add, 1)

# 2. Add HTML
html_to_add = '''
  <!-- Mobile Floating Actions -->
  <div class="mobile-floating-actions">
    <a href="https://wa.me/919880782128" target="_blank" class="float-btn float-wa" aria-label="WhatsApp">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="white">
        <path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.124.553 4.195 1.603 6.012L.15 23.393l5.503-1.442a11.966 11.966 0 006.378 1.83h.005c6.645 0 12.03-5.385 12.03-12.032S18.675 0 12.03 0h.001zm0 21.782h-.005a9.99 9.99 0 01-5.092-1.39l-.365-.217-3.784.992.992-3.784-.238-.378a9.982 9.982 0 01-1.528-5.31C2.011 5.485 6.495 1.002 12.03 1.002c5.534 0 10.017 4.484 10.017 10.019 0 5.536-4.484 10.02-10.017 10.02zm5.511-7.534c-.302-.152-1.792-.885-2.069-.986-.277-.101-.48-.152-.682.152-.202.302-.782.986-.958 1.189-.177.202-.354.227-.656.075-2.029-.997-3.411-1.921-4.707-3.665-.2-.269-.021-.414.13-.564.136-.135.302-.353.454-.53.151-.177.201-.303.302-.505.1-.202.05-.378-.025-.53-.075-.152-.682-1.643-.934-2.25-.246-.593-.497-.512-.682-.521-.176-.008-.378-.01-.58-.01-.202 0-.53.076-.807.379-.277.303-1.06 1.036-1.06 2.527 0 1.49 1.085 2.932 1.236 3.134.152.202 2.138 3.262 5.178 4.572.721.312 1.285.498 1.724.638.725.23 1.385.197 1.905.12.583-.086 1.792-.733 2.044-1.44.252-.708.252-1.314.177-1.44-.075-.126-.277-.202-.579-.354z"/>
      </svg>
    </a>
    <a href="tel:9880782128" class="float-btn float-call" aria-label="Call">
      📞
    </a>
  </div>

</body>'''

html = html.replace('</body>', html_to_add)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
