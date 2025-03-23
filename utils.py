import json



topics =  [
    {"category": "Nigerian Sports", "sub_category": "Super Eagles at AFCON "},
    {"category": "Nigerian Movies", "sub_category": "Nollywood Blockbusters"},
    {"category": "Nigerian Sports", "sub_category": "World Cup"},
    {"category": "Nigerian Music", "sub_category": "Fuji Music by Ayinde Barrister"},
    {"category": "Nigerian Music", "sub_category": "Fuji Music by Kollington Ayinla"},
    {"category": "Nigerian Music", "sub_category": "Fuji Music by Wasiu Alabi Pasuma"},
    {"category": "Nigerian Music", "sub_category": "Afrobeat by Fela Kuti"},
    {"category": "Nigerian Music", "sub_category": "Afrobeat by Tony Allen"},
    {"category": "Nigerian Music", "sub_category": "Afrobeat Influence"},
    {"category": "Nigerian Music", "sub_category": "Afrobeat Horn Section"},
    {"category": "Nigerian Sports", "sub_category": "Super Eagles 1996 Olympics"},
    {"category": "Nigerian Sports", "sub_category": "Super Eagles Coaches"},
    {"category": "Nigerian Sports", "sub_category": "Nigerian Football League (NPFL)"},
    {"category": "Nigerian Sports", "sub_category": "Nigerian Basketball"},
    {"category": "Nigerian Sports", "sub_category": "Nigerian Athletics"},
    {"category": "Nigerian Sports", "sub_category": "Nigerian Boxing"},
    {"category": "Nigerian Movies", "sub_category": "Nollywood Directors"},
    {"category": "Nigerian Movies", "sub_category": "Igbo Epic Films"},
    {"category": "Nigerian Movies", "sub_category": "Nollywood Actors"},
    {"category": "Nigerian Movies", "sub_category": "Technical aspects of Nollywood film production in specific decades"},
    {"category": "Nigerian Movies", "sub_category": "The history of specific Nollywood film studios"},
    {"category": "Nigerian Movies", "sub_category": "The effect of streaming services on Nollywood Production."},
    {"category": "Nigerian Movies", "sub_category": "The history of specific Nollywood awards shows."},
    {"category": "Nigerian History/Culture", "sub_category": "Benin Empire Art"},
    {"category": "Nigerian History/Culture", "sub_category": "Oyo Empire Politics"},
    {"category": "Nigerian History/Culture", "sub_category": "Igbo Kingdoms"},
    {"category": "Nigerian History/Culture", "sub_category": "Hausa Trade Routes"},
    {"category": "Nigerian History/Culture", "sub_category": "Nigerian Colonial History"},
    {"category": "Nigerian History/Culture", "sub_category": "Nigerian Civil War"},
    {"category": "Nigerian History/Culture", "sub_category": "Nigerian Literature"},
    {"category": "Nigerian History/Culture", "sub_category": "Nigerian Traditional Arts and Crafts"},
    {"category": "Nigerian History/Culture", "sub_category": "Nigerian Food and Cuisine"},
    {"category": "Nigerian Music", "sub_category": "Highlife"},
    {"category": "Nigerian Music", "sub_category": "Juju Music"},
    {"category": "Nigerian Music", "sub_category": "Contemporary Nigerian Pop (Afropop/Afrobeats)"},
    {"category": "Nigerian Music", "sub_category": "Gospel Music"},
    {"category": "International Politics", "sub_category": "The Cold War and its African Impact"},
    {"category": "International Finance", "sub_category": "The 2008 Global Financial Crisis"},
    {"category": "World History", "sub_category": "The Fall of the Berlin Wall"},
    {"category": "Global Technology", "sub_category": "The Rise of the Internet"},
    {"category": "World Entertainment", "sub_category": "Michael Jackson's Music Career"},
    {"category": "Global Sports", "sub_category": "The 1994 FIFA World Cup"},
    {"category": "World Literature", "sub_category": "Nobel Prize Winners in Literature"},
    {"category": "World Science", "sub_category": "The Human Genome Project"},
    {"category": "General Knowledge", "sub_category": "Major World Capitals"},
    {"category": "General Knowledge", "sub_category": "Important Historical Figures"},
    {"category": "World Literature", "sub_category": "The works of Shakespeare"},
    {"category": "World Literature", "sub_category": "The rise of post-colonial literature"},
    {"category": "World Literature", "sub_category": "The influence of magical realism"},
    {"category": "World Science", "sub_category": "The discovery of DNA"},
    {"category": "World Science", "sub_category": "The development of nuclear energy"},
    {"category": "World Science", "sub_category": "The theory of relativity"},
    {"category": "General Knowledge", "sub_category": "Major World Religions"},
    {"category": "General Knowledge", "sub_category": "Important Scientific Discoveries"},
    {"category": "General Knowledge", "sub_category": "Major Global Organizations (UN, WHO, etc.)"},
    {"category": "International Politics", "sub_category": "The Iranian Revolution"},
    {"category": "International Finance", "sub_category": "The creation of the World Trade Organization"},
    {"category": "World History", "sub_category": "The Russian Revolution"},
    {"category": "Global Technology", "sub_category": "The development of GPS"},
    {"category": "World Entertainment", "sub_category": "The rise of Bollywood"},
    {"category": "Global Sports", "sub_category": "The history of the Cricket World Cup"},
    {"category": "World Literature", "sub_category": "The works of Jane Austen"},
    {"category": "World Science", "sub_category": "The discovery of Penicillin"},
    {"category": "World History", "sub_category": "The Apartheid Era in South Africa"},
    {"category": "Global Technology", "sub_category": "The Space Race"},
    {"category": "Global Technology", "sub_category": "The invention of the personal computer"},
    {"category": "Global Technology", "sub_category": "The development of mobile phones"},
    {"category": "World Entertainment", "sub_category": "The Beatles' Influence on Music"},
    {"category": "World Entertainment", "sub_category": "The rise of Hollywood's Golden Age"},
    {"category": "World Entertainment", "sub_category": "The advent of MTV and music videos"},
    {"category": "Global Sports", "sub_category": "The Olympic Boycotts of the 1980s"},
    {"category": "Global Sports", "sub_category": "Muhammad Ali's Boxing Career"},
    {"category": "Nigerian Music", "sub_category": "The Role of DJs in Nigerian Music Evolution"},
    {"category": "Nigerian Sports", "sub_category": "Nigerian Players in European Leagues (2000s)"},
    {"category": "Nigerian Sports", "sub_category": "D'Tigers at the Olympics"},
    {"category": "Nigerian Sports", "sub_category": "Nigerian Para-athletes and Paralympic Success"},
    {"category": "Nigerian Sports", "sub_category": "Rivalries in Nigerian Club Football"},
    {"category": "Nigerian Sports", "sub_category": "Nigerian Wrestlers and Traditional Wrestling"},
    {"category": "Nigerian Movies", "sub_category": "Nollywood Home Video Boom (1990s)"},
    {"category": "Nigerian Movies", "sub_category": "Yoruba Nollywood Classics"},
    {"category": "Nigerian Movies", "sub_category": "Kannywood (Hausa Film Industry)"},
    {"category": "Nigerian Movies", "sub_category": "Evolution of Special Effects"},
    {"category": "Global Technology", "sub_category": "Cybersecurity Trends in the 21st Century"},
    {"category": "Global Technology", "sub_category": "The Rise of Blockchain and Cryptocurrency"},
    {"category": "Global Technology", "sub_category": "The Ethics of Genetic Engineering"},
    {"category": "Global Technology", "sub_category": "The Future of Renewable Energy Technology"},
    {"category": "Global Technology", "sub_category": "The Impact of Social Media on Global Communication"},
    {"category": "Global Technology", "sub_category": "Breakthroughs in Space Exploration"},
    {"category": "World Science", "sub_category": "The Exploration of Mars"},
    {"category": "World Science", "sub_category": "The Role of Dark Matter in the Universe"},
    {"category": "World Science", "sub_category": "The Physics Behind Black Holes"},
    {"category": "World Science", "sub_category": "The History of the Periodic Table"},
    {"category": "World Science", "sub_category": "Medical Advancements in the Last Century"},
    {"category": "World Science", "sub_category": "The Future of Robotics in Everyday Life"},
    {"category": "World Science", "sub_category": "The Origins of the Universe and the Big Bang Theory"}
]




def extract_json(response_text):
    try:
        json_str = response_text.strip()  # Remove leading/trailing whitespace
        if json_str.startswith("```json"):
            json_str = json_str[7:]  # Remove ```json\n
        if json_str.endswith("```"):
            json_str = json_str[:-3]  # Remove trailing ```
        
        data = json.loads(json_str)
        
        if isinstance(data, list):  # Ensure we return a single dict if it's a list
            return data[0] if data else None
        return data

    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Response text:\n{response_text}")  # Debugging output
        return None