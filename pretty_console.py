class color_printer:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Print key in Header color and the message in  "WARNING", "OKBLUE", "OKGREEN" , "FAIL", "BOLD", or with "UNDERLINE"
    @staticmethod
    def print_key_val_warning(key,value,rjust=0):
        # print(f"{color_printer.HEADER}{key.rjust(rjust)}: {color_printer.WARNING} {value}{color_printer.ENDC}")
        print(color_printer.HEADER + key.rjust(rjust) + ": " +color_printer.WARNING + value + color_printer.ENDC)
    
    @staticmethod
    def print_key_val_fail(key,value,rjust=0):
        # print(f"{color_printer.HEADER}{key.rjust(rjust)}: {color_printer.FAIL} {value}{color_printer.ENDC}")
        print(color_printer.HEADER + key.rjust(rjust) + ": " + color_printer.FAIL + value + color_printer.ENDC)

    @staticmethod
    def print_key_val_blue(key,value,rjust=0):
        # print(f"{color_printer.HEADER}{key.rjust(rjust)}: {color_printer.OKBLUE} {value}{color_printer.ENDC}")
        print(color_printer.HEADER + key.rjust(rjust) + ": " + color_printer.OKBLUE + value + color_printer.ENDC)

    @staticmethod
    def print_key_val_green(key,value,rjust=0):
        # print(f"{color_printer.HEADER}{key.rjust(rjust)}: {color_printer.OKBLUE} {value}{color_printer.ENDC}")
        print(color_printer.HEADER + key.rjust(rjust) + ": " + color_printer.OKBLUE + value + color_printer.ENDC)

    @staticmethod
    def print_key_val_bold(key,value,rjust=0):
        # print(f"{color_printer.HEADER}{key.rjust(rjust)}: {color_printer.BOLD} {value}{color_printer.ENDC}")    
        print(color_printer.HEADER + key.rjust(rjust) + ": " + color_printer.BOLD + value + color_printer.ENDC)    

    @staticmethod
    def print_key_val_underlined(key,value,rjust=0):
        # print(f"{color_printer.HEADER}{key.rjust(rjust)}: {color_printer.UNDERLINE} {value}{color_printer.ENDC}")
        print(color_printer.HEADER + key.rjust(rjust) +": " + color_printer.UNDERLINE + value + color_printer.ENDC)

#  print a string in Header
    @staticmethod
    def print_header(string,padding=0,):
        # print(f"{color_printer.HEADER}{string.rjust(padding)}{color_printer.ENDC}")
        print(color_printer.HEADER + string.rjust(padding) + color_printer.ENDC)

#  print a string in yellow
    @staticmethod
    def print_warning(string,padding=0,):
        # print(f"{color_printer.WARNING}{string.rjust(padding)}{color_printer.ENDC}")   
        print(color_printer.WARNING +string.rjust(padding)+color_printer.ENDC)   

 #  print a string in Red   
    @staticmethod
    def print_fail(string,padding=0,):
        # print(f"{color_printer.FAIL}{string.rjust(padding)}{color_printer.ENDC}")
        print(color_printer.FAIL + string.rjust(padding) + color_printer.ENDC)

 #  print a string in Blue   
    @staticmethod
    def print_ok_blue(string,padding=0,):
        # print(f"{color_printer.OKBLUE}{string.rjust(padding)}{color_printer.ENDC}")
        print(color_printer.OKBLUE + string.rjust(padding) + color_printer.ENDC)

 #  print a string in Green   
    @staticmethod
    def print_ok_green(string,padding=0,):
        # print(f"{color_printer.OKGREEN}{string.rjust(padding)}{color_printer.ENDC}")
        print(color_printer.OKGREEN + string.rjust(padding)+ color_printer.ENDC)

 #  print a string in Bold   
    @staticmethod
    def print_bold(string,padding=0,):
        # print(f"{color_printer.BOLD}{string.rjust(padding)}{color_printer.ENDC}")
        print(color_printer.BOLD + string.rjust(padding) + color_printer.ENDC)

 #  print a string with Underline   
    @staticmethod
    def print_underline(string,padding=0,):
        # print(f"{color_printer.UNDERLINE}{string.rjust(padding)}{color_printer.ENDC}")
        print(color_printer.UNDERLINE + string.rjust(padding) + color_printer.ENDC)

