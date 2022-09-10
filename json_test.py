from regex import F
import src.JsonDB as JsonDB
dic=JsonDB.read_json(filename='./src/jsonfile/database.json')
dic['command'].update({'gametag':'print ตอนนี้กำลังเล่น>> {game_name} << to user end'})
JsonDB.write_json(filename='./src/jsonfile/database.json',data= dic)
def command_read_database(Input_command,user_name):
    if Input_command in dic['command']:
        commandp=dic['command'][Input_command]
        command= commandp.split()
        command_str=""
        for v in command:
            try:
                if v == 'print':
                    command_str+=f'ctx.send(\' '
                elif v=='to':
                    command_str+=f' @'
                elif v=='user':
                    command_str+=f'{"{"}{user_name}{"}"}'
                elif v=='{game_name}':
                    command_str+='{game_name}'
                elif v=='end':
                    command_str+='\')'
                else:
                    command_str+=f' {v}'
            except Exception as e:
                command_str=f'ctx.send({e})'
        return command_str
print(command_read_database('discord','rabbitz'))

        
