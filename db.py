from firebase import firebase


def update_result(name, result):
    db = firebase.FirebaseApplication('https://yonchi-97f33.firebaseio.com/', authentication=None)
    all_users = db.get("/users", None)
    for k, v in all_users.items():
        nickname = v['name'].encode('utf-8')
        record = v['record']
        if nickname == name:
            if result > record:
                db.patch('users/' + k, data={"record": result})
                return
            else:
                return
    db.post('/users', data={"name": name, "record": result}, params={'print': 'pretty'})
    return
