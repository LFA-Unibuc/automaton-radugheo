class Automaton():
    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")
        self.alf = set()
        self.states = set()
        self.fstates = set()
        self.transitions = []
        self.istate = ''
        self.dfaDict = dict()
        self.read_input(config_file)

    def validate(self):
        """Return a Boolean
        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        return "I can't tell if the config file is valid... yet!"

    def accepts_input(self, input_str):
        """Return a Boolean
        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        input = open(input_str, "r")
        text_input = input.readlines()
        cnt = 0
        self.n = 3
        for linie in text_input:
            if linie.startswith('\n') or linie.startswith("#") or 'States' in linie or 'Transitions' in linie:
                continue
            elif "Sigma" in linie:
                cnt = 1
                continue
            elif linie.startswith('End'):
                cnt += 1
                continue
            if cnt == 1:
                self.alf.add(linie.strip())
            elif cnt == 2:
                if len(linie.strip().split(', ')) > 2:
                    self.states.add(linie.strip().split()[0])
                    if linie.strip().split(',')[2] == 'F' or linie.strip().split(',')[1] == 'F':
                        self.fstates.add(linie.strip().split(' ,')[0])
                    elif linie.strip().split(',')[2] == 'S' or linie.strip().split(',')[1] == 'S':
                        self.istate = linie.strip().split(' ,')[0]
                elif len(linie.strip().split(',')) == 2:
                    self.states.add(linie.strip().split()[0])
                    if linie.strip().split(',')[1] == 'S':
                        self.istate = linie.strip().split(' ,')[0]
                    elif linie.strip().split(',')[1] == 'F':
                        self.fstates.add(linie.strip().split(' ,')[0])
                else:
                    self.states.add(linie.strip())
            if cnt == 3:
                text = linie.strip().split(", ")
                for i in range(len(text)):
                    if i == 1:
                        text[i] = text[i][:-1]
                self.transitions.append(tuple(text))
        ok = 1
        for transition in self.transitions:
            if transition[1] not in self.alf or transition[0] not in self.states or transition[2] not in self.states:
                print("Invalid input.")
                ok = 0
                return 0
        if ok == 1:
            dictionary = {}
            for transition in self.transitions:
                state1 = transition[0]
                word = transition[1]
                state2 = transition[2]

                if state1 not in dictionary.keys():
                    dt = {}
                    if word not in dt.keys():
                        dt[word] = []
                        dt[word].append(state2)
                    else:
                        dt[word].append(state2)
                    dictionary[state1] = dt
                else:
                    if word not in dt.keys():
                        dictionary[state1][word] = []
                        dictionary[state1][word].append(state2)
                    else:
                        dictionary[state1][word].append(state2)

            self.dfaDict = dictionary
            print("Valid input. GG.")
        return 1

if __name__ == "__main__":
    a = Automaton('date.in')
    a.read_input('date.in')