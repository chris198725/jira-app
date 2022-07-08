from app.project import Project


projects = Project.find()  # input search criteria if necessary
permission_scheme_id = 'input integer permission scheme id here'  # default scheme is 0


for project in projects:
    r = project.change_permission(permission_scheme_id)
    print("%s - %s" % (r, project.key))

