import streamlit as st
from flask import Flask

app = Flask(__name)

@app.route('/')
def hello_world():
    # Define the HTML content as a string
    html_content = """
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4563574275594853"
     crossorigin="anonymous"></script>
    """
    return html_content

if __name__ == '__main__':
    app.run()

def calculate_bmi(height, weight):
  """Calculates the BMI given the height and weight in meters and kilograms."""
  bmi = weight / height ** 2
  return bmi

def main():
  """The main function of the app."""
  st.title("BMI Calculator")

  height = st.number_input("Height (in meters)")
  weight = st.number_input("Weight (in kilograms)")

  bmi = calculate_bmi(height, weight)

  st.write("Your BMI is:", bmi)

  if bmi < 18.5:
    st.write("You are underweight.")
  elif bmi < 25:
    st.write("You are healthy.")
  elif bmi < 30:
    st.write("You are overweight.")
  else:
    st.write("You are obese.")

if __name__ == "__main__":
  main()
