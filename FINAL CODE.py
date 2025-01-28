import streamlit as st
import random

# Function to generate the SERC scenario
def generate_serc_scenario(victim_count):
    locations = ["pool", "lake", "open ocean", "river"]
    environmental_factors = ["sunny", "stormy", "fading daylight", "cold water temperatures", "murky water"]

    # Victim Details
    bystanders = random.randint(1, 3)
    injured = random.randint(1, victim_count - 2) if victim_count > 2 else 0
    non_swimmers = random.randint(1, victim_count - injured - 1) if victim_count > 2 else 0
    tired_swimmers = random.randint(0, victim_count - injured - non_swimmers) if victim_count > 1 else 0
    unconscious_swimmers = victim_count - (injured + non_swimmers + tired_swimmers)

    # Equipment and phone info
    equipment_list = ["first aid kit", "flotation devices", "radio", "oxygen", "rescue tubes", "throw bags"]
    available_equipment = random.sample(equipment_list, k=random.randint(2, 4))
    phone_distance = random.choice(["onsite", "200m away", "150m away at the park entrance"])

    # Scenario description
    location = random.choice(locations)
    environmental_factor = random.choice(environmental_factors)

    athlete_scenario = (
        f"A group of people is in distress at a {location}. Rescuers arrive to find a chaotic scene, with shouts for help "
        f"coming from multiple directions. The environment is challenging, with {environmental_factor}. "
        f"The nearest phone is {phone_distance}, and available equipment includes {', '.join(available_equipment)}."
    )

    # Coach's notes
    coach_notes = (
        f"Victims: {bystanders} bystanders, {injured} injured swimmers, {non_swimmers} non-swimmers, "
        f"{tired_swimmers} tired swimmers, {unconscious_swimmers} unconscious swimmers.\n"
        f"Equipment: {', '.join(available_equipment)}\n"
        f"Nearest phone: {phone_distance}."
    )

    return athlete_scenario, coach_notes

# Streamlit App Configuration
st.set_page_config(page_title="SERC Scenario Generator", layout="centered")
st.title("Lifesaving Sport SERC Scenario Generator")

st.write(
    """<div style='text-align: center;'>
    Welcome to the Simulated Emergency Response Scenario Generator! Use this tool to create detailed scenarios for training or competition.
    </div>""", 
    unsafe_allow_html=True
)

# Sidebar: Input for number of victims
st.sidebar.header("Settings")
victim_count = st.sidebar.number_input("Enter the number of swimmers available to be victims:", min_value=1, value=5, step=1)

# Button to generate the scenario
if st.button("Generate Scenario"):
    athlete_scenario, coach_notes = generate_serc_scenario(victim_count)

    # Display the generated scenarios
    st.subheader("Scenario Description (Athlete Version):")
    st.markdown(f"<div>{athlete_scenario}</div>", unsafe_allow_html=True)

    st.subheader("Coach’s Notes:")
    st.markdown(f"<div>{coach_notes}</div>", unsafe_allow_html=True)
