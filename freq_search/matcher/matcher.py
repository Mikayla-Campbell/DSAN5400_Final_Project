class Matcher:
    dei_dict = {
        "ability": [
            r"[Aa]ccessib(le|ility)",
            r"([Dd]is)?ability",
            r"[Mm]ental health",
            r"[Pp]eople-centered care",
            r"[Aa]t risk"
        ],
        "class": [
            r"[Oo]ppress(ion|ive)",
            r"[Pp]rivileges?",
            r"[Ss]ocioeconomic",
            r"[Ss]tatus",
            r"[Ss]ystemic(ally)?"
        ],
        "climate": [
            r"[Cc]lean energy",
            r"[Cc]limate (crisis|science)",
            r"[Ee]nvironment(al)?",
            r"[Pp]ollution"
        ],
        "gs": [
            r"[Gg]ender ?(ideology|diversity|based|-affirming)",
            r"[Aa]ssigned (fe)?male at birth",
            r"[Ss]exual(ity)? (preferences)?",
            r"LGBTQ?",
            r"[Tt]rans(gender|sexual)"
        ],
        "re": [
            r"([Mm]ulti)?cultural(ly)? ?(competence|differences|heritage|sensitivity|appropriate|responsive)?",
            r"[Ee]thnic(ity)?",
            r"[Rr]ac(e|ial(ly)?|ism)",
            "Latinx",
            "Native American",
            "Black",
        ]
    }
    def __init__(self, dei_dict):
        self.dei_dict = dei_dict

    def match:
        pass


class RealMatcher(Matcher):
    def counts(self):
        for a in abstract:
            if dei_dict in abstract


