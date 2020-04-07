
import gitlab
import os

baseurl = os.getenv("GITLAB_BASE_URL","") 
lixiGitlabApi = os.getenv("SHANE_LIXI_GITLAB_API","") 


class SingeltonGitlab():
    __instance = None
    @staticmethod
    def getInstance():
        if SingeltonGitlab.__instance == None:
            SingeltonGitlab()
        return SingeltonGitlab.__instance

    def __init__(self):
        if SingeltonGitlab.__instance!=None:
            raise Exception("This class is a singelton")
        else:
            if baseurl and lixiGitlabApi:
                SingeltonGitlab.__instance = gitlab.Gitlab(baseurl,lixiGitlabApi)
            else:
                raise ValueError("Make sure gitlab base url and api related environment variables are loaded. Try 'pipenv shell' to load them")

