class Pipe:
    
    def __init__(self,name):
        self.name = name
        self.actions = []
        
        g.pipes[self.name] = self #quando inicia se coloca na instancia de pipe.
        g.pipe_list.append(self)
    
    def update_action(self, action):
        
        #atualiza a ação e retorna se ação esta bloqueando
        if not action.active:
            action.start()
        action.update()
        return action.blocking
    
    def update(self):
        ran_action = False
        for action in self.actions:
            if not action.blockable:
                ran_action = self.update_action(action) or ran_action
                
            else:
                if ran_action:
                    continue
                else:
                    ran_action = self.update_action(action) or ran_action
    def add_action(self, action):
        """
        Adiciona uma nova ação ao pipe
        """
        self.actions.append(action)
        action.pipe = self