import streamlit as st

# Sayfa Başlığı ve Açıklama
st.markdown("##`Mantolama Maliyet Hesapla` :joy:")

# 1. EPS
col1, col2 = st.columns([3, 1])
with col1:
    eps_input = st.number_input(
        "1 m² EPS fiyatı (TL)", min_value=0.0, step=1.0, value=None, key="eps_fiyat"
    )
with col2:
    epsmiktar = st.number_input(
        "Miktar (m²)", min_value=0.0, step=1.0, value=1.0, key="eps_miktar"
    )

# 2. Yapıştırıcı (25 kg)
col3, col4 = st.columns([3, 1])
with col3:
    glue_input = st.number_input(
        "25 kg yapıştırıcı fiyatı (TL)", min_value=0.0, step=1.0, value=None, key="glue_fiyat"
    )
with col4:
    gluemiktar = st.number_input(
        "Miktar (kg)", min_value=0.0, step=1.0, value=4.0, key="glue_miktar"
    )

# 3. Sıva (25 kg)
col5, col6 = st.columns([3, 1])
with col5:
    siva_input = st.number_input(
        "25 kg sıva fiyatı (TL)", min_value=0.0, step=1.0, value=None, key="siva_fiyat"
    )
with col6:
    sivamiktar = st.number_input(
        "Miktar (kg)", min_value=0.0, step=1.0, value=4.5, key="siva_miktar"
    )

# 4. Mineral Sıva (25 kg)
col7, col8 = st.columns([3, 1])
with col7:
    mineralsiva_input = st.number_input(
        "25 kg mineral sıva fiyatı (TL)",
        min_value=0.0,
        step=1.0,
        value=None,
        key="mineral_fiyat",
    )
with col8:
    mineralsivamiktar = st.number_input(
        "Miktar (kg)", min_value=0.0, step=1.0, value=2.5, key="mineral_miktar"
    )

# 5. File (50m2)
col9, col10 = st.columns([3, 1])
with col9:
    file_input = st.number_input(
        "50 m² file fiyatı (TL)", min_value=0.0, step=1.0, value=None, key="file_fiyat"
    )
with col10:
    filemiktar = st.number_input(
        "Miktar (m²)", min_value=0.0, step=1.0, value=1.1, key="file_miktar"
    )

# 6. Dübel (500 adet)
col11, col12 = st.columns([3, 1])
with col11:
    dubel_input = st.number_input(
        "500 adet dübel fiyatı (TL)", min_value=0.0, step=1.0, value=None, key="dubel_fiyat"
    )
with col12:
    dubelmiktar = st.number_input(
        "Miktar (adet)", min_value=0.0, step=1.0, value=6.0, key="dubel_miktar"
    )

# 7. Fileli Köşe
col13, col14 = st.columns([3, 1])
with col13:
    filelikose_input = st.number_input(
        "1 boy fileli köşe fiyatı (TL)",
        min_value=0.0,
        step=1.0,
        value=None,
        key="kose_fiyat",
    )
with col14:
    filelikosemiktar = st.number_input(
        "Miktar (boy)", min_value=0.0, step=1.0, value=0.1, key="kose_miktar"
    )

st.markdown("---")

# Hesaplama Butonu
if st.button("Toplam Maliyeti Hesapla", type="primary"):
  # Miktarlarla çarpılarak yapılan oranlı hesaplamalar (Senin kodundaki orijinal mantık)
  eps = eps_input / 1 * epsmiktar
  glue = glue_input / 25 * gluemiktar
  siva = siva_input / 25 * sivamiktar
  mineralsiva = mineralsiva_input / 25 * mineralsivamiktar
  file = file_input / 50 * filemiktar
  dubel = dubel_input / 500 * dubelmiktar
  filelikose = filelikose_input / 1 * filelikosemiktar
