from model.project import Project
import random
from random import randint


def test_del_project(app, db, config):
    if len(app.soap.get_project_list()) == 0:
        app.project.create(
            Project(name="test_name" + str(randint(1, 100000)),
                    description='description' + str(randint(1, 100000))))
    old_projects = app.soap.get_project_list(username=config['webadmin']["username"],
                                             password=config['webadmin']["password"])
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username=config['webadmin']["username"],
                                             password=config['webadmin']["password"])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects