class color_printer():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    colors = {
        "HEADER" : '\033[95m',
        "OKBLUE" : '\033[94m',
        "OKGREEN" : '\033[92m',
        "WARNING" : '\033[93m',
        "FAIL" : '\033[91m',
        "ENDC" : '\033[0m',
        "BOLD" : '\033[1m',
        "UNDERLINE" : '\033[4m',
    }

    @classmethod
    def color_format_key_value(cls,key:str,value:str,colorValue:str="WARNING",rightJustify:int=0):
        '''
        Color print a key and value phrase
        - key : string that describes the data
        - value: string that descirbes key
        - colorValue : string represention of a color 
        # Example of colorValues are: HEADER, OKBLUE, OKGREEN, WARNING, FAIL, BOLD, UNDERLINE
        '''
        return "{HEADER}{key}: {colorValue}{value}{ENDC}".format(**cls.colors,key=key.rjust(rightJustify),value=value, colorValue=cls.colors[colorValue])

    @classmethod
    def color_format_string(cls,phrase:str,colorValue:str="WARNING",rightJustify:int=0):
        '''
        Returns colored phrase
        - colorValue : string represention of a color 
        * example of colorValues HEADER, OKBLUE, OKGREEN, WARNING, FAIL, BOLD, UNDERLINE
        '''
        return "{colorValue}{phrase}{ENDC}".format(**cls.colors,colorValue=cls.colors[colorValue],phrase=phrase.rjust(rightJustify))

    @classmethod
    def printProgressBar (cls,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        prefix = cls.color_format_string(str(prefix),"HEADER",20)
        percent = cls.color_format_string(("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total))),"HEADER")
        filledLength = int(length * iteration // total)
        bar = cls.color_format_string(fill * filledLength + '-' * (length - filledLength),"OKBLUE")
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()

if __name__=="__main__":
    print(color_printer.color_format_key_value("Key","value","OKBLUE",18))
    print(color_printer.color_format_string("This is a phrase","OKGREEN",18))

    

