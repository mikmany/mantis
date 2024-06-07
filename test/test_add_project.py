from model.project import Project


def test_add_project(app, db):
    old_projects = db.get_project_list()
    project = Project(name="test_name", description="test_description")
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
