import typer
import uvicorn

from tifa.cli.auth import group_auth
from tifa.cli.db import group_db
from tifa.cli.scaffold import group_scaffold

banner = """

                                                                    
                                                                    
         tttt            iiii     ffffffffffffffff                  
      ttt:::t           i::::i   f::::::::::::::::f                 
      t:::::t            iiii   f::::::::::::::::::f                
      t:::::t                   f::::::fffffff:::::f                
ttttttt:::::ttttttt    iiiiiii  f:::::f       ffffffaaaaaaaaaaaaa   
t:::::::::::::::::t    i:::::i  f:::::f             a::::::::::::a  
t:::::::::::::::::t     i::::i f:::::::ffffff       aaaaaaaaa:::::a 
tttttt:::::::tttttt     i::::i f::::::::::::f                a::::a 
      t:::::t           i::::i f::::::::::::f         aaaaaaa:::::a 
      t:::::t           i::::i f:::::::ffffff       aa::::::::::::a 
      t:::::t           i::::i  f:::::f            a::::aaaa::::::a 
      t:::::t    tttttt i::::i  f:::::f           a::::a    a:::::a 
      t::::::tttt:::::ti::::::if:::::::f          a::::a    a:::::a 
      tt::::::::::::::ti::::::if:::::::f          a:::::aaaa::::::a 
        tt:::::::::::tti::::::if:::::::f           a::::::::::aa:::a
          ttttttttttt  iiiiiiiifffffffff            aaaaaaaaaa  aaaa
                                                                    

            A opinionated fastapi starter since 2020.04.15 by @twocucao

"""

cli = typer.Typer()


def builtin_runserver():
    uvicorn.run("tifa.app:current_app", port=8000, reload=True, access_log=False)


@cli.command()
def start():
    typer.echo(banner)
    builtin_runserver()


@cli.command()
def runserver():
    typer.echo(banner)
    builtin_runserver()


@cli.command()
def shell_plus():
    typer.echo(f"shell_plus")


cli.add_typer(group_scaffold, name="g")
cli.add_typer(group_auth, name="auth")
cli.add_typer(group_db, name="db")
