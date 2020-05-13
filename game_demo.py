class Prot:
    def __init__(self, name, exp=100, skills= []):
        self.name = name
        self.exp = exp
        self.skills = skills

    def earned(self):
        self.exp = 100
        return self

    def say_name(self):
        if self.exp > 10:
            self.exp -= 5
            return f"I'm {self.name}"
        return "I need more exp yet"

    def learn_new_skill(self, new_skill, cost_to_learn):
        if self.exp >= cost_to_learn:
            self.exp -= cost_to_learn
            self.skills.append(new_skill)
            return f"I now know {new_skill.upper()}"
        return "I need more experience to learn new skills"
