# Farm2Home_app.py
# A simple, production-ready Streamlit app for a Farm2Home marketplace.
# Features:
# - Multilingual UI (English, Hindi, Marathi, Tamil)
# - Product grid with search, category & price filters
# - Cart & checkout (mock) with rupee pricing
# - Lightweight Admin mode to add inventory items

from dataclasses import dataclass
from typing import List, Dict
import streamlit as st
import uuid

# App Config
st.set_page_config(page_title="Farm2Home", page_icon="🌾", layout="wide")

# i18n: Strings
STRINGS = {
    "en": {
        "title": "Farm2Home",
        "tagline": "Fresh produce delivered straight from local farms.",
        "language": "Language",
        "search": "Search",
        "category": "Category",
        "all": "All",
        "price_range": "Price range (₹)",
        "add_to_cart": "Add to Cart",
        "added": "Added!",
        "cart": "Cart",
        "empty_cart": "Your cart is empty.",
        "total": "Total",
        "checkout": "Checkout",
        "place_order": "Place Order",
        "name": "Full Name",
        "phone": "Phone",
        "address": "Delivery Address",
        "order_success": "✅ Order placed! Your order ID is",
        "continue_shopping": "Continue Shopping",
        "filters": "Filters",
        "reset": "Reset",
        "qty": "Qty",
        "unit": "unit",
        "per": "per",
        "admin_mode": "Admin Mode",
        "admin_key": "Admin key",
        "admin_ok": "Enter admin mode",
        "inventory": "Inventory",
        "add_product": "Add Product",
        "name_label": "Name",
        "price_label": "Price (₹)",
        "unit_label": "Unit (kg/l/dozen/pc)",
        "category_label": "Category",
        "image_url": "Image URL (optional)",
        "create": "Create",
        "created": "Product created",
        "remove": "Remove",
        "footer": "© 2025 Farm2Home — Built with Streamlit",
        "popular": "Popular Picks",
        "clear_cart": "Clear Cart",
        "no_results": "No products match your filters.",
        "delivery_note": "Note: This is a demo checkout (no payment).",
    },
    "hi": {
        "title": "Farm2Home",
        "tagline": "ताज़ी उपज सीधे खेतों से आपके घर तक।",
        "language": "भाषा",
        "search": "खोजें",
        "category": "श्रेणी",
        "all": "सभी",
        "price_range": "कीमत सीमा (₹)",
        "add_to_cart": "कार्ट में जोड़ें",
        "added": "जोड़ दिया!",
        "cart": "कार्ट",
        "empty_cart": "आपका कार्ट खाली है।",
        "total": "कुल",
        "checkout": "चेकआउट",
        "place_order": "ऑर्डर करें",
        "name": "पूरा नाम",
        "phone": "फोन",
        "address": "डिलीवरी पता",
        "order_success": "✅ ऑर्डर हो गया! आपका ऑर्डर आईडी है",
        "continue_shopping": "खरीदारी जारी रखें",
        "filters": "फ़िल्टर",
        "reset": "रीसेट",
        "qty": "मात्रा",
        "unit": "यूनिट",
        "per": "प्रति",
        "admin_mode": "एडमिन मोड",
        "admin_key": "एडमिन कुंजी",
        "admin_ok": "एडमिन में प्रवेश करें",
        "inventory": "भंडार",
        "add_product": "उत्पाद जोड़ें",
        "name_label": "नाम",
        "price_label": "कीमत (₹)",
        "unit_label": "यूनिट (किलो/ली/दर्जन/पीस)",
        "category_label": "श्रेणी",
        "image_url": "छवि URL (वैकल्पिक)",
        "create": "बनाएँ",
        "created": "उत्पाद जोड़ा गया",
        "remove": "हटाएँ",
        "footer": "© 2025 Farm2Home — Streamlit से निर्मित",
        "popular": "लोकप्रिय",
        "clear_cart": "कार्ट खाली करें",
        "no_results": "आपके फ़िल्टर से कोई उत्पाद नहीं मिला।",
        "delivery_note": "नोट: यह डेमो चेकआउट है (कोई पेमेंट नहीं)।",
    },
    "mr": {
        "title": "Farm2Home",
        "tagline": "ताजे अन्नद्रव्य थेट शेतातून तुमच्या घरी.",
        "language": "भाषा",
        "search": "शोधा",
        "category": "वर्ग",
        "all": "सर्व",
        "price_range": "किंमत श्रेणी (₹)",
        "add_to_cart": "कार्टमध्ये जोडा",
        "added": "जोडले!",
        "cart": "कार्ट",
        "empty_cart": "तुमचा कार्ट रिकामा आहे.",
        "total": "एकूण",
        "checkout": "चेकआउट",
        "place_order": "ऑर्डर करा",
        "name": "पूर्ण नाव",
        "phone": "फोन",
        "address": "डिलिव्हरी पत्ता",
        "order_success": "✅ ऑर्डर झाले! तुमचा ऑर्डर आयडी आहे",
        "continue_shopping": "खरेदी सुरू ठेवा",
        "filters": "फिल्टर्स",
        "reset": "रीसेट",
        "qty": "प्रमाण",
        "unit": "युनिट",
        "per": "प्रति",
        "admin_mode": "ॲडमिन मोड",
        "admin_key": "ॲडमिन की",
        "admin_ok": "ॲडमिन मध्ये जा",
        "inventory": "साठा",
        "add_product": "उत्पादन जोडा",
        "name_label": "नाव",
        "price_label": "किंमत (₹)",
        "unit_label": "युनिट (किलो/ली/डझन/पीस)",
        "category_label": "वर्ग",
        "image_url": "इमेज URL (ऐच्छिक)",
        "create": "तयार करा",
        "created": "उत्पादन तयार झाले",
        "remove": "काढा",
        "footer": "© 2025 Farm2Home — Streamlit द्वारा",
        "popular": "लोकप्रिय निवड",
        "clear_cart": "कार्ट रिकामी करा",
        "no_results": "तुमच्या फिल्टरनुसार उत्पादने आढळली नाहीत.",
        "delivery_note": "नोंद: हा डेमो चेकआउट आहे (पेमेंट नाही).",
    },
    "ta": {
        "title": "Farm2Home",
        "tagline": "சமீபத்திய பண்ணைப் பொருட்கள் உங்கள் இல்லத்திற்கே.",
        "language": "மொழி",
        "search": "தேடல்",
        "category": "வகை",
        "all": "அனைத்தும்",
        "price_range": "விலை வரம்பு (₹)",
        "add_to_cart": "வாங்குபட்டியலில் சேர்",
        "added": "சேர்க்கப்பட்டது!",
        "cart": "வாங்குபட்டி",
        "empty_cart": "உங்கள் வாங்குபட்டி காலியாக உள்ளது.",
        "total": "மொத்தம்",
        "checkout": "காசோலை",
        "place_order": "ஆர்டர் செய்",
        "name": "முழுப் பெயர்",
        "phone": "தொலைபேசி",
        "address": "டெலிவரி முகவரி",
        "order_success": "✅ ஆர்டர் நிறைவு! உங்கள் ஆர்டர் ஐடி:",
        "continue_shopping": "ஷாப்பிங் தொடர்க",
        "filters": "வடிப்பான்கள்",
        "reset": "மீட்டமை",
        "qty": "அளவு",
        "unit": "அலகு",
        "per": "ஒரு",
        "admin_mode": "நிர்வாக நிலை",
        "admin_key": "கீ",
        "admin_ok": "நிர்வாகத்தில் நுழை",
        "inventory": "கையிருப்பு",
        "add_product": "புதிய பொருள்",
        "name_label": "பெயர்",
        "price_label": "விலை (₹)",
        "unit_label": "அலகு (kg/l/dozen/pc)",
        "category_label": "வகை",
        "image_url": "பட இணைப்பு (விருப்ப)",
        "create": "உருவாக்கு",
        "created": "உருவாக்கப்பட்டது",
        "remove": "நீக்கு",
        "footer": "© 2025 Farm2Home — Streamlit மூலம்",
        "popular": "பிரபலமானவை",
        "clear_cart": "காலி செய்",
        "no_results": "உங்கள் வடிப்பான்களுக்கு பொருட்கள் இல்லை.",
        "delivery_note": "குறிப்பு: இது டெமோ காசோலை (கட்டணம் இல்லை).",
    },
}
SUPPORTED_LANGS = {"English": "en", "हिन्दी": "hi", "मराठी": "mr", "தமிழ்": "ta"}

# Data Model
@dataclass
class Product:
    id: str
    name: str
    price: float
    unit: str
    category: str
    image: str = ""

# Seed inventory
def seed_products() -> List[Product]:
    return [
        Product(str(uuid.uuid4()), "Tomatoes", 40, "kg", "Vegetables"),
        Product(str(uuid.uuid4()), "Onions", 35, "kg", "Vegetables"),
        Product(str(uuid.uuid4()), "Potatoes", 30, "kg", "Vegetables"),
        Product(str(uuid.uuid4()), "Organic Milk", 60, "l", "Dairy"),
        Product(str(uuid.uuid4()), "Free-range Eggs", 70, "dozen", "Dairy"),
        Product(str(uuid.uuid4()), "Alphonso Mango", 180, "kg", "Fruits"),
        Product(str(uuid.uuid4()), "Banana", 50, "dozen", "Fruits"),
        Product(str(uuid.uuid4()), "Cold Pressed Groundnut Oil", 180, "l", "Essentials"),
    ]

CATEGORIES = ["Vegetables", "Fruits", "Dairy", "Essentials"]

# State
if "inventory" not in st.session_state:
    st.session_state.inventory = seed_products()

if "cart" not in st.session_state:
    st.session_state.cart: Dict[str, int] = {}

if "lang_code" not in st.session_state:
    st.session_state.lang_code = "en"

def t(key: str) -> str:
    return STRINGS.get(st.session_state.lang_code, STRINGS["en"]).get(key, key)

def money(x: float) -> str:
    # show 0 decimals if integer, else 2
    return f"₹{x:,.0f}" if float(x).is_integer() else f"₹{x:,.2f}"

def get_product(pid: str) -> Product:
    for p in st.session_state.inventory:
        if p.id == pid:
            return p
    raise KeyError(pid)

def add_to_cart(pid: str, qty: int = 1):
    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + int(qty)

def remove_from_cart(pid: str):
    st.session_state.cart.pop(pid, None)

def clear_cart():
    st.session_state.cart = {}

# Sidebar: language, filters, cart
with st.sidebar:
    st.markdown(f"## 🛒 {t('title')}")
    # Language
    lang_label = t("language")
    current_index = list(SUPPORTED_LANGS.values()).index(st.session_state.lang_code)
    choice = st.selectbox(lang_label, list(SUPPORTED_LANGS.keys()), index=current_index)
    st.session_state.lang_code = SUPPORTED_LANGS[choice]

    st.markdown("---")
    st.markdown(f"### 🔎 {t('filters')}")
    query = st.text_input(f"🔍 {t('search')}", "")
    categories = [t("all")] + CATEGORIES
    cat = st.selectbox(f"📦 {t('category')}", categories)

    inv_prices = [p.price for p in st.session_state.inventory] or [0]
    min_price = int(min(inv_prices))
    max_price = int(max(inv_prices))
    price_min, price_max = st.slider(f"💰 {t('price_range')}", 0, max(100, max_price * 2), (min_price, max_price))

    if st.button(t("reset")):
        query = ""
        cat = t("all")
        price_min, price_max = (min_price, max_price)

    st.markdown("---")
    st.markdown(f"### 🧺 {t('cart')}")
    if not st.session_state.cart:
        st.caption(t("empty_cart"))
    else:
        total = 0.0
        for pid, qty in list(st.session_state.cart.items()):
            p = get_product(pid)
            line = p.price * qty
            total += line
            col1, col2, col3, col4 = st.columns([5, 2, 2, 2])
            with col1:
                st.write(f"{p.name}** — {money(p.price)} / {p.unit}")
            with col2:
                st.write(f"{t('qty')}: {qty}")
            with col3:
                st.write(money(line))
            with col4:
                if st.button(t("remove"), key=f"rm_{pid}"):
                    remove_from_cart(pid)
        if st.session_state.cart:
            st.write(f"{t('total')}: {money(total)}")
            st.button(t("clear_cart"), on_click=clear_cart)

# Header
st.title(f"🌾 {t('title')}")
st.caption(t("tagline"))

# Popular section
st.subheader(f"⭐ {t('popular')}")
cols_pop = st.columns(4)
for i, prod in enumerate(st.session_state.inventory[:4]):
    with cols_pop[i % 4]:
        st.markdown(f"{prod.name}")
        st.write(f"{money(prod.price)} / {prod.unit}")
        st.button(t("add_to_cart"), key=f"pop_{prod.id}", on_click=add_to_cart, args=(prod.id, 1))

st.markdown("---")

# Main grid with filters
filtered: List[Product] = []
for p in st.session_state.inventory:
    if query and query.lower() not in p.name.lower():
        continue
    if cat != t("all") and p.category != cat:
        continue
    if not (price_min <= p.price <= price_max):
        continue
    filtered.append(p)

if not filtered:
    st.info(t("no_results"))
else:
    cols = st.columns(3)
    for i, p in enumerate(filtered):
        with cols[i % 3]:
            with st.container(border=True):
                if p.image:
                    st.image(p.image, use_container_width=True)
                st.markdown(f"### {p.name}")
                st.write(f"{money(p.price)} / {p.unit}")
                qty = st.number_input(f"{t('qty')}", min_value=1, max_value=20, step=1, key=f"qty_{p.id}")
                st.button(t("add_to_cart"), key=f"add_{p.id}", on_click=add_to_cart, args=(p.id, int(qty)))

# Checkout
st.markdown("---")
st.subheader(f"💳 {t('checkout')}")
st.caption(t("delivery_note"))

with st.form("checkout_form", clear_on_submit=False):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input(t("name"))
        phone = st.text_input(t("phone"))
    with c2:
        address = st.text_area(t("address"))

    can_submit = bool(st.session_state.cart) and name.strip() and phone.strip() and address.strip()
    submitted = st.form_submit_button(t("place_order"), disabled=not can_submit)
    if submitted:
        order_id = str(uuid.uuid4())[:8].upper()
        st.success(f"{t('order_success')} *#{order_id}*")
        clear_cart()
        st.link_button(t("continue_shopping"), "#")

# Admin mode (lightweight)
with st.expander(f"🛠 {t('admin_mode')}"):
    key = st.text_input(t("admin_key"), type="password")
    if st.button(t("admin_ok")) and key == "admin123":
        st.session_state._is_admin = True

    if st.session_state.get("_is_admin"):
        st.markdown(f"### 📦 {t('inventory')}")
        for p in st.session_state.inventory:
            with st.container(border=True):
                st.write(f"{p.name}** — {money(p.price)} / {p.unit} — {p.category}")

        st.markdown("---")
        st.markdown(f"### ➕ {t('add_product')}")
        with st.form("add_product_form"):
            np_name = st.text_input(t("name_label"))
            np_price = st.number_input(t("price_label"), min_value=0.0, step=1.0)
            np_unit = st.text_input(t("unit_label"), value="kg")
            np_cat = st.selectbox(t("category_label"), CATEGORIES)
            np_img = st.text_input(t("image_url"))
            created = st.form_submit_button(t("create"))
            if created and np_name.strip():
                new_prod = Product(
                    id=str(uuid.uuid4()),
                    name=np_name.strip(),
                    price=float(np_price),
                    unit=np_unit.strip() or "kg",
                    category=np_cat,
                    image=np_img.strip(),
                )
                st.session_state.inventory.append(new_prod)
                st.success(t("created"))

# Footer
st.markdown("---")
st.caption(t("footer"))