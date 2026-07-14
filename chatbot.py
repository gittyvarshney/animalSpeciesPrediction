animal_info = {
    "Butterfly": {
        "scientific_name": "Rhopalocera",
        "category": "Insect",
        "habitat": "Gardens, forests, grasslands",
        "diet": "Nectar from flowers",
        "lifespan": "2 to 4 weeks",
        "weight": "Less than 1 gram",
        "speed": "8-20 km/h",
        "legs": "6",
        "sound": "Butterflies do not produce sounds.",
        "color": "Various vibrant colors",
        "domesticated": "No",
        "fact": "Butterflies taste with their feet."
    },

    "Cat": {
        "scientific_name": "Felis catus",
        "category": "Mammal",
        "habitat": "Homes and urban areas",
        "diet": "Carnivore",
        "lifespan": "12-18 years",
        "weight": "3-6 kg",
        "speed": "48 km/h",
        "legs": "4",
        "sound": "Meow",
        "color": "Many colors",
        "domesticated": "Yes",
        "fact": "Cats spend about 70% of their lives sleeping."
    },

    "Cow": {
        "scientific_name": "Bos taurus",
        "category": "Mammal",
        "habitat": "Farms and grasslands",
        "diet": "Herbivore",
        "lifespan": "15-20 years",
        "weight": "500-900 kg",
        "speed": "40 km/h",
        "legs": "4",
        "sound": "Moo",
        "color": "Black, white, brown",
        "domesticated": "Yes",
        "fact": "Cows have a stomach with four compartments."
    },

    "Dog": {
        "scientific_name": "Canis lupus familiaris",
        "category": "Mammal",
        "habitat": "Homes worldwide",
        "diet": "Omnivore",
        "lifespan": "10-15 years",
        "weight": "10-40 kg",
        "speed": "72 km/h",
        "legs": "4",
        "sound": "Bark",
        "color": "Many colors",
        "domesticated": "Yes",
        "fact": "Dogs have an excellent sense of smell."
    },

    "Elephant": {
        "scientific_name": "Loxodonta africana",
        "category": "Mammal",
        "habitat": "Forests and savannas",
        "diet": "Herbivore",
        "lifespan": "60-70 years",
        "weight": "2500-7000 kg",
        "speed": "40 km/h",
        "legs": "4",
        "sound": "Trumpet",
        "color": "Gray",
        "domesticated": "No",
        "fact": "Elephants are the largest land animals on Earth."
    },

    "Horse": {
        "scientific_name": "Equus ferus caballus",
        "category": "Mammal",
        "habitat": "Grasslands and farms",
        "diet": "Herbivore",
        "lifespan": "25-30 years",
        "weight": "380-1000 kg",
        "speed": "88 km/h",
        "legs": "4",
        "sound": "Neigh",
        "color": "Brown, black, white, gray",
        "domesticated": "Yes",
        "fact": "Horses can sleep while standing."
    },

    "Sheep": {
        "scientific_name": "Ovis aries",
        "category": "Mammal",
        "habitat": "Farms and grasslands",
        "diet": "Herbivore",
        "lifespan": "10-12 years",
        "weight": "45-160 kg",
        "speed": "40 km/h",
        "legs": "4",
        "sound": "Baa",
        "color": "Mostly white",
        "domesticated": "Yes",
        "fact": "Sheep have excellent memories for recognizing faces."
    },

    "Spider": {
        "scientific_name": "Araneae",
        "category": "Arachnid",
        "habitat": "Forests, gardens and houses",
        "diet": "Insects",
        "lifespan": "1-3 years",
        "weight": "Less than 100 grams",
        "speed": "1.9 km/h",
        "legs": "8",
        "sound": "Spiders do not produce vocal sounds.",
        "color": "Various colors",
        "domesticated": "No",
        "fact": "Spiders are not insects; they are arachnids."
    },

    "Squirrel": {
        "scientific_name": "Sciuridae",
        "category": "Mammal",
        "habitat": "Forests, parks and gardens",
        "diet": "Nuts, fruits, seeds",
        "lifespan": "6-12 years",
        "weight": "250-700 grams",
        "speed": "32 km/h",
        "legs": "4",
        "sound": "Chatter",
        "color": "Brown, gray, red",
        "domesticated": "No",
        "fact": "Squirrels help forests grow by burying nuts they never retrieve."
    }
}


def chatbot(species, question):
    """
    species -> predicted animal
    question -> user's question
    """

    if species not in animal_info:
        return "Sorry, I don't have information about that animal."

    data = animal_info[species]
    q = question.lower().strip()

    greetings = [
        "hi", "hello", "hey", "good morning",
        "good afternoon", "good evening"
    ]

    if q in greetings:
        return (
            f"Hello! 👋 I identified the animal as **{species}**.\n\n"
            "You can ask me:\n"
            "• What does it eat?\n"
            "• Where does it live?\n"
            "• Scientific name\n"
            "• Weight\n"
            "• Lifespan\n"
            "• Speed\n"
            "• Number of legs\n"
            "• Sound\n"
            "• Category\n"
            "• Color\n"
            "• Interesting fact"
        )

    if any(k in q for k in ["diet", "eat", "food", "feeds", "consume"]):
        return f"🥗 {species}s are **{data['diet'].lower()}**. They mainly eat {data['diet'].lower()} food."

    if any(k in q for k in ["habitat", "live", "where", "forest", "home", "found"]):
        return f"🌍 {species}s are commonly found in **{data['habitat']}**."

    if any(k in q for k in ["life", "lifespan", "age", "years"]):
        return f"⏳ The average lifespan of a {species} is **{data['lifespan']}**."

    if any(k in q for k in ["weight", "heavy", "mass"]):
        return f"⚖️ An adult {species} usually weighs **{data['weight']}**."

    if any(k in q for k in ["speed", "fast", "run"]):
        return f"🏃 A {species} can reach speeds of about **{data['speed']}**."

    if any(k in q for k in ["scientific", "latin"]):
        return f"📚 The scientific name of {species} is **{data['scientific_name']}**."

    if any(k in q for k in ["category", "type", "mammal", "bird", "insect", "arachnid"]):
        return f"📖 {species} belongs to the **{data['category']}** category."

    if any(k in q for k in ["legs", "feet"]):
        return f"🦵 A {species} has **{data['legs']} legs**."

    if any(k in q for k in ["sound", "voice", "noise"]):
        return f"🔊 {species}s typically make this sound: **{data['sound']}**"

    if any(k in q for k in ["color", "colour"]):
        return f"🎨 {species}s are commonly **{data['color']}**."

    if any(k in q for k in ["domestic", "domesticated", "pet", "wild"]):
        return f"🏡 Domesticated: **{data['domesticated']}**."

    if any(k in q for k in ["fact", "interesting", "special", "tell me more"]):
        return f"💡 Fun Fact: {data['fact']}"

    if any(k in q for k in ["help", "options"]):
        return (
            "You can ask me:\n\n"
            "• What does it eat?\n"
            "• Where does it live?\n"
            "• Scientific name\n"
            "• Weight\n"
            "• Lifespan\n"
            "• Speed\n"
            "• Number of legs\n"
            "• Sound\n"
            "• Category\n"
            "• Color\n"
            "• Interesting fact\n"
            "• Is it domesticated?"
        )

    return (
        "❓ I couldn't understand that question.\n\n"
        "Try asking:\n"
        "• What does it eat?\n"
        "• Where does it live?\n"
        "• Scientific name\n"
        "• Weight\n"
        "• Lifespan\n"
        "• Speed\n"
        "• Number of legs\n"
        "• Sound\n"
        "• Interesting fact"
    )