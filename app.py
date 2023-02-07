import os
import openai
import streamlit as st

st.markdown("# OpenAi test 🎈")
openai.api_key = os.getenv("OPENAI_API_KEY")
st.write("API KEY", openai.api_key)
current_line_number = 1

prompt = "### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### {}\nSELECT"
input_query = st.text_input('Ask me anything', key=str(current_line_number))
if input_query!='stop':
    try:
      response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt.format(input_query),
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
      )
      st.write("response ", response)
    except Exception as exc:
      st.write(f'En error occurred. {exc}')
