from model.shell_model import Shell, db

class ShellDAO:
    def get_all_shells(self):
        return Shell.query.all()

    def create_shell(self, data):
        shell = Shell(**data)
        db.session.add(shell)
        db.session.commit()
        return shell

    def get_shell(self, id):
        return Shell.query.get_or_404(id)

    def update_shell(self, id, data):
        shell = Shell.query.get_or_404(id)
        for key, value in data.items():
            setattr(shell, key, value)
        db.session.commit()
        return shell

    def delete_shell(self, id):
        shell = Shell.query.get_or_404(id)
        db.session.delete(shell)
        db.session.commit()