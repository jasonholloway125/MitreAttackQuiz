import json
import traceback as tb
import sys

class MitreAttackQuiz(dict):
    def __init__(self, file_path:str):
        super().__init__()

        self.__title = """
███╗   ███╗██╗████████╗██████╗ ███████╗     █████╗ ████████╗████████╗██╗    ██████╗██╗  ██╗     ██████╗ ██╗   ██╗██╗███████╗
████╗ ████║██║╚══██╔══╝██╔══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██║   ██╔════╝██║ ██╔╝    ██╔═══██╗██║   ██║██║╚══███╔╝
██╔████╔██║██║   ██║   ██████╔╝█████╗      ███████║   ██║      ██║████████╗██║     █████╔╝     ██║   ██║██║   ██║██║  ███╔╝ 
██║╚██╔╝██║██║   ██║   ██╔══██╗██╔══╝      ██╔══██║   ██║      ██║██╔═██╔═╝██║     ██╔═██╗     ██║▄▄ ██║██║   ██║██║ ███╔╝  
██║ ╚═╝ ██║██║   ██║   ██║  ██║███████╗    ██║  ██║   ██║      ██║██████║  ╚██████╗██║  ██╗    ╚██████╔╝╚██████╔╝██║███████╗
╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝╚═════╝   ╚═════╝╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝                                                                                                                            
"""

        self['file_path'] = file_path
        self['data'] = self.__open_data__(file_path)

    def __open_data__(self, file_path)->dict:
        data = {}        
        with open(file_path, 'r') as in_file:
            try:
                data = json.load(in_file)
            except Exception:
                print(tb.format_exc())
        return data
    
    def __choose_option__(self, prompt_msg:str, options:list[str], invalid_msg:str, spacing:int=2)->str:
        print("\n"*spacing)
        in_valid = False
        while(not in_valid):
            in1 = input(prompt_msg)
            if in1 not in options:
                print(invalid_msg)
                continue
            return in1
        
    def __match_technique__(self, techniques:dict, sub:bool=False):
        if sub: prompt = "Enter sub-technique {0}:\n>"
        else: prompt = "Enter technique {0}:\n>"
        for k, v in techniques.items():
            inp = input(prompt.format(k))
            if inp.strip().upper() == v['name'].upper():
                print("CORRECT\n")
            else:
                print(f"INCORRECT: {v['name']}\n")
            if 'sub_techniques' in v and len(v['sub_techniques'].keys()) > 0:
                self.__match_technique__(v['sub_techniques'], True)
        
    def __ordered__(self, type:int):
        data = self['data']['tactics'].items()
        match type:
            case 1:
                for k1,v1 in data:
                    print(f"\n\n\n{v1['name'].upper()} {k1.upper()} TECHNIQUES")
                    self.__match_technique__(v1['techniques'])
                        
            case 2:
                pass
            case 3:
                pass

    def __randomized__(self):
        pass

    
    def run(self, title:bool=True):
        if title:
            print(self.__title)    

        opt1 = self.__choose_option__("(1) Please select an option:\n1>Ordered\n2>Randomized\n>", ["1", "2"], "Invalid Option\n")
        opt2 = self.__choose_option__("(2) Please select an option:\n1>Name\n2>Description\n3>Go Back\n>", ["1", "2", "3"], "Invalid Option\n")

        if opt2 == "3":
            del opt1, opt2
            return self.run(False)

        match opt1:
            case "1":
                self.__ordered__(int(opt2)) 
            case "2":
                self.__randomized__()
            case _:
                return
        
        
        
                




if __name__ == '__main__':
    quiz = MitreAttackQuiz(sys.argv[1])
    quiz.run()
    