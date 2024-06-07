from model.project import Project
import random
from random import randint


def test_del_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(
            Project(name="test_name" + str(randint(1, 100000)),
                    description='description' + str(randint(1, 100000))))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects