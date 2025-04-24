import nltk
import logging
import re
import matplotlib.pyplot as plt

class Matcher:

    def __init__(self, oct_list, nov_list, dec_list, jan_list, feb_list, mar_list):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            filename='../../logs.txt')
        logging.info("Instantiating instance of Matcher.")
        self.month_dict = {"oct": oct_list, "nov": nov_list, "dec": dec_list,
                           "jan": jan_list, "feb": feb_list, "mar": mar_list}

        self.tally = {"oct": 0, "nov": 0, "dec": 0, "jan": 0, "feb": 0, "mar": 0}
        self.dei_dict = {
            "ability": [
                r"[Aa]ccessib(?:le|ility)",
                r"(?:[Dd]is)?ability",
                r"[Mm]ental health",
                r"[Pp]eople-centered care",
                r"[Aa]t risk"
            ],
            "class": [
                r"[Oo]ppress(?:ion|ive)",
                r"[Pp]rivileges?",
                r"[Ss]ocioeconomic",
                r"[Ss]tatus",
                r"[Ss]ystemic(?:ally)?"
            ],
            "climate": [
                r"[Cc]lean energy",
                r"[Cc]limate (?:crisis|science)",
                r"[Ee]nvironment(?:al)?",
                r"[Pp]ollution"
            ],
            "gs": [
                r"[Gg]ender ?(?:ideology|diversity|based|-affirming)",
                r"[Aa]ssigned (?:fe)?male at birth",
                r"[Ss]exual(?:ity)? (?:preferences)?",
                r"LGBTQ?",
                r"[Tt]rans(?:gender|sexual)"
            ],
            "re": [
                r"(?:[Mm]ulti)?cultural(?:ly)? ?(?:competence|differences|heritage|sensitivity|appropriate|responsive)?",
                r"[Ee]thnic(?:ity)?",
                r"[Rr]ac(?:e|ial(?:ly)?|ism)",
                "Latinx",
                "Native American",
                "Black",
            ]
        }

    def __str__(self):
        return (
            f"Oct: {len(self.oct_list)} items, "
            f"Nov: {len(self.nov_list)} items, "
            f"Dec: {len(self.dec_list)} items, "
            f"Jan: {len(self.jan_list)} items, "
            f"Feb: {len(self.feb_list)} items, "
            f"Mar: {len(self.mar_list)} items"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"oct_list={self.oct_list}, "
            f"nov_list={self.nov_list}, "
            f"dec_list={self.dec_list}, "
            f"jan_list={self.jan_list}, "
            f"feb_list={self.feb_list}, "
            f"mar_list={self.mar_list})"
        )

    def match(self, category):
        logging.info("Entered match function.")
        logging.info("Matching for category {}".format(category))
        for month, month_abstract_list in self.month_dict.items():
            tally = 0
            for abstract in month_abstract_list:
                #logging.info("abstract {}".format(abstract))
                for pattern in self.dei_dict[category]:
                    matches = re.findall(pattern, abstract)
                    tally += len(matches)
                    if matches:
                        logging.info("Found matches: " + str(matches))
            self.tally[month] = tally

        logging.info("Final tally: {}".format(self.tally))
        logging.info("Plotting graph...")

        self.graph_plot(category)
        return self.tally

    def graph_plot(self, category):
        logging.info("Entered graph_plot function.")

        # format title
        if category == "re":
            category = "Race / Ethnicity"
        elif category == "gs":
            category = "Gender / Sexuality"
        else:
            category = category.upper()

        plt.bar(self.tally.keys(), self.tally.values())
        plt.title(category)
        plt.xlabel('Months')
        plt.ylabel('Term Usage')
        plt.show()