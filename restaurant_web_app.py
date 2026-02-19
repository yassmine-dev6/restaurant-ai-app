import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="Restaurant Content Generator", page_icon="🍽️")

# Title
st.title("🍽️ Restaurant Content Generator")
st.write("Generate professional menu descriptions, review responses, and social media posts instantly.")

# Sidebar for restaurant info
st.sidebar.header("Restaurant Information")
restaurant_name = st.sidebar.text_input("Restaurant Name", "Bella Italia")
cuisine_type = st.sidebar.text_input("Cuisine Type", "Italian")

# Main content - tabs for different tools
tab1, tab2, tab3 = st.tabs(["📝 Menu Description", "💬 Review Response", "📱 Social Media"])

# Tab 1: Menu Description
with tab1:
    st.header("Generate Menu Description")
    
    dish_name = st.text_input("Dish Name", "Truffle Risotto")
    ingredients = st.text_area("Ingredients", "arborio rice, Italian truffle, parmesan, cream")
    
    tone = st.selectbox("Writing Tone", ["Casual", "Upscale", "Playful"])
    
    if st.button("Generate Menu Description", key="menu"):
        with st.spinner("Generating..."):
            tone_instructions = {
                "Casual": "Write in a friendly, casual tone.",
                "Upscale": "Write in an elegant, sophisticated tone.",
                "Playful": "Write in a fun, energetic tone."
            }
            
            prompt = f"""Write an appetizing menu description for {dish_name} at {restaurant_name}, a {cuisine_type} restaurant.
            Ingredients: {ingredients}
            {tone_instructions[tone]}
            Make it mouth-watering. 50 words max."""
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = response.choices[0].message.content
            st.success("Generated!")
            st.write("### Result:")
            st.write(result)

# Tab 2: Review Response
with tab2:
    st.header("Generate Review Response")
    
    review = st.text_area("Customer Review", "Food was amazing but service was a bit slow. Still recommend!")
    
    if st.button("Generate Response", key="review"):
        with st.spinner("Generating..."):
            prompt = f"""Write a professional and friendly response to this review for {restaurant_name}.
            Review: {review}
            Thank them and address feedback genuinely."""
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = response.choices[0].message.content
            st.success("Generated!")
            st.write("### Result:")
            st.write(result)

# Tab 3: Social Media
with tab3:
    st.header("Generate Social Media Post")
    
    theme = st.text_input("Post Theme/Special", "Weekend brunch special with bottomless mimosas")
    
    if st.button("Generate Posts", key="social"):
        with st.spinner("Generating..."):
            prompt = f"""Write 3 Instagram caption variations for {restaurant_name}, a {cuisine_type} restaurant.
            Theme: {theme}
            Make them engaging with hashtags."""
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = response.choices[0].message.content
            st.success("Generated!")
            st.write("### Result:")
            st.write(result)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Built with Streamlit + Groq AI")