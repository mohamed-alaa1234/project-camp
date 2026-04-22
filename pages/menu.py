# 1. Importing extensions
import streamlit as st
import pandas as pd

# 2. Check Authentication
if not st.session_state.get('logged_in', False):
    st.warning('⚠️ Please sign in from the navbar to access the menu!')
    st.stop()

# 3. Main menu interface   
st.title('Welcome to Megatronics Planet 🤖', text_alignment='center')
st.success(f'Hello {st.session_state.get("name", "Customer")}, choose your components!')

# Adding menu items with prices
menu_microcontroller = {
    'UNO': 250,
    'MEGA': 210, 
    'NANO': 280,
    'UNO Q': 320
}
menu_wires = {
    'Male to Male': 180,
    'Male to Female': 200,
    'Female to Female': 190
}
menu_sensors = {
    'Ultrasonic': 30,
    'LDR': 30,
    'GAS Sensor': 45,
    'IR Sensor': 15
}

# Setup Tabs
micro_tab, wires_tab, sensors_tab = st.tabs(
    ['Microcontrollers ⚡', 'Wires & Cables 🔌', 'Sensors 📡']
)

order_items = []

# ================= MICROCONTROLLERS TAB =================
with micro_tab:
    st.header('Microcontrollers Boards')
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-04-21 235849.png", use_container_width=True) 
        st.subheader('Arduino UNO', text_alignment='center')
        st.write(f'Price: :red[{menu_microcontroller["UNO"]}] EGP')
        uno_qty = st.number_input('Quantity:', key='uno', min_value=0, max_value=20, step=1)
        if uno_qty > 0:
            order_items.append({"Item": "Arduino UNO", "Quantity": uno_qty, "Price": uno_qty * menu_microcontroller["UNO"]})
            
    with col2:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-04-21 235904.png", use_container_width=True) 
        st.subheader('Arduino MEGA', text_alignment='center')
        st.write(f'Price: :red[{menu_microcontroller["MEGA"]}] EGP')
        mega_qty = st.number_input('Quantity:', key='mega', min_value=0, max_value=20, step=1)
        if mega_qty > 0:
            order_items.append({"Item": "Arduino MEGA", "Quantity": mega_qty, "Price": mega_qty * menu_microcontroller["MEGA"]})
    
    with col3:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-04-21 235925.png", use_container_width=True) 
        st.subheader('Arduino NANO', text_alignment='center')
        st.write(f'Price: :red[{menu_microcontroller["NANO"]}] EGP')
        nano_qty = st.number_input('Quantity:', key='nano', min_value=0, max_value=20, step=1)
        if nano_qty > 0:
            order_items.append({"Item": "Arduino NANO", "Quantity": nano_qty, "Price": nano_qty * menu_microcontroller["NANO"]})

    with col4:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-04-21 235810.png", use_container_width=True) 
        st.subheader('Arduino UNO Q', text_alignment='center')
        st.write(f'Price: :red[{menu_microcontroller["UNO Q"]}] EGP')
        unoq_qty = st.number_input('Quantity:', key='unoq', min_value=0, max_value=20, step=1)
        if unoq_qty > 0:
            order_items.append({"Item": "UNO Q", "Quantity": unoq_qty, "Price": unoq_qty * menu_microcontroller["UNO Q"]})


# ================= WIRES TAB =================
with wires_tab:
    st.header('Jumper Wires')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-04-22 000256.png", use_container_width=True)
        st.subheader("Male to Male")
        st.write(f'Price: :red[{menu_wires["Male to Male"]}] EGP')
        mm_qty = st.number_input('Quantity:', key='mm_wire', min_value=0, max_value=50, step=1)
        if mm_qty > 0: 
            order_items.append({"Item": "Jumper Male to Male", "Quantity": mm_qty, "Price": mm_qty * menu_wires["Male to Male"]})
        
    with col2:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-04-22 000303.png", use_container_width=True)
        st.subheader("Male to Female")
        st.write(f'Price: :red[{menu_wires["Male to Female"]}] EGP')
        mf_qty = st.number_input('Quantity:', key='mf_wire', min_value=0, max_value=50, step=1)
        if mf_qty > 0: 
            order_items.append({"Item": "Jumper Male to Female", "Quantity": mf_qty, "Price": mf_qty * menu_wires["Male to Female"]})
        
    with col3:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-04-22 000310.png", use_container_width=True)
        st.subheader("Female to Female")
        st.write(f'Price: :red[{menu_wires["Female to Female"]}] EGP')
        ff_qty = st.number_input('Quantity:', key='ff_wire', min_value=0, max_value=50, step=1)
        if ff_qty > 0: 
            order_items.append({"Item": "Jumper Female to Female", "Quantity": ff_qty, "Price": ff_qty * menu_wires["Female to Female"]})


# ================= SENSORS TAB =================
with sensors_tab:
    st.header('Electronic Sensors')
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\4.jpg", use_container_width=True)
        st.subheader("Ultrasonic Sensor")
        st.write(f'Price: :red[{menu_sensors["Ultrasonic"]}] EGP')
        ultra_qty = st.number_input('Quantity:', key='ultra', min_value=0, max_value=20, step=1)
        if ultra_qty > 0: 
            order_items.append({"Item": "Ultrasonic Sensor", "Quantity": ultra_qty, "Price": ultra_qty * menu_sensors["Ultrasonic"]})
        
    with col2:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\2.jpg", use_container_width=True)
        st.subheader("LDR Sensor")
        st.write(f'Price: :red[{menu_sensors["LDR"]}] EGP')
        ldr_qty = st.number_input('Quantity:', key='ldr', min_value=0, max_value=20, step=1)
        if ldr_qty > 0: 
            order_items.append({"Item": "LDR Sensor", "Quantity": ldr_qty, "Price": ldr_qty * menu_sensors["LDR"]})
        
    with col3:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\3.jpg", use_container_width=True)
        st.subheader("GAS Sensor")
        st.write(f'Price: :red[{menu_sensors["GAS Sensor"]}] EGP')
        gas_qty = st.number_input('Quantity:', key='gas', min_value=0, max_value=20, step=1)
        if gas_qty > 0: 
            order_items.append({"Item": "GAS Sensor", "Quantity": gas_qty, "Price": gas_qty * menu_sensors["GAS Sensor"]})
        
    with col4:
        st.image("C:\\Users\\moha2\\OneDrive\\Pictures\\Screenshots\\1.jpg", use_container_width=True)
        st.subheader("IR Sensor")
        st.write(f'Price: :red[{menu_sensors["IR Sensor"]}] EGP')
        ir_qty = st.number_input('Quantity:', key='ir', min_value=0, max_value=20, step=1)
        if ir_qty > 0: 
            order_items.append({"Item": "IR Sensor", "Quantity": ir_qty, "Price": ir_qty * menu_sensors["IR Sensor"]})

st.divider()

# ================= SUMMARY SECTION =================
st.subheader("🛒 Order Summary")

total_price = sum([item["Price"] for item in order_items])

if len(order_items) > 0:
    df = pd.DataFrame(order_items)
    
    # Clean visual for table
    st.table(df)
    st.subheader(f'💰 Grand Total: :red[{total_price}] EGP')
else:
    st.info("Your cart is currently empty. Add items from the tabs above.")
    st.subheader(f'💰 Grand Total: :red[0] EGP')

if st.button("Place Order", use_container_width=True, type="primary"):
    if total_price > 0:
        st.success("🎉 Order placed successfully! Thank you for choosing Megatronics Planet!")
    else:
        st.error("Cannot place an empty order. Please add components to your cart.")