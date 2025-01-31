from model.shell_model import Shell, db

class ShellService:
    @staticmethod
    async def get_all_shells():
        return Shell.query.all()

    @staticmethod
    async def create_shell(data):
        required_fields = ['name', 'species', 'description']
    
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"{field} is required")
    
        shell = Shell(**data)
        db.session.add(shell)
        db.session.commit()
        return shell

    @staticmethod
    async def get_shell(id):
          return Shell.query.get_or_404(id)

    @staticmethod
    async def update_shell(id, data):
        shell = Shell.query.get_or_404(id)
        for key, value in data.items():
            setattr(shell, key, value)
        db.session.commit()
        return shell

    @staticmethod
    async def delete_shell(id):
        shell = Shell.query.get_or_404(id)
        db.session.delete(shell)
        db.session.commit()
