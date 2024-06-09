from model.project import Project


def test_add_project(app, config):
    old_projects = app.soap.get_project_list(username=config['webadmin']["username"],
                                             password=config['webadmin']["password"])
    project = Project(name="test_name", description="test_description")
    app.project.create(project)
    new_projects = app.soap.get_project_list(username=config['webadmin']["username"],
                                             password=config['webadmin']["password"])
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
