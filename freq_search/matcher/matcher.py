class matcher:
    def __init__(self, tally=None):
        if tally is None:
            tally = {"oct":0, "nov":0, "dec":0, "jan":0, "feb":0, "mar":0}

class realmatcher(matcher):
    def 

dei_dict = {
    "ability":[
        r"accessib(le|ility)",
        r"(dis)?ability",
        "mental health",
        "people-centered care",
        "at risk"
    ],
    "class":[
        r"oppress(ion|ive)",
        r"privileges?",
        "socioeconomic",
        "status",
        r"systemic(ally)?"
    ],
    "climate":[
        "clean energy",
        r"climate (crisis|science)",
        r"environment(al)?",
        "pollution"
    ],
    "gs":[
        r"gender ?(ideology|diversity|based|-affirming)",
        r"assigned (fe)?male at birth",
        r"sexual(ity)? (preferences)?",
        r"LGBTQ?",
        r"trans(gender|sexual)"
    ],
    "re":[
        r"(multi)?cultural(ly)? ?(competence|differences|heritage|sensitivity|appropriate|responsive)?",
        r"ethnic(ity)?",
        r"rac(e|ial(ly)?|ism)",
        "Latinx",
        "Native American",
        "Black",
    ]
}
