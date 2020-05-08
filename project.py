from gitlab_singleton import SingeltonGitlab as Git
class Project (Git):
    def __init__(self,projectId,milestoneTitle):
        self.milestoneTitle = milestoneTitle
        self.projectId = projectId
        self.__getProject()
       
    def __getProject(self):
        self.git = self.getInstance()
        with self.git as g:
            self.project = g.projects.get(self.projectId)
            self.webUrl = self.project.web_url
            self.id = self.project.id
            self.groupId = self.project.namespace["id"]
            self.group = g.groups.get(self.groupId)

    def milestone(self):
            return next(m for m in self.group.milestones.list() if m.title == self.milestoneTitle)

    def issue(self,issue_iid):
        '''Return project issue object to perform changes '''
        return self.project.issues.get(issue_iid)

    def getProjectLabels(self):
        return self.project.labels.list()

    def filterSchematronLabels(self):
        labels = self.project.labels.list()
        return [lbl.name for lbl in labels if "Rule" in lbl.name[-4:]]

    def filterStandardLables(self):
        labels = self.project.labels.list()
        return [lbl.name for lbl in labels if len(lbl.name)==3]