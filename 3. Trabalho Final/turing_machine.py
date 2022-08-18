class Tape(object):
    
    blank_symbol = " "
    
    def __init__(self, tape_string = ""):
        self.list = tape_string
        self.__tape = dict((enumerate(tape_string)))
       
        
    def __str__(self):
        s = "".join(map(str, list(self.__tape.values())))
        return s
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class TuringMachine(object):
    
    def __init__(self, tape = "", blank_symbol = " ", initial_state = "", final_states = None, transition_function = None):
        self.__tape = Tape(tape) # pilha
        self.__head_position = 0 # posicao da cabeca
        self.__blank_symbol = blank_symbol #simbolo vazio
        self.__current_state = initial_state #Estado atual
        self.number = 0

        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self):
        return str(self.__tape)
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        self.number = self.number + 1
        input_ = (self.__current_state, char_under_head)
        if input_ in self.__transition_function:
            output_ = self.__transition_function[input_]
            print("Transicao ", output_)
            self.__tape[self.__head_position] = output_[1]
            if output_[2] == "R":
                self.__head_position += 1
            elif output_[2] == "L":
                self.__head_position -= 1
            self.__current_state = output_[0]
        return self.__current_state

    def final(self):
        if self.__current_state in self.__final_states or self.number == len(str(self.get_tape)):
            return True
        else:
            return False
        
    def string_process(self):
        while not self.final():
            self.step()

