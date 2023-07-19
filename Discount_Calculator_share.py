import streamlit as st

st.set_page_config(page_title="Discount Calculator", page_icon=":abacus:")

# --- Header Section ---
#st.subheader("Burkett Discount Calculator :notebook:")
st.title("Discount Calculator :notebook:")
st.info("This is a tool for quickly converting discounts in #/#/# format to the correct multiplier.", icon="ℹ️")
# st.write("Example use cases: Individual item - promo price validation - MIRP check")

# --- Body Section ---

with st.expander(label="**:blue[Information]**"):
 """
- Add your discount without a % sign and press Enter/Return.
- Your discount multilpier will be **:blue[rounded]** to **:blue[6 decimal places]** as needed.
    - The un-rounded multiplier will also be listed for your reference.
- You can multiply a List Price by the discount.
    - The result will be **:blue[rounded]** to **:blue[2 decimal]** places.

"""

# --- Calculator Tab ---
tab1, tab2 = st.tabs(["Calculator", "Discount Structure Explanation"])

with tab1:
    column1, column2 = st.columns(2, gap ="medium")

    # --- PYTHON FUNCTIONALITY: DISCOUNT ---

    with column1:
    
        user_input = st.text_input(label='**Enter your Discount**', placeholder='Example: 50/10/5', help='Make sure the discount aligns with VPD info')

        # list of each individual discount from user
        indiv_disc = user_input.split("/")
        indiv_disc_clean = [value for value in indiv_disc if value] # removes empty initial value from indiv_disc

        # each discount, converted to decimal, subtracted from 1 and stored in a list
        final_decimal_list = []

        for discount in indiv_disc_clean:
            discount = float(discount) # converts user's string input to float
            decimal = discount / 100
            final_decimal = 1 - decimal
            final_decimal_list.append(final_decimal)
            print(final_decimal)

        multiplier = 1

        for dec in final_decimal_list:
            multiplier = multiplier * dec

        # --- Response to User ---
        if multiplier == 1:
            st.subheader(f"Discount multiplier is: ")
        else:
            st.subheader(f":green[Discount multiplier is: {round(multiplier,6)}]")
            st.caption(f"*The un-rounded discount multiplier is: {multiplier}*")

    # --- PYTHON FUNCTIONALITY: DISCOUNT x LIST PRICE ---

    with column2:
        choice = st.selectbox("**Do you want to apply the Discount to a Price?**", ('','Yes', 'No'), help="Check AutoQuotes for the latest active list price")
        lp_user_input = 0
        if choice == 'Yes':
            lp_user_input = st.number_input(label='**Enter your Price**', step = 0.01)
            if lp_user_input == 0:
                st.subheader(f"Discounted price is: ")  
            else:
                st.subheader(f":green[Discounted price is: ${round(float(lp_user_input)*multiplier,2)}]")  

st.write("---")

# --- Discount Structure Explanation Tab ---

with tab2:
    tab2.subheader("Discount Structure Explanation 	:open_book:")
    tab2.write(
    """
    **:blue[50/10]** is an example of a discount structure. It represents the total percentage discount received on products from a vendor. 
    - The first number is the first discount received.
    - Each subsequent number represents the additional discount/s received beyond the first discount.  

    """)

    st.info(
    """
    A **:blue[50/10]** discount structure can be read out loud as follows: “:blue[An item sells for $100, but I get a 50% discount on it. I then get an additional 10% discount on the already discounted price.]”

    """)

    tab2.write(
    """
    Examples of other total discounts:
    - 50/10/8
    - 35/5/5/5
    """)
    

    st.info(
    """
    Additional discounts are based on various elements, such as additional purchase amounts negotiated with the vendor.

    """)

    tab2.write(
    """
    For creating the Cost Multiplier that is used in NetSuite, that sentence can be expressed as:
    
    **:blue[1 x 0.5 x 0.9 = 0.45]**.

    - Multiply by **:blue[0.5]** because we are now only paying **:blue[50%]** of the original price.
    - Multiply by **:blue[0.9]** because we are now only paying **:blue[90%]** of the already discounted (i.e., “new” original) price.
    
    """
    )

   

# --- Footer Section ---

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
