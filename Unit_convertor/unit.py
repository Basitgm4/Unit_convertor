import streamlit as st

def convert(amount, from_unit, to_unit):
    try:
        amount = float(amount)

        if from_unit == to_unit:
            return f"{amount:.2f} {to_unit}"

        if from_unit == "Meters" and to_unit == "Feet":
            result = amount * 3.28084
        elif from_unit == "Feet" and to_unit == "Meters":
            result = amount / 3.28084
        elif from_unit == "Kilograms" and to_unit == "Pounds":
            result = amount * 2.20462
        elif from_unit == "Pounds" and to_unit == "Kilograms":
            result = amount / 2.20462
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (amount * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (amount - 32) * 5/9
        else:
            return "Conversion not supported."

        return f"{result:.2f} {to_unit}"

    except ValueError:
        return "Invalid input."

def main():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
        }
        h1 {
            color: #3366cc;
            text-align: center;
            margin-bottom: 20px;
        }
        .stNumberInput > div > div > input,
        .stSelectbox > div > div > div > div {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            margin: 5px 0; /* Add margin for spacing */
            display: block; /* Ensures inputs are block-level */
            width: 100%; /* Make inputs take full width */
            box-sizing: border-box; /* Include padding and border in width */
        }
        .stButton > button {
            background: linear-gradient(to right, #4CAF50, #3e8e41); /* Gradient button */
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            display: block;
            margin: 20px auto; /* Center button */
        }
        .stButton > button:hover {
            background: linear-gradient(to right, #3e8e41, #367c37);
        }
        .stAlert {
            background-color: #ffe6e6;
            border: 1px solid #ff0000;
            border-radius: 5px;
            padding: 12px;
            color: #ff0000;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Unit Converter")

    amount = st.number_input("Amount:", value=1.0)

    units = ["Meters", "Feet", "Kilograms", "Pounds", "Celsius", "Fahrenheit"]
    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("From:", units, index=0)
    to_unit = col2.selectbox("To:", units, index=1)

    if st.button("Convert"):
        result = convert(amount, from_unit, to_unit)
        if "Invalid input" in result or "Conversion not supported" in result:
            st.markdown(f'<div class="stAlert">{result}</div>', unsafe_allow_html=True)
        else:
            st.write(f"Result: {result}")

if __name__ == "__main__":
    main()