
@auth.requires_login()
def manage_clients():
    grid = SQLFORM.grid(db.client, user_signature=False)
    rows = db().select(db.client.ALL)
    return response.render("clients/liste.html",dict(grid=grid))


@auth.requires_login()
def manage_employees():
    grid = SQLFORM.grid(db.employee, user_signature=False)
    return response.render("Employee/liste.html",dict(grid=grid))

@auth.requires_login()
def manage_contracts():
    grid = SQLFORM.grid(db.contract, user_signature=False)
    return response.render("contrats/liste.html",dict(grid=grid))

@auth.requires_login()
def manage_interventions():
    grid = SQLFORM.grid(db.intervention, user_signature=False)
    return response.render("interventions/liste.html",dict(grid=grid))


def delete_client():
    id = request.vars.id
    db(db.client.id == id).delete()
    redirect(URL('Controller', 'manage_clients'))


def acceuil():
    return response.render("default/index.html")