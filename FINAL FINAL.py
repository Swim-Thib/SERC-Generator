import streamlit as st
import random

def generate_serc_scenario(victim_count):
    # Step 2: General Nature of the Emergency
    locations = ["pool", "lake", "open ocean", "river"]
    environmental_factors = ["sunny", "stormy", "fading daylight", "cold water temperatures", "murky water"]

    # Step 3: Victim Details
    bystanders = random.randint(1, 3)
    injured = random.randint(1, victim_count - 2) if victim_count > 2 else 0
    non_swimmers = random.randint(1, victim_count - injured - 1) if victim_count > 2 else 0
    tired_swimmers = random.randint(0, victim_count - injured - non_swimmers) if victim_count > 1 else 0
    unconscious_swimmers = victim_count - (injured + non_swimmers + tired_swimmers)

    # Step 4: Resources
    equipment_list = ["first aid kit", "flotation devices", "radio", "oxygen", "rescue tubes", "throw bags"]
    available_equipment = random.sample(equipment_list, k=random.randint(2, 4))
    phone_distance_options = ["onsite", "200m away", "150m away at the park entrance"]
    nearest_phone = random.choice(phone_distance_options)

    # Step 5: Output Generation
    location = random.choice(locations)
    environmental_factor = random.choice(environmental_factors)

    # Athlete Version
    athlete_scenario = (
        f"A group of people is in distress at a {location}. Rescuers arrive to find a chaotic scene, with shouts for help "
        f"coming from multiple directions. The environment is challenging, with {environmental_factor}. "
        f"The nearest phone is {nearest_phone}, and available equipment includes {', '.join(available_equipment)}."
    )

    # Coach’s Notes
    coach_notes = (
        f"Victims: {bystanders} bystanders providing information, {injured} injured swimmers with minor injuries, "
        f"{non_swimmers} non-swimmers clinging to objects, {tired_swimmers} tired swimmers, and {unconscious_swimmers} unconscious swimmers.\n"
        f"Equipment: {', '.join(available_equipment)}\n"
        f"Additional Info: Nearest phone is {nearest_phone}."
    )

    return athlete_scenario, coach_notes

# Streamlit App
st.set_page_config(page_title="SERC Scenario Generator", layout="centered")
st.title("Lifesaving Sport SERC Scenario Generator")
st.markdown(
    """<div style='color: black; text-align: center;'>
    Welcome to the Simulated Emergency Response Scenario Generator! Use this tool to create detailed scenarios for training or competition.
    </div>""",
    unsafe_allow_html=True
)

# Sidebar for number of victims
st.sidebar.header("Settings")
st.sidebar.markdown("<div style='color: orange;'><strong>Customize your scenario:</strong></div>", unsafe_allow_html=True)
victim_count = st.sidebar.number_input(
    "Enter the number of swimmers available to be victims:", min_value=1, value=5, step=1
)

# Generate scenario button
if st.button("Generate Scenario"):
    athlete_scenario, coach_notes = generate_serc_scenario(victim_count)

    # Display scenarios
    st.subheader("Scenario Description (Athlete Version):")
    st.markdown(
        f"<div style='padding:10px; background-color:#ffedcc; border: 2px solid black; border-radius:10px; color:black;'>{athlete_scenario}</div>", 
        unsafe_allow_html=True
    )

    st.subheader("Coach’s Notes:")
    st.markdown(
        f"<div style='padding:10px; background-color:#ffd9b3; border: 2px solid orange; border-radius:10px; color:black;'>{coach_notes}</div>", 
        unsafe_allow_html=True
    )

# Add custom styling for mobile optimization
st.markdown(
    """
    <style>
        /* Mobile-first styles */
        @media (max-width: 768px) {
            .css-ffhzg2 { /* Adjusts text style of the title */
                font-size: 24px;
                text-align: center;
            }
            .css-1v3v2qg { /* Adjusts sidebar layout */
                width: 100%;
                padding: 5px;
            }
            .stButton>button { /* Makes the button larger and more touch-friendly */
                width: 100%;
                padding: 20px;
                font-size: 16px;
                margin-top: 10px;
            }
            .stMarkdown, .stSubheader { /* Adjusts text for better readability */
                font-size: 16px;
                padding: 10px;
            }
            /* Adjusts box styling for mobile */
            .stMarkdown div {
                padding: 10px;
                font-size: 14px;
            }
            /* Makes inputs larger and more user-friendly on mobile */
            .stNumberInput>div>div>input {
                font-size: 18px;
                padding: 10px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)
