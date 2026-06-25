from flask import Flask
app = Flask(__name__)
id_proof_counts = {}


class Member:

    def __init__(self, name, id_number, id_proof, referrer=None):
        if id_proof_counts.get(id_proof, 0) >= 3:
            raise Exception("ఈ ఐడీ ప్రూఫ్‌తో ఇప్పటికే మూడు ఐడీలు రిజిస్టర్ అయ్యాయి.")

        self.name = name
        self.id_number = id_number
        self.id_proof = id_proof
        self.referrer = referrer
        self.downline = []
        
if referrer:
referrer.downline.append(self)
        id_proof_counts[id_proof] = id_proof_counts.get(id_proof, 0) + 1

    def display_info(self):
        referrer_name = (
            self.referrer.name if self.referrer else "ఎవరూ లేరు"
        )
        return f"సభ్యుడి పేరు: {self.name}, ID: {self.id_number}, ID ప్రూఫ్: {self.id_proof}, జాయిన్ చేసినవారు: {referrer_name}"


# ఉదాహరణకు ఒకరిని ఎలా జాయిన్ చేయవచ్చో ఇక్కడ చూడండి:
root_member = Member("అభి", "101", "Aadhar")
member2 = Member("రాము", "102", "PAN", root_member)

print(root_member.display_info())
print(member2.display_info())
@app.route("/")
def home():
    return "నా యాప్ విజయవంతంగా రన్ అవుతోంది!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
